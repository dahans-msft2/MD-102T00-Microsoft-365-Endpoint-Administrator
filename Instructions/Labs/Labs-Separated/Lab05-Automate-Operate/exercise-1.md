# Lab 05, Exercise 1: Automate with Microsoft Graph PowerShell

### Scenario

Microsoft Graph is a REST API that provides programmatic access to Microsoft 365 services, including Intune. You'll register an application in Microsoft Entra ID for unattended automation, authenticate with the Graph PowerShell SDK, and perform common management tasks via PowerShell.

### Task 1: Install the Microsoft Graph PowerShell SDK

1. On **SEA-DEV1**, open **Windows Terminal (Admin)**.

1. Install the Microsoft Graph PowerShell SDK:

   ```powershell
   Install-Module Microsoft.Graph -Scope AllUsers -Force
   ```

   > [!NOTE]
   > The Microsoft.Graph module is a meta-package that installs all Graph PowerShell modules. If prompted to install from an untrusted repository, type **Y** and press Enter.

1. Verify the installation:

   ```powershell
   Get-Module -Name Microsoft.Graph.* -ListAvailable
   ```

   The output should show multiple Microsoft.Graph.* modules (e.g., Microsoft.Graph.Authentication, Microsoft.Graph.Intune, Microsoft.Graph.Users).

**You have successfully installed the Microsoft Graph PowerShell SDK.**

---

### Task 2: Register an application for unattended automation

For interactive automation, you can use delegated permissions (user signs in). For unattended automation (e.g., scheduled scripts), you need application permissions and a client secret or certificate.

1. On **SEA-DEV1**, open **Microsoft Edge** and navigate to **https://entra.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Entra admin center**, in the left navigation, expand **Entra ID** and select **App registrations**.

   > [!NOTE]
   > In the current Entra portal, **App registrations** is a direct child of **Entra ID** — there's no "Applications" parent node. (The older "Identity → Applications → App registrations" path no longer exists.)

1. Select **+ New registration**.

1. On the **Register an application** page, enter:
   - **Name:** `Intune Automation App`
   - **Supported account types:** **Single tenant only - Contoso** (the default; this is the modern label for "Accounts in this organizational directory only")
   - **Redirect URI:** Leave blank

1. Select **Register**.

1. On the **Intune Automation App** overview page, note the following:
   - **Application (client) ID:** (copy this value—you'll need it for authentication)
   - **Directory (tenant) ID:** (copy this value)

**You have successfully registered an application for Graph API access.**

---

### Task 3: Grant API permissions to the application

1. In the **Intune Automation App** details, select **API permissions** from the left navigation.

1. Select **Add a permission**.

1. In the **Request API permissions** pane, select **Microsoft Graph**.

1. Select **Application permissions** (not Delegated permissions).

1. Search for and select the following permissions:
   - **DeviceManagementManagedDevices.Read.All** (read device information)
   - **DeviceManagementConfiguration.ReadWrite.All** (read/write configuration policies)
   - **DeviceManagementApps.ReadWrite.All** (read/write applications)

   > [!NOTE]
   > Application permissions run with the application's identity, not the user's identity. They are suitable for unattended automation but require admin consent.

1. Select **Add permissions**.

1. On the **API permissions** page, select **Grant admin consent for <TenantPrefix>**.

1. In the confirmation dialog, select **Yes**.

1. Verify all permissions show a green checkmark under **Status** (indicating admin consent granted).

**You have successfully granted API permissions to the application.**

---

### Task 4: Create a client secret

1. In the **Intune Automation App** details, select **Certificates & secrets** from the left navigation.

1. Under **Client secrets**, select **New client secret**.

1. In the **Add a client secret** pane, enter:
   - **Description:** `Automation secret for PowerShell scripts`
   - **Expires:** 6 months (or 12 months, depending on your policy)

1. Select **Add**.

1. **Immediately copy the secret value** (the long alphanumeric string under **Value**).

   > [!WARNING]
   > The client secret is only displayed once. If you lose it, you must generate a new secret.

1. Save the secret securely (e.g., in Azure Key Vault or a password manager). For lab purposes, save it in a text file on SEA-DEV1 (e.g., `C:\LabScripts\ClientSecret.txt`).

**You have successfully created a client secret for unattended authentication.**

---

### Task 5: Authenticate with Microsoft Graph using application credentials

1. On **SEA-DEV1**, open **Windows Terminal** (Admin).

1. Create a folder for automation scripts:

   ```powershell
   New-Item -Path "C:\LabScripts" -ItemType Directory -Force
   ```

1. Create a PowerShell script to authenticate with the application credentials:

   ```powershell
   $tenantId = "<Your Tenant ID>"
   $clientId = "<Your Application (client) ID>"
   $clientSecret = "<Your Client Secret>"

   # Convert client secret to secure string
   $secureSecret = ConvertTo-SecureString $clientSecret -AsPlainText -Force

   # Create credential object
   $credential = New-Object System.Management.Automation.PSCredential ($clientId, $secureSecret)

   # Connect to Microsoft Graph
   Connect-MgGraph -TenantId $tenantId -ClientSecretCredential $credential

   # Verify connection
   Get-MgContext
   ```

   Replace `<Your Tenant ID>`, `<Your Application (client) ID>`, and `<Your Client Secret>` with the values you copied earlier.

1. Save the script as `C:\LabScripts\Connect-GraphApp.ps1`.

1. Run the script:

   ```powershell
   .\Connect-GraphApp.ps1
   ```

1. Verify the connection by reviewing the output of `Get-MgContext`:
   - **TenantId:** Should match your tenant ID
   - **Scopes:** Should show the granted application permissions
   - **AuthType:** Should show "AppOnly"

**You have successfully authenticated to Microsoft Graph using application credentials.**

---

### Task 6: Query managed devices using Graph PowerShell

1. In the PowerShell session (with Graph connected), query all managed devices:

   ```powershell
   Get-MgDeviceManagementManagedDevice | Select-Object DeviceName, OperatingSystem, ComplianceState, LastSyncDateTime
   ```

1. Review the output. You should see SEA-DEV1 and SEA-DEV2 listed with their compliance status.

1. Query devices with specific filters:

   ```powershell
   # Get devices running Windows
   Get-MgDeviceManagementManagedDevice -Filter "operatingSystem eq 'Windows'" | Select-Object DeviceName, OperatingSystem

   # Get non-compliant devices
   Get-MgDeviceManagementManagedDevice -Filter "complianceState eq 'noncompliant'" | Select-Object DeviceName, ComplianceState
   ```

1. Query the configuration profiles tagged with the `Pharmacy` scope tag (created in **Lab 01 Exercise 2 Task 6** and applied to profiles in **Labs 02–04**). This is the canonical Graph-PowerShell way to enumerate everything a delegated admin (Pharmacy Helpdesk) would see.

   > [!NOTE]
   > The `roleScopeTags` collection is exposed only via the **beta** Graph endpoint at the time of writing, so this lookup uses `Invoke-MgGraphRequest` directly rather than a typed `Get-Mg*` cmdlet:

   ```powershell
   # Resolve the Pharmacy scope tag's numeric ID via the beta endpoint
   $tagsResp = Invoke-MgGraphRequest -Method GET -Uri 'https://graph.microsoft.com/beta/deviceManagement/roleScopeTags'
   $pharmacyTag = $tagsResp.value | Where-Object { $_.displayName -eq 'Pharmacy' }
   if ($pharmacyTag) {
       Write-Output "Pharmacy scope tag ID: $($pharmacyTag.id)"
   } else {
       Write-Output "Pharmacy scope tag not found - confirm it was created in Lab 01 Exercise 2 Task 6"
   }

   # List all device configuration profiles that include the Pharmacy scope tag
   Get-MgDeviceManagementDeviceConfiguration -All |
       Where-Object { $_.AdditionalProperties.roleScopeTagIds -contains $pharmacyTag.id } |
       Select-Object DisplayName, Id

   # List all compliance policies tagged Pharmacy
   Get-MgDeviceManagementDeviceCompliancePolicy -All |
       Where-Object { $_.AdditionalProperties.roleScopeTagIds -contains $pharmacyTag.id } |
       Select-Object DisplayName, Id
   ```

   > [!NOTE]
   > The Graph API surfaces scope tag membership on a per-object basis via the `roleScopeTagIds` array. This is the underlying field the Intune admin center reads when it filters what a delegated admin sees. Querying it directly via Graph is how you'd build a compliance dashboard scoped to a delegated team — or audit which policies a particular scope tag is applied to.

**You have successfully queried managed devices and Pharmacy-scoped policies using Microsoft Graph PowerShell.**

---

### Task 7: Create a compliance policy using Graph API

You'll create a Windows compliance policy using the Graph API (instead of the Intune admin center).

1. In the PowerShell session, define the compliance policy JSON payload. Note the **`scheduledActionsForRule`** block at the end — the Graph API requires every compliance policy to have **exactly one** block action, so this nested object is mandatory:

   ```powershell
   $compliancePolicyJson = @"
   {
     "@odata.type": "#microsoft.graph.windows10CompliancePolicy",
     "displayName": "Graph API - Windows Compliance Policy",
     "description": "Compliance policy created via Microsoft Graph PowerShell",
     "passwordRequired": true,
     "passwordBlockSimple": true,
     "passwordMinimumLength": 8,
     "passwordRequiredType": "alphanumeric",
     "osMinimumVersion": "10.0.19041",
     "bitLockerEnabled": true,
     "secureBootEnabled": true,
     "codeIntegrityEnabled": true,
     "storageRequireEncryption": true,
     "scheduledActionsForRule": [
       {
         "ruleName": "PasswordRequired",
         "scheduledActionConfigurations": [
           {
             "actionType": "block",
             "gracePeriodHours": 0,
             "notificationTemplateId": "",
             "notificationMessageCCList": []
           }
         ]
       }
     ]
   }
   "@
   ```

   > [!IMPORTANT]
   > The properties available on **`windows10CompliancePolicy`** in v1.0 are limited to Windows-device-health attestation settings (BitLocker, Secure Boot, Code Integrity, password rules, storage encryption). Firewall, antivirus, and Defender-related properties live on `windows10MobileCompliancePolicy` or require beta-only types. The full v1.0 property list is at [Microsoft Graph → Create windows10CompliancePolicy](https://learn.microsoft.com/graph/api/intune-deviceconfig-windows10compliancepolicy-create?view=graph-rest-1.0).

1. Create the policy using the Graph API:

   ```powershell
   Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/deviceManagement/deviceCompliancePolicies" -Body $compliancePolicyJson -ContentType "application/json"
   ```

1. Verify the policy was created:

   ```powershell
   Get-MgDeviceManagementDeviceCompliancePolicy | Where-Object { $_.DisplayName -eq "Graph API - Windows Compliance Policy" } | Select-Object DisplayName, Description, Id
   ```

**You have successfully created a compliance policy using the Microsoft Graph API.**

---

### Task 8: Assign the compliance policy to a group

1. Get the policy ID:

   ```powershell
   $policy = Get-MgDeviceManagementDeviceCompliancePolicy | Where-Object { $_.DisplayName -eq "Graph API - Windows Compliance Policy" }
   $policyId = $policy.Id
   ```

1. Get the target group ID (e.g., dyn-Windows-Devices):

   ```powershell
   $group = Get-MgGroup -Filter "displayName eq 'dyn-Windows-Devices'"
   $groupId = $group.Id
   ```

1. Create the assignment JSON payload. Note the `assignments` array wrapper \u2014 the `/assign` action accepts a collection, not a single assignment object:

   ```powershell
   $assignmentJson = @"
   {
     "assignments": [
       {
         "@odata.type": "#microsoft.graph.deviceCompliancePolicyAssignment",
         "target": {
           "@odata.type": "#microsoft.graph.groupAssignmentTarget",
           "groupId": "$groupId"
         }
       }
     ]
   }
   "@
   ```

1. Assign the policy to the group using the **`/assign`** action endpoint (not `/assignments`):

   ```powershell
   Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/deviceManagement/deviceCompliancePolicies/$policyId/assign" -Body $assignmentJson -ContentType "application/json"
   ```

   > [!NOTE]
   > Compliance-policy assignment is a Graph **action** (`/assign`) rather than a sub-collection POST (`/assignments`). The action takes the full assignment set and replaces any existing assignments \u2014 useful for idempotent automation scripts.

1. Verify the assignment in the Intune admin center:
   - Navigate to **Devices** → **Compliance policies** → **Graph API - Windows Compliance Policy** → **Assignments**

**You have successfully assigned a compliance policy to a group using Microsoft Graph API.**

---

**Previous:** [← Introduction](introduction.md) | **Next:** [→ Exercise 2: Deploy proactive remediations](exercise-2.md)

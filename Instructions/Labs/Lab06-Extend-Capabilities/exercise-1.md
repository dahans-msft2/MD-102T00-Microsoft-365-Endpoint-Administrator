# Lab 06, Exercise 1: Configure Endpoint Privilege Management (EPM)

### Scenario

Endpoint Privilege Management allows standard users to run specific applications with elevated privileges without granting full administrator rights. With the Intune Suite trial active (from **Lab 01** prerequisites), EPM is already provisioned in your tenant. You'll verify it's available, create elevation settings and rules policies, and test different elevation scenarios.

### Task 1: Verify Endpoint Privilege Management is available

**Endpoint Privilege Management** is one of the Microsoft Intune Suite add-on capabilities. With the Suite trial activated in **Lab 01** prerequisites, EPM is already provisioned in your tenant — there is no separate tenant-wide "Enable EPM" toggle. Instead, you enable EPM on individual devices by deploying a **Windows elevation settings policy** with the **Endpoint Privilege Management** setting set to **Enabled** (you'll do that in Task 2).

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Endpoint Privilege Management**.

1. Confirm the EPM blade loads with the following tabs across the top:
   - **Overview** (insights dashboard — may show "Insufficient data" on a new tenant)
   - **Reports** (elevation report, elevation requests, file trends)
   - **Policies** (where you'll create elevation settings and elevation rules policies)
   - **Reusable settings** (shared certificate groups for use across rules)
   - **Elevation requests** (live and historical support-approved elevation requests)

   > [!NOTE]
   > If the EPM blade shows a banner indicating the capability isn't licensed, return to **Lab 01 prerequisites** and complete the Microsoft Intune Suite trial activation before continuing. EPM requires either an active trial or purchased Microsoft Intune Suite licenses.

**You have successfully verified Endpoint Privilege Management is available.**

---

### Task 2: Create an elevation settings policy

Elevation settings policies define the default elevation behavior for devices — and they're also what **enables EPM on a device** in the first place. The `Endpoint Privilege Management` setting inside this policy is what installs the EPM agent and starts evaluating elevation requests.

1. In the **Microsoft Intune admin center**, on the **Endpoint Privilege Management** page, select the **Policies** tab.

1. Select **+ Create** from the top toolbar.

1. In the **Create a profile** pane, set:
   - **Platform:** Windows
   - **Profile:** **Windows elevation settings policy**

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `EPM Settings - Default Behavior`
   - **Description:** `Default EPM settings for the Contoso fleet`

1. Select **Next**.

1. On the **Configuration settings** page, configure:
   - **Endpoint Privilege Management:** **Enabled** (this is the toggle that actually enables EPM on the device; leaving it disabled or removing the policy disables EPM on those devices after seven days)
   - **Default elevation response:** **Require user confirmation**
   - **Validation:** **Business justification** (require the user to enter a reason)
   - **Send data to Microsoft for reporting:** **Diagnostic data and managed elevations only** (enables the **Elevation report** under the **Reports** tab to populate)

   > [!NOTE]
   > The four elevation responses are **Not Configured**, **Deny all requests**, **Require support approval**, and **Require user confirmation**. "Not Configured" behaves the same as "Deny all requests". Pick `Require user confirmation` for this lab so you can see the EPM prompt later in Task 6 — in production, the security-stronger choice for unknown files is `Deny all requests` paired with explicit elevation rules.

1. Select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select** → **Next** → **Create**.

**You have successfully created an elevation settings policy.**

---

### Task 3: Create an automatic elevation rule

Automatic elevation rules allow specific applications to always run elevated without user prompts.

1. On the **Endpoint Privilege Management** page, on the **Policies** tab, select **+ Create**.

1. In the **Create a profile** pane, set **Platform** to **Windows** and **Profile** to **Windows elevation rules policy**. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `EPM Rules - Automatic Elevation`
   - **Description:** `Allows Registry Editor to always run elevated`

1. Select **Next**.

1. On the **Elevation rules** page, select **Add** → **File rule**.

1. In the **Create rule** pane, configure:
   - **Rule name:** `Elevate Registry Editor`
   - **Description:** `Automatically elevates regedit.exe without user prompt`
   - **Elevation type:** Automatic
   - **File path:** `C:\Windows\regedit.exe`
   - **File hash:** Leave blank (allow any version)
   - **Certificate:** Leave blank (no certificate requirement)

   > [!NOTE]
   > File-based rules target specific executables by path. You can also create rules based on file hash, publisher certificate, or product name for more precise targeting.

1. Select **OK** to add the rule.

1. Select **Next** → **Assign to `sg-Intune-Pilot-Users`** (pilot-first rollout for EPM — same cohort as the blocking ESP, pilot update ring, and Block-mode ASR rules from earlier labs) → **Next** → **Create**.

**You have successfully created an automatic elevation rule scoped to the pilot cohort.**

---

### Task 4: Create a user-confirmed elevation rule

User-confirmed elevation rules prompt the user to approve elevation (with optional business justification).

1. On the **Endpoint Privilege Management** page, on the **Policies** tab, select **+ Create**.

1. In the **Create a profile** pane, set **Platform** to **Windows** and **Profile** to **Windows elevation rules policy**. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `EPM Rules - User Confirmed Elevation`
   - **Description:** `Prompts user to approve elevation for MSConfig`

1. Select **Next**.

1. On the **Elevation rules** page, select **Add** → **File rule**.

1. In the **Create rule** pane, configure:
   - **Rule name:** `Elevate MSConfig with User Confirmation`
   - **Elevation type:** User confirmed
   - **File path:** `C:\Windows\System32\msconfig.exe`
   - **Require business justification:** Yes

1. Select **OK** → **Next** → **Assign to `sg-Intune-Pilot-Users`** → **Next** → **Create**.

**You have successfully created a user-confirmed elevation rule scoped to the pilot cohort.**

---

### Task 5: Create a support-approved elevation rule

Support-approved elevation rules require a help desk agent to approve elevation requests remotely.

1. On the **Endpoint Privilege Management** page, on the **Policies** tab, select **+ Create**.

1. In the **Create a profile** pane, set **Platform** to **Windows** and **Profile** to **Windows elevation rules policy**. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `EPM Rules - Support Approved Elevation`
   - **Description:** `Requires help desk approval for CMD elevation`

1. Select **Next**.

1. On the **Elevation rules** page, select **Add** → **File rule**.

1. In the **Create rule** pane, configure:
   - **Rule name:** `Elevate Command Prompt with Support Approval`
   - **Elevation type:** Support approved
   - **File path:** `C:\Windows\System32\cmd.exe`

1. Select **OK** → **Next** → **Assign to `sg-Intune-Pilot-Users`** → **Next** → **Create**.

> [!NOTE]
> **Pilot-first EPM rollout.** All three elevation policies target the pilot cohort initially. Watch the **Endpoint privilege management** → **Reports** → **Elevation summary** for a week. Confirm the automatic rule isn't being abused (legitimate registry edits only), the user-confirmed rule's business-justifications look reasonable, and the support-approved rule's request volume is manageable. Then expand each policy's assignment to `dyn-Windows-Devices` (with `sg-Intune-Pilot-Users` excluded). Same pattern as the ASR rollout in Lab 04 Exercise 2.

**You have successfully created a support-approved elevation rule scoped to the pilot cohort.**

---

### Task 6: Test EPM elevation on CL3

1. Switch to **CL3** (this device should be enrolled with a standard user account, e.g., Alex Wilber).

1. Sign in as **AlexW@<TenantPrefix>.OnMicrosoft.com** (standard user, not a local administrator).

1. Force a device sync to apply the EPM policies:
   - **Settings** → **Accounts** → **Access work or school** → **Connected to Contoso** → **Info** → **Sync**

1. Wait 10–15 minutes for policies to apply.

1. Test **automatic elevation** (Registry Editor):
   - Open the **Start menu** and search for `regedit`
   - Launch **Registry Editor**
   - **Expected behavior:** The app launches elevated without prompting (automatic elevation rule applied)

1. Test **user-confirmed elevation** (MSConfig):
   - Open the **Start menu** and search for `msconfig`
   - Launch **System Configuration**
   - **Expected behavior:** A prompt appears asking the user to confirm elevation and provide business justification
   - Enter a justification (e.g., "Troubleshooting startup issues") and approve

1. Test **support-approved elevation** (Command Prompt):
   - Open the **Start menu** and search for `cmd`
   - Right-click **Command Prompt** and select **Run with elevated access** (if EPM is configured)
   - **Expected behavior:** A prompt appears indicating the request is pending help desk approval

   > [!NOTE]
   > In a production environment, a help desk agent would see the elevation request in the **Endpoint privilege management** dashboard and approve or deny it remotely.

**You have successfully tested EPM elevation scenarios.**

---

### Task 7: Monitor EPM elevation reports

1. On **CL1**, in the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Endpoint privilege management** → **Reports**.

1. Select **Elevation summary** report.

1. Review the report data:
   - **Total elevations:** Count of all elevation requests
   - **Automatic elevations:** Count of automatic approvals
   - **User-confirmed elevations:** Count of user-approved requests
   - **Support-approved elevations:** Count of help desk-approved requests
   - **Denied elevations:** Count of blocked requests

1. Select **Elevation details** to view individual elevation events:
   - **Device name**
   - **User name**
   - **Application name**
   - **Elevation type**
   - **Timestamp**
   - **Business justification** (if provided)

**You have successfully monitored EPM elevation reports.**

---

**Previous:** [← Introduction](introduction.md) | **Next:** [→ Exercise 2: Deploy Remote Help](exercise-2.md)

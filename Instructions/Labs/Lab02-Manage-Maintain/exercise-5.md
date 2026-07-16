# Lab 02, Exercise 5: Enable Endpoint analytics and proactive remediations

### Scenario

Endpoint analytics provides insights into device performance, startup times, and user experience. Proactive remediations automatically detect and fix common issues before users report problems.

### Task 1: Enable Endpoint analytics

1. In the **Microsoft Intune admin center**, expand **Reports**, expand the **Analytics** group, and select **Endpoint analytics**.

1. The first time you visit Endpoint analytics in a tenant, you land on the **Endpoint analytics | Introduction** page. Leave **Collect device data from** set to **All cloud-managed devices** and select **Start** to enable data collection.

   > [!NOTE]
   > If a previous admin has already started data collection, the **Start** button won't appear and you'll land on **Overview** instead. Skip to the next step.

1. Select **Settings** in the left navigation.

1. Review the **Intune data collection policy** section.

   > [!NOTE]
   > Endpoint analytics requires devices to send diagnostic data to Microsoft. This is automatically enabled for Intune-enrolled devices.

1. Verify the following toggles are enabled:
   - **Startup performance:** On
   - **Application reliability:** On
   - **Work from anywhere:** On
   - **Resource performance:** On
   - **Battery health:** On

1. Select **Save** (if any changes were made).

1. Return to the **Endpoint analytics | Overview** page.

   > [!NOTE]
   > Endpoint analytics requires 24–48 hours of device telemetry before displaying meaningful insights. In a new lab environment, the dashboard will show limited data. You can still review the dashboard structure and understand the metrics tracked.

1. In the left navigation, expand the **Reports** group and review the available reports:
   - **Startup performance:** Boot times and logon durations
   - **Application reliability:** App crashes and hangs
   - **Work from anywhere:** Cloud connectivity and recommended actions
   - **Resource performance:** CPU and memory utilization
   - **Battery health:** Battery condition and runtime

**You have successfully enabled Endpoint analytics.**

---

### Task 2: Create a proactive remediation script package

Proactive remediations run PowerShell scripts on devices to detect and fix issues automatically.

1. In the **Microsoft Intune admin center**, expand **Devices**, then under **Manage devices** select **Scripts and remediations**.

1. Select the **Remediations** tab (the page opens on this tab by default).

   > [!IMPORTANT]
   > The Remediations tab displays a banner: "Use of remediations requires Windows license verification to be enabled." Windows license verification is enabled by an Intune admin under **Tenant administration > Intune add-ons** and requires an Intune Suite or Remediations add-on entitlement. In a lab tenant without this enabled, you can still walk through the wizard, but the script package won't execute on devices.

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Remediation - Clear Temp Files`
   - **Description:** `Detects and clears temporary files older than 30 days`

1. Select **Next**.

1. On the **Settings** page, configure:
   - **Detection script file:** Select **Browse** and navigate to `C:\LabAssets\Remediations\Detect-TempFiles.ps1` (provided in lab assets).

     > [!NOTE]
     > If the script is not present, you can create it inline:
     > ```powershell
     > $tempPath = "$env:TEMP"
     > $oldFiles = Get-ChildItem -Path $tempPath -Recurse -File | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) }
     > if ($oldFiles.Count -gt 0) {
     >     Write-Output "Found $($oldFiles.Count) old temp files"
     >     exit 1  # Issue detected
     > } else {
     >     Write-Output "No old temp files found"
     >     exit 0  # Compliant
     > }
     > ```

   - **Remediation script file:** Select **Browse** and navigate to `C:\LabAssets\Remediations\Remediate-TempFiles.ps1`.

     Example remediation script:
     ```powershell
     $tempPath = "$env:TEMP"
     try {
         Get-ChildItem -Path $tempPath -Recurse -File | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Remove-Item -Force
         Write-Output "Cleared old temp files"
         exit 0  # Success
     } catch {
         Write-Error "Failed to clear temp files: $_"
         exit 1  # Failure
     }
     ```

   - **Run this script using the logged on credentials:** No (run as SYSTEM)
   - **Enforce script signature check:** No
   - **Run script in 64-bit PowerShell:** Yes

1. Select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created a proactive remediation script package.**

---

### Task 3: Monitor remediation execution

1. In the **Microsoft Intune admin center**, on the **Remediations** tab, select **Remediation - Clear Temp Files** from the list.

1. Select the **Device status** tab.

1. Review the device execution results:
   - **Detection status:** Shows whether the issue was detected
   - **Remediation status:** Shows whether the remediation succeeded or failed
   - **Last check-in:** Timestamp of last script execution

   > [!NOTE]
   > Proactive remediations run on a schedule (default: once per day). After initial policy deployment, wait 1–2 hours for the first execution, then check the results.

**You have successfully monitored proactive remediation execution.**

---

**Previous:** [← Exercise 4: Configure Windows Update management](exercise-4.md) | **Next:** [→ Exercise 6: Use the Troubleshooting blade](exercise-6.md)

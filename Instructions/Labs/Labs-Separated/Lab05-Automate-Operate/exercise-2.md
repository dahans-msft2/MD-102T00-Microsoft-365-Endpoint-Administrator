# Lab 05, Exercise 2: Deploy proactive remediations

### Scenario

Proactive remediations automatically detect and fix common device issues before users report them. The upper-intermediate pattern for any new remediation script is a **pilot-first rollout**: deploy to the pilot cohort, watch for detection-vs-remediation outcomes for a day or two, then expand to the broader fleet. You'll follow that pattern here — the same pilot group (`sg-Intune-Pilot-Users`) that received the blocking ESP (Lab 01), the Pilot update ring (Lab 02), and Block-mode ASR (Lab 04) gets the new remediation first.

### Task 1: Create detection and remediation scripts

1. On **CL1**, create a folder for remediation scripts:

   ```powershell
   New-Item -Path "C:\LabScripts\Remediations" -ItemType Directory -Force
   ```

1. Create the detection script (`Detect-StaleWindowsUpdateCache.ps1`):

   ```powershell
   @"
   # Detection script: Check for Windows Update cache files older than 30 days
   `$updateCachePath = "C:\Windows\SoftwareDistribution\Download"
   `$oldFiles = Get-ChildItem -Path `$updateCachePath -Recurse -File -ErrorAction SilentlyContinue | Where-Object { `$_.LastWriteTime -lt (Get-Date).AddDays(-30) }

   if (`$oldFiles.Count -gt 0) {
       Write-Output "Found `$(`$oldFiles.Count) stale Windows Update cache files"
       exit 1  # Issue detected
   } else {
       Write-Output "Windows Update cache is clean"
       exit 0  # Compliant
   }
   "@ | Out-File -FilePath "C:\LabScripts\Remediations\Detect-StaleWindowsUpdateCache.ps1" -Encoding UTF8
   ```

1. Create the remediation script (`Remediate-StaleWindowsUpdateCache.ps1`):

   ```powershell
   @"
   # Remediation script: Clear stale Windows Update cache files
   `$updateCachePath = "C:\Windows\SoftwareDistribution\Download"
   try {
       Stop-Service -Name wuauserv -Force -ErrorAction SilentlyContinue
       Get-ChildItem -Path `$updateCachePath -Recurse -File -ErrorAction SilentlyContinue | Where-Object { `$_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Remove-Item -Force -ErrorAction SilentlyContinue
       Start-Service -Name wuauserv -ErrorAction SilentlyContinue
       Write-Output "Stale Windows Update cache cleared"
       exit 0  # Success
   } catch {
       Write-Error "Failed to clear Windows Update cache: `$_"
       exit 1  # Failure
   }
   "@ | Out-File -FilePath "C:\LabScripts\Remediations\Remediate-StaleWindowsUpdateCache.ps1" -Encoding UTF8
   ```

**You have successfully created detection and remediation scripts.**

---

### Task 2: Upload the remediation script package to Intune

1. In **Microsoft Edge**, navigate to **https://intune.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Intune admin center**, expand **Devices** and select **Scripts and remediations**.

1. Select the **Remediations** tab.

1. Select **Create** → **Windows 10 and later**.

1. On the **Basics** page, enter:
   - **Name:** `Remediation - Clear Stale Windows Update Cache`
   - **Description:** `Detects and removes Windows Update cache files older than 30 days`

1. Select **Next**.

1. On the **Settings** page, configure:
   - **Detection script file:** Browse and select `C:\LabScripts\Remediations\Detect-StaleWindowsUpdateCache.ps1`
   - **Remediation script file:** Browse and select `C:\LabScripts\Remediations\Remediate-StaleWindowsUpdateCache.ps1`
   - **Run this script using the logged on credentials:** No (run as SYSTEM)
   - **Enforce script signature check:** No
   - **Run script in 64-bit PowerShell:** Yes

1. Select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users** (the pilot cohort from Lab 01 — you'll expand to the fleet in Task 4 after watching detection-vs-remediation results).

1. Select **Select**.

1. Select **Next** → **Create**.

**You have successfully uploaded the proactive remediation script package and assigned it to the pilot cohort.**

---

### Task 3: Monitor remediation execution

1. In the **Microsoft Intune admin center**, on the **Remediations** tab, select **Remediation - Clear Stale Windows Update Cache**.

1. Select **Device status** from the left navigation.

1. Wait 10–15 minutes for the remediation to run on devices.

   > [!NOTE]
   > Remediations run on a schedule (default: once per day). For faster testing, you can force a device sync or wait for the next sync cycle.

1. Review the device status:
   - **Detection status:** Shows whether the issue was detected (exit code 1) or not detected (exit code 0)
   - **Remediation status:** Shows whether the remediation succeeded (exit code 0) or failed (exit code 1)
   - **Last check-in:** Timestamp of last script execution

**You have successfully deployed and monitored a proactive remediation script.**

---

### Task 4: Expand the remediation from pilot to fleet

Once the pilot device status (Task 3) shows the detection script running cleanly (no false positives) and the remediation script succeeding (no script errors), you expand the assignment to the broader fleet. This is the canonical *pilot → fleet* rollout for any new remediation script.

1. In the **Microsoft Intune admin center**, on the **Remediations** tab, select **Remediation - Clear Stale Windows Update Cache**.

1. Select **Properties** from the left navigation, then in the **Assignments** section select **Edit**.

1. Add a second assignment under **Assign to** → **Add groups** → select **dyn-Windows-Devices**. Under **Exclude groups**, add **sg-Intune-Pilot-Users** (pilot already has it; no need to assign twice).

1. Select **Review + save** → **Save**.

   > [!NOTE]
   > A real production rollout would let the pilot run for 24–72 hours before this step, and you'd want to be confident the detection script's exit-code-1 rate matches the actual issue rate (i.e., no false positives) and the remediation succeeded every time it ran. For this lab, you're simulating the rollout flow.

**You have successfully expanded the remediation from pilot to the broader fleet.**

---

**Previous:** [← Exercise 1: Automate with Microsoft Graph PowerShell](exercise-1.md) | **Next:** [→ Exercise 3: Assign and verify the Pharmacy Helpdesk delegated role end-to-end](exercise-3.md)

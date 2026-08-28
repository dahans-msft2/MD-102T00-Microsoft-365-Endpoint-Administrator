# Lab 01, Exercise 6: Configure Windows Autopilot

### Scenario

Windows Autopilot streamlines device provisioning by automatically joining devices to Microsoft Entra ID and enrolling them in Intune during the out-of-box experience (OOBE). You'll register SEA-DEV3 for Autopilot, create a deployment profile, and assign it to the device.

> [!NOTE]
> Due to lab time constraints, you will not perform a full Autopilot OOBE (which requires resetting the device). You'll complete the registration and configuration steps to understand the Autopilot deployment workflow.

> [!NOTE]
> **This is classic Autopilot (hardware-hash based), not Windows Autopilot device preparation.** Device preparation is a newer, simpler re-architecture that skips manual hash registration entirely for its supported scenarios (user-driven, physical devices) — devices just enroll and get added to a security group at enrollment time. But it doesn't yet support pre-provisioned, self-deploying, existing-devices, hybrid join, or Autopilot Reset scenarios — those still require classic Autopilot. Manual hardware-hash registration (what you're doing here) is Microsoft's own documented approach for **testing and evaluation**, which is exactly this lab's context; production registration normally happens automatically via the OEM/reseller/CSP instead.

### Task 1: Generate the Autopilot hardware hash for SEA-DEV3

The Autopilot hardware hash uniquely identifies a device and is required for Autopilot registration.

1. Switch to **SEA-DEV3**.

1. Sign in with the local administrator account:
   - **Username:** `Admin`
   - **Password:** 

1. Right-click the **Start** button and select **Windows Terminal (Admin)**.

1. In the PowerShell session, create a folder for the output file and install the **Get-WindowsAutopilotInfo** script (this is a PowerShell Gallery **script**, not a module):

   ```powershell
   New-Item -ItemType Directory -Path C:\Autopilot -Force
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
   Install-Script -Name Get-WindowsAutopilotInfo -Force
   ```

1. After installation completes, generate the Autopilot hardware hash and export it to a CSV file:

   ```powershell
   Get-WindowsAutopilotInfo -OutputFile C:\Autopilot\SEA-DEV3-AutopilotHash.csv
   ```

1. Verify the CSV file was created:

   ```powershell
   Test-Path C:\Autopilot\SEA-DEV3-AutopilotHash.csv
   ```

   The output should return **True**.

1. Open the CSV file to verify the hardware hash was captured:

   ```powershell
   notepad C:\Autopilot\SEA-DEV3-AutopilotHash.csv
   ```

1. Review the CSV contents. It should contain:
   - **Device Serial Number**
   - **Windows Product ID**
   - **Hardware Hash** (long base64-encoded string)

1. Close Notepad.

**You have successfully generated the Autopilot hardware hash for SEA-DEV3.**

---

### Task 2: Upload the hardware hash to Intune

1. Switch to **SEA-DEV1**.

1. In **Microsoft Edge**, navigate to **https://intune.microsoft.com** (sign in as admin if needed).

1. In the **Microsoft Intune admin center**, expand **Devices** and select **Enrollment**.

1. Under **Windows Autopilot**, select **Devices** (under the Windows Autopilot Deployment Program section).

1. Select **Import** from the top toolbar.

1. In the **Import Windows Autopilot devices** pane, select the folder icon to browse for the CSV file.

1. Navigate to **\\\SEA-DEV3\C$\Autopilot\\** (or copy the CSV file from SEA-DEV3 to SEA-DEV1 using a shared folder or USB).

   > [!NOTE]
   > If you cannot access SEA-DEV3's file system from SEA-DEV1, manually copy the CSV file to SEA-DEV1 (e.g., save to a USB drive, or use the lab platform's file transfer mechanism).

1. Select **SEA-DEV3-AutopilotHash.csv** and select **Open**.

1. In the **Import Windows Autopilot devices** pane, select **Import**.

1. Wait for the import to complete. A notification will appear when the import finishes (typically 1–2 minutes).

1. After import completes, refresh the **Devices** page. You should see **SEA-DEV3** appear in the Autopilot devices list.

   > [!NOTE]
   > It may take 5–10 minutes for the device to fully sync and appear in the list. If the device doesn't appear immediately, refresh the page periodically.

**You have successfully uploaded the SEA-DEV3 hardware hash to Intune.**

---

### Task 3: Create a Windows Autopilot deployment profile

Autopilot deployment profiles define the OOBE experience and determine which settings users can configure during setup.

1. In the **Microsoft Intune admin center**, on the **Windows enrollment** page, select **Deployment Profiles** (under Windows Autopilot Deployment Program).

1. Select **Create profile** → **Windows PC**.

1. On the **Basics** page, enter:
   - **Name:** `Autopilot User-Driven Profile`
   - **Description:** `User-driven Microsoft Entra join profile for Windows Autopilot`
   - **Convert all targeted devices to Autopilot:** No

1. Select **Next**.

1. On the **Out-of-box experience (OOBE)** page, configure the following:
   - **Deployment mode:** User-driven
   - **Join to Microsoft Entra ID as:** Microsoft Entra joined
   - **Microsoft Software License Terms:** Hide
   - **Privacy Settings:** Hide
   - **Hide change account options:** Hide
   - **User account type:** Standard
   - **Allow pre-provisioned deployment:** No
   - **Apply device name template:** No

   > [!NOTE]
   > This configuration simplifies the OOBE by hiding unnecessary prompts. Users will sign in with their Microsoft Entra credentials, and the device will be automatically configured.

1. Select **Next** and **Next** again to skip **Scope tags**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **dyn-Autopilot-Devices**.

1. Select **Select**.

   > [!NOTE]
   > By assigning the profile to `dyn-Autopilot-Devices`, any device registered in Autopilot — enrolled or not — automatically receives this deployment profile, which is what actually lets SEA-DEV3's Profile status reach **Assigned** in Task 4.

1. Select **Next**.

1. On the **Review + create** page, review the settings and select **Create**.

**You have successfully created a Windows Autopilot deployment profile.**

---

### Task 4: Review the Autopilot profile status for SEA-DEV3

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Enrollment** → **Devices** (under Windows Autopilot).

1. Select **SEA-DEV3** from the Autopilot devices list.

1. Review the device details:
   - **Profile status:** Should now show **Assigned** (it may take a few minutes for the dynamic group to populate and the profile assignment to sync)
   - **Group tag:** None
   - **Assigned user:** None

   > [!NOTE]
   > If it still shows "Not assigned" after several minutes, select **Sync** from the toolbar on the **Devices** list to force a sync. Also double check `dyn-Autopilot-Devices` actually shows SEA-DEV3 as a member (**Groups** → `dyn-Autopilot-Devices` → **Members**) — if SEA-DEV3 isn't there, re-check the rule syntax from Task 3.

1. Close the device details pane.

**You have successfully assigned the Autopilot deployment profile to SEA-DEV3.**

---

### Task 5: (Optional) Understand the Autopilot OOBE flow

In a production environment, the next step would be to reset SEA-DEV3 and go through the Autopilot OOBE. Here's what would happen:

1. **Device boots:** SEA-DEV3 is powered on (factory-reset or new device).

1. **Autopilot recognition:** During OOBE, Windows contacts the Autopilot service and recognizes the device by its hardware hash.

1. **Profile download:** The device downloads the assigned Autopilot profile (`Autopilot User-Driven Profile`).

1. **Simplified OOBE:** The user sees a simplified OOBE with Microsoft branding:
   - No license terms or privacy prompts (hidden per profile settings)
   - User signs in with Microsoft Entra credentials (e.g., `AlexW@<TenantPrefix>.OnMicrosoft.com`)
   - Device automatically joins Microsoft Entra ID and enrolls in Intune

1. **Policy application:** After enrollment, Intune policies (configuration profiles, compliance policies, apps) are applied before the user reaches the desktop.

1. **User desktop:** The user reaches the desktop with a fully configured device.

> [!NOTE]
> Resetting SEA-DEV3 and completing a live Autopilot OOBE takes 20–30 minutes and is beyond the scope of this lab. However, you've completed all the prerequisites (hardware hash registration, profile creation, and assignment) required for Autopilot deployment.

**You now understand the Windows Autopilot deployment workflow.**

---

**Previous:** [← Exercise 5: Enroll Windows devices](exercise-5.md) | **Next:** [Lab summary →](summary.md)

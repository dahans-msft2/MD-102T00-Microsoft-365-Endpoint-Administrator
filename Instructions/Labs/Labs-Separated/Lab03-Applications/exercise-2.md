# Lab 03, Exercise 2: Package and deploy a Win32 application

### Scenario

Win32 apps are traditional Windows desktop applications (.exe, .msi installers). You'll package a Win32 app using the Microsoft Win32 Content Prep Tool, create a detection rule, and deploy it to managed devices.

### Task 1: Prepare the Win32 app package

1. On **SEA-DEV1**, verify the Win32 Content Prep Tool is available at `C:\Program Files\IntuneWinAppUtil\IntuneWinAppUtil.exe`.

   > [!NOTE]
   > If the tool is not present, download it from https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool/releases and extract to the specified path.

1. Verify the app source files are present at `C:\LabAssets\Win32-App\`:
   - **Source folder:** `C:\LabAssets\Win32-App\Source\` (contains the app installer and files)
   - **Setup file:** `7z-portable.exe` (or substitute with another small portable app like Notepad++, Paint.NET, etc.)

1. Open **Windows Terminal (Admin)** (right-click Start → Windows Terminal (Admin)).

1. Navigate to the Win32 Content Prep Tool directory:

   ```powershell
   cd "C:\Program Files\IntuneWinAppUtil"
   ```

1. Run the content prep tool to package the app:

   ```powershell
   .\IntuneWinAppUtil.exe -c "C:\LabAssets\Win32-App\Source" -s "7z-portable.exe" -o "C:\LabAssets\Win32-App\Output"
   ```

   - `-c`: Source folder containing the app files
   - `-s`: Setup file (installer executable)
   - `-o`: Output folder for the .intunewin package

1. Wait for the packaging to complete (typically 10–30 seconds).

1. Verify the .intunewin file was created:

   ```powershell
   Test-Path "C:\LabAssets\Win32-App\Output\7z-portable.intunewin"
   ```

   The output should return **True**.

**You have successfully packaged a Win32 app using the Intune Win32 Content Prep Tool.**

---

### Task 2: Add the Win32 app to Intune

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Windows app (Win32)**. Select **Create**.

1. On the **App information** page, select **Select app package file**.

1. In the **App package file** pane, select **Browse** and navigate to `C:\LabAssets\Win32-App\Output\`.

1. Select **7z-portable.intunewin** and select **OK**.

1. On the **App information** page, configure:
   - **Name:** `7-Zip Portable`
   - **Description:** `7-Zip portable file archiver for Windows`
   - **Publisher:** `Igor Pavlov`

1. Select **Next**.

1. On the **Program** page, configure:
   - **Install command:** `7z-portable.exe /S /D="%ProgramFiles%\7-Zip"`
   - **Uninstall command:** `"%ProgramFiles%\7-Zip\Uninstall.exe" /S`
   - **Install behavior:** System
   - **Device restart behavior:** Determine behavior based on return codes

   > [!NOTE]
   > The `/S` switch performs a silent installation (no user prompts). Adjust the command based on your app's installer.

1. Select **Next**.

1. On the **Requirements** page, configure:
   - **Operating system architecture:** 64-bit
   - **Minimum operating system:** Windows 10 1607

1. Select **Next**.

1. On the **Detection rules** page, configure:
   - **Rules format:** Manually configure detection rules

1. Select **Add** under **Detection rules**.

1. In the **Detection rule** pane, configure:
   - **Rule type:** File
   - **Path:** `C:\Program Files\7-Zip`
   - **File or folder:** `7z.exe`
   - **Detection method:** File or folder exists
   - **Associated with a 32-bit app on 64-bit clients:** No

   > [!NOTE]
   > This detection rule checks if `C:\Program Files\7-Zip\7z.exe` exists. If the file is present, Intune considers the app installed.

1. Select **OK**.

1. Select **Next**.

1. On the **Dependencies** page, select **Next** (no dependencies required).

1. On the **Supersedence** page, select **Next** (will configure supersedence in a later task).

1. On the **Scope tags** page, select **+ Select scope tags**, add **Pharmacy** (created in **Lab 01 Exercise 2 Task 6**), select **Select**, then select **Next**.

   > [!NOTE]
   > 7-Zip is the canonical archive tool for the Contoso clinical document workflow (research-data exports, anonymized DICOM bundles). Tagging the deployment with `Pharmacy` keeps it visible to the Pharmacy Helpdesk role (assigned in **Lab 05 Exercise 3**).

1. On the **Assignments** page, under **Required**, select **Add group**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully added a Win32 app with a custom detection rule.**

---

### Task 3: Monitor Win32 app installation

1. On **SEA-DEV1**, force a device sync:
   - **Settings** → **Accounts** → **Access work or school** → **Connected to Contoso** → **Info** → **Sync**

1. Wait 10–15 minutes for the app to install.

   > [!NOTE]
   > Win32 app installation can take longer than Store apps because Intune must download the package, run the installer, and verify the detection rule.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **7-Zip Portable**.

1. Select **Device install status** from the left navigation.

1. Review the installation status for each device:
   - **Installed:** App successfully installed and detection rule passed
   - **In progress:** Installation is running
   - **Failed:** Installation failed (review error code and message)
   - **Not applicable:** Device not targeted by the assignment

1. If installation failed, select the failed device to view detailed error information.

**You have successfully monitored Win32 app installation status.**

---

**Previous:** [← Exercise 1: Deploy Microsoft Store apps](exercise-1.md) | **Next:** [→ Exercise 3: Deploy Microsoft 365 Apps](exercise-3.md)

# Lab 03: Manage applications

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With devices enrolled and managed (Labs 01-02), you now need to deploy applications to users and devices. You'll use multiple deployment methods: Microsoft Store apps (modern apps), Win32 packages (legacy applications), Microsoft 365 Apps (productivity suite), and the Enterprise App Catalog (curated third-party apps). You'll also configure App Protection Policies to secure corporate data on mobile and unenrolled devices.

By the end of this lab, you'll have:
- Deployed a Microsoft Store app
- Packaged and deployed a Win32 application with custom detection rules (tagged with the `Pharmacy` scope tag from Lab 01)
- Deployed Microsoft 365 Apps with update channel configuration
- Added and assigned an app from the Enterprise App Catalog
- Configured app supersedence to automatically upgrade an application (still scoped to the pilot cohort and tagged `Pharmacy`)
- Created an App Protection Policy for mobile devices
- Monitored app deployment status, troubleshot failures, and diagnosed an intentional app-assignment conflict

---

## Lab Duration

**Estimated Time:** 100 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled, groups configured)
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- Global Administrator or Intune Administrator credentials
- **SEA-DEV1** (enrolled device, Megan Bowen signed in)
- **SEA-DEV2** (enrolled device, Joni Sherman signed in)
- Win32 app source files (provided in lab assets at `C:\LabAssets\Win32-App\`)
- **Microsoft Intune Suite trial active** (activated in **Lab 01** prerequisites) — required for Exercise 4 (Enterprise App Catalog)

---

## Exercise 1: Deploy Microsoft Store apps

### Scenario

Microsoft Store apps are modern Windows applications distributed through the Microsoft Store. Intune can deploy Store apps to managed devices without requiring users to access the Store directly.

### Task 1: Add a Microsoft Store app

1. On **SEA-DEV1**, open **Microsoft Edge** and navigate to **https://intune.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Intune admin center**, expand **Apps** and select **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows**, then set **App type** to **Microsoft Store app (new)**. Select **Create**.

   > [!NOTE]
   > The portal flow is a two-step picker: choose Platform first (Windows / iOS/iPadOS / macOS / Android), then the App type list filters to that platform. The "new" Microsoft Store app type uses the Microsoft Store for Business backend and provides better reliability than the legacy connector.

1. On the **App information** page, select **Search the Microsoft Store app (new)**.

1. In the Store search dialog, search for `Microsoft To Do`.

1. Select **Microsoft To Do** from the search results.

1. Select **Select**.

1. On the **App information** page, verify the app details:
   - **Name:** Microsoft To Do
   - **Publisher:** Microsoft Corporation
   - **Description:** (auto-populated from Store)

1. Select **Next**.

1. On the **Assignments** page, under **Required**, select **Add group**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

   > [!NOTE]
   > Assigning as "Required" means the app will install automatically on all devices in the group. "Available" would make it visible in the Company Portal for user-initiated installation.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully added and assigned a Microsoft Store app.**

---

### Task 2: Verify app installation on SEA-DEV1

1. On **SEA-DEV1**, wait 5–10 minutes for the app to install automatically.

   > [!NOTE]
   > Intune checks for new app assignments every 8 hours by default, or when the device syncs. You can force a sync to speed up installation.

1. To force a device sync, open **Settings** (press `Windows + I`).

1. Navigate to **Accounts** → **Access work or school**.

1. Select the **Connected to Contoso** entry (or **Connected to <TenantPrefix>** if the display name differs).

1. Select **Info** → Scroll down and select **Sync**.

1. Wait for the sync to complete (typically 1–2 minutes).

1. After sync, open the **Start menu** and search for `Microsoft To Do`.

1. Verify the app appears in the search results and can be launched.

**You have successfully verified Microsoft Store app installation.**

---

## Exercise 2: Package and deploy a Win32 application

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

## Exercise 3: Deploy Microsoft 365 Apps

### Scenario

Microsoft 365 Apps (formerly Office 365 ProPlus) provide Word, Excel, PowerPoint, Outlook, and other productivity tools. You'll deploy the suite to managed devices with a specific update channel configuration.

### Task 1: Add Microsoft 365 Apps

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Microsoft 365 Apps for Windows 10 and later**. Select **Create**.

1. On the **App suite information** page, configure:
   - **Suite Name:** `Microsoft 365 Apps (Current Channel)`
   - **Suite Description:** `Microsoft 365 Apps with Current Channel updates`

1. Select **Next**.

1. On the **Configure app suite** page, under **Select Office apps**, check the following:
   - **Excel**
   - **Outlook**
   - **PowerPoint**
   - **Word**
   - **OneDrive Desktop** (sync client)

1. Under **App suite settings**, configure:
   - **Update channel:** Current Channel
   - **Remove other versions:** Yes
   - **Version to install:** Latest
   - **Use shared computer activation:** No
   - **Accept the Microsoft Software License Terms on behalf of users:** Yes
   - **Languages:** Select **English (United States)**

   > [!NOTE]
   > Current Channel receives new features as soon as they're released. Monthly Enterprise Channel provides monthly updates with a longer lead time for testing.

1. Select **Next**.

1. On the **Assignments** page, under **Required**, select **Add group**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully configured and assigned Microsoft 365 Apps.**

---

### Task 2: Monitor Microsoft 365 Apps installation

1. On **SEA-DEV1**, force a device sync.

1. Wait 15–30 minutes for Microsoft 365 Apps to download and install.

   > [!NOTE]
   > Microsoft 365 Apps is a large download (~3 GB) and installation can take 20–40 minutes depending on network speed and device performance. For lab purposes, you can proceed to the next exercise and check installation status later.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **Microsoft 365 Apps (Current Channel)**.

1. Select **Device install status** from the left navigation.

1. Review the installation progress for each device.

1. After installation completes, on **SEA-DEV1**, open the **Start menu** and verify the following apps are present:
   - **Excel**
   - **Word**
   - **PowerPoint**
   - **Outlook**

**You have successfully deployed and monitored Microsoft 365 Apps installation.**

---

## Exercise 4: Use the Enterprise App Catalog

### Scenario

The Enterprise App Catalog (part of Microsoft Intune Suite) provides a curated library of third-party applications with pre-configured installers, detection rules, and icons. You'll add an app from the catalog and deploy it to devices.

> [!NOTE]
> The **Enterprise App Catalog** is part of **Microsoft Intune Enterprise Application Management**, a Microsoft Intune Suite capability. The Suite trial was activated in **Lab 01** prerequisites, so this exercise is fully hands-on.

### Task 1: Browse the Enterprise App Catalog

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Enterprise App Catalog app**. Select **Create**.

   > [!NOTE]
   > Enterprise App Catalog app is now generally available (the "(preview)" suffix that appeared earlier has been dropped). It's part of **Enterprise App Management**, an Intune Suite capability — active because of the Suite trial from Lab 01 prerequisites. If this option doesn't appear, the Suite trial may not have fully provisioned yet. Wait 5–10 minutes after activation and refresh — capability tiles can take a few minutes to surface after the trial flips to **Active**.

1. On the **Select app** page, browse the available apps in the catalog.

   The catalog includes popular enterprise apps such as:
   - **Google Chrome**
   - **Mozilla Firefox**
   - **Zoom**
   - **Adobe Acrobat Reader**
   - **VLC Media Player**
   - **Notepad++**

1. Search for or select **Google Chrome** from the list.

1. Select **Select**.

**You have successfully browsed the Enterprise App Catalog and selected an app.**

---

### Task 2: Configure and assign the app

1. On the **App information** page, review the pre-populated details:
   - **Name:** Google Chrome
   - **Description:** (auto-populated)
   - **Publisher:** Google
   - **Installation command:** (pre-configured)
   - **Detection rule:** (pre-configured)

1. Select **Next**.

1. On the **Requirements** page, review the pre-configured requirements and select **Next**.

1. On the **Detection rules** page, review the pre-configured detection rule:
   - **Rule type:** File or registry-based detection
   - **Detection logic:** Checks for Chrome installation path

1. Select **Next**.

1. On the **Assignments** page, under **Available for enrolled devices**, select **Add group**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

   > [!NOTE]
   > Assigning as "Available" makes the app visible in the Company Portal app, allowing users to install it on-demand. This is useful for optional software.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully added and assigned an app from the Enterprise App Catalog.**

---

### Task 3: Verify app availability in Company Portal

1. On **SEA-DEV1**, open the **Start menu** and search for `Company Portal`.

1. Launch the **Company Portal** app.

1. Sign in as **MeganB@<TenantPrefix>.OnMicrosoft.com** (if not already signed in).

1. Navigate to the **Apps** section.

1. Verify **Google Chrome** appears in the available apps list.

1. Select **Install** to install the app.

1. Wait for installation to complete.

1. Open the **Start menu** and verify **Google Chrome** is present.

**You have successfully installed an app from the Company Portal.**

---

## Exercise 5: Configure app supersedence

### Scenario

App supersedence allows you to automatically upgrade or replace applications. When a user has an older version installed, Intune automatically uninstalls it and installs the newer version.

### Task 1: Create a second version of the Win32 app

For this task, you'll simulate a new version by creating a second Win32 app entry.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Windows app (Win32)**. Select **Create**.

1. On the **App information** page, select **Select app package file** and upload the same **7z-portable.intunewin** file (from `C:\LabAssets\Win32-App\Output\`).

1. On the **App information** page, configure:
   - **Name:** `7-Zip Portable v2.0`
   - **Description:** `Updated version of 7-Zip portable`
   - **Publisher:** `Igor Pavlov`

1. Select **Next**.

1. On the **Program** page, use the same install/uninstall commands as the original app.

1. Select **Next**.

1. On the **Requirements** page, use the same settings as before.

1. Select **Next**.

1. On the **Detection rules** page, configure the same file-based detection rule:
   - **Path:** `C:\Program Files\7-Zip`
   - **File:** `7z.exe`
   - **Detection method:** File or folder exists

1. Select **Next**.

1. On the **Dependencies** page, select **Next**.

1. On the **Supersedence** page, select **Add** under **Supersedence relationships**.

1. In the **Add supersedence** pane, search for and select **7-Zip Portable** (the original app).

1. Under **Supersedence type**, select **Replace**.

   > [!NOTE]
   > "Replace" uninstalls the old app before installing the new one. "Update" installs the new app and leaves the old app installed (useful for side-by-side versions).

1. Select **OK**.

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**. The supersedence relationship inherits the same scope as the original app, keeping Pharmacy delegation consistent across both versions.

1. On the **Assignments** page, under **Required**, select **Add group**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully configured app supersedence to automatically upgrade from v1 to v2.**

---

### Task 2: Verify app supersedence behavior

1. On **SEA-DEV1**, force a device sync.

1. Wait 10–15 minutes for Intune to detect the supersedence relationship and upgrade the app.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **7-Zip Portable v2.0**.

1. Select **Device install status** and verify SEA-DEV1 shows **Installed**.

1. Navigate to **7-Zip Portable** (the original app) and select **Device install status**.

1. Verify the status shows **Superseded** or **Uninstalled**.

**You have successfully verified app supersedence automatically replaced the old app with the new version.**

---

## Exercise 6: Create an App Protection Policy

### Scenario

App Protection Policies (APP) secure corporate data on mobile devices and BYOD (bring-your-own-device) scenarios without requiring full device enrollment. You'll create an APP for iOS/Android that prevents copy/paste, requires a PIN, and enforces conditional access.

### Task 1: Create an iOS App Protection Policy

1. In the **Microsoft Intune admin center**, expand **Apps** and select **App protection policies**.

1. Select **Create policy** → **iOS/iPadOS**.

1. On the **Basics** page, configure:
   - **Name:** `APP - iOS Data Protection`
   - **Description:** `Protects corporate data in Microsoft apps on iOS devices`

1. Select **Next**.

1. On the **Apps** page, select **Select public apps**.

1. In the app picker, search for and select:
   - **Microsoft Outlook**
   - **Microsoft Teams**
   - **Microsoft Word**
   - **Microsoft Excel**
   - **Microsoft PowerPoint**
   - **OneDrive**

1. Select **OK**.

1. Select **Next**.

1. On the **Data protection** page, configure:
   - **Data transfer:**
     - **Send org data to other apps:** Policy managed apps
     - **Receive data from other apps:** Policy managed apps
     - **Save copies of org data:** Block
     - **Allow user to save copies to selected services:** OneDrive for Business, SharePoint
     - **Restrict cut, copy, and paste between apps:** Policy managed apps with paste in
   - **Encryption:**
     - **Encrypt org data:** Require
   - **Functionality:**
     - **Sync app with native contacts app:** Block
     - **Printing org data:** Block
     - **Restrict web content transfer with other apps:** Microsoft Edge

1. Select **Next**.

1. On the **Access requirements** page, configure:
   - **PIN for access:** Require
   - **PIN type:** Numeric
   - **Select Minimum PIN length:** 6
   - **Biometric instead of PIN for access:** Require
   - **Work or school account credentials for access:** Require
   - **Recheck the access requirements after (minutes of inactivity):** 30

1. Select **Next**.

1. On the **Conditional launch** page, review the default conditions:
   - **Max PIN attempts:** 5 (Action: Reset PIN)
   - **Offline grace period:** 720 minutes (Action: Block access)
   - **Jailbroken/rooted devices:** (Action: Block access)
   - **Min OS version:** (Optional—define minimum iOS version)

1. Select **Next**.

1. On the **Assignments** page, under **Include**, select **Add groups**.

1. Search for and select **All users**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created an iOS App Protection Policy.**

---

### Task 2: Create an Android App Protection Policy

1. On the **App protection policies** page, select **Create policy** → **Android**.

1. On the **Basics** page, configure:
   - **Name:** `APP - Android Data Protection`
   - **Description:** `Protects corporate data in Microsoft apps on Android devices`

1. Select **Next**.

1. On the **Apps** page, select **Select public apps**.

1. Search for and select the same Microsoft apps as the iOS policy (Outlook, Teams, Word, Excel, PowerPoint, OneDrive).

1. Select **OK** and select **Next**.

1. On the **Data protection** page, configure the same settings as the iOS policy:
   - **Send org data to other apps:** Policy managed apps
   - **Receive data from other apps:** Policy managed apps
   - **Save copies of org data:** Block
   - **Restrict cut, copy, and paste:** Policy managed apps
   - **Encrypt org data:** Require
   - **Restrict web content transfer:** Microsoft Edge

1. Select **Next**.

1. On the **Access requirements** page, configure:
   - **PIN for access:** Require
   - **PIN type:** Passcode
   - **Minimum PIN length:** 6
   - **Biometric instead of PIN:** Require
   - **Work or school account credentials:** Require
   - **Recheck access requirements:** 30 minutes

1. Select **Next**.

1. On the **Conditional launch** page, review the default conditions and select **Next**.

1. On the **Assignments** page, under **Include**, select **Add groups** and select **All users**.

1. Select **Next** → **Create**.

**You have successfully created an Android App Protection Policy.**

---

### Task 3: Understand App Protection Policy enforcement

App Protection Policies are enforced at the application level, not the device level. Here's how they work:

1. **User installs a managed app** (e.g., Outlook) from the App Store or Google Play.

1. **User signs in with work account** (`user@<TenantPrefix>.onmicrosoft.com`).

1. **Intune recognizes the managed identity** and applies the App Protection Policy.

1. **User is prompted to set a PIN** (6 digits or more).

1. **App Protection controls are enforced**:
   - User cannot copy data from Outlook to personal apps (e.g., Gmail)
   - User cannot save attachments outside OneDrive or SharePoint
   - App data is encrypted at rest
   - App is wiped if device is jailbroken/rooted

1. **Conditional Access integration** (optional): If combined with a Conditional Access policy, non-compliant users are blocked from signing in.

> [!NOTE]
> App Protection Policies do not require device enrollment. They protect corporate data on BYOD devices without giving IT full control of the device.

**You now understand how App Protection Policies enforce data protection on mobile devices.**

---

## Exercise 7: Monitor app deployment and troubleshoot failures

### Scenario

You'll use the Intune admin center to monitor app deployment across all devices, identify failed installations, and troubleshoot common issues.

### Task 1: Review the App overview dashboard

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **Overview**.

1. Review the **App protection status** dashboard:
   - **iOS:** Number of users with protected apps
   - **Android:** Number of users with protected apps
   - **Windows:** (App Protection Policies not applicable to Windows)

1. Review the **App install status** dashboard:
   - **Failed:** Apps that failed to install
   - **In progress:** Apps currently installing
   - **Installed:** Successfully installed apps
   - **Not installed:** Apps not yet evaluated

1. Select **Failed** to view a list of failed app installations.

**You have successfully reviewed the App overview dashboard.**

---

### Task 2: Investigate a failed app installation

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select an app that shows installation failures (e.g., **7-Zip Portable**).

1. Select **Device install status** from the left navigation.

1. Locate a device with status **Failed** and select it.

1. Review the error details:
   - **Error code:** Numeric code (e.g., 0x80070005 = Access Denied)
   - **Error message:** Description of the failure
   - **Last modified:** Timestamp of last installation attempt

1. Common failure reasons and resolutions:
   - **0x80070005 (Access Denied):** App installer requires elevation—set install behavior to "System" instead of "User"
   - **Detection rule not met:** App installed successfully but detection rule failed—verify detection rule logic
   - **Download failed:** Device has no internet connectivity or cannot reach Intune endpoints
   - **Disk space insufficient:** Device does not have enough free space for installation

**You have successfully investigated a failed app installation.**

---

### Task 3: Export app install status to CSV

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **Monitor** → **App install status**.

1. Select an app from the list (e.g., **Microsoft 365 Apps (Current Channel)**).

1. On the **Device install status** page, select **Export** from the top toolbar.

1. Wait for the export to complete (typically 1–2 minutes).

1. Select **Download** to save the CSV file.

1. Open the CSV in **Excel** and review the columns:
   - **Device name**
   - **User name**
   - **Platform**
   - **Status** (Installed, Failed, In Progress)
   - **Last check-in**

**You have successfully exported app installation data for reporting.**

---

### Task 4: Diagnose an intentional app-assignment conflict

App assignment intents can collide just like configuration profiles can. The classic example is one admin marking an app **Required** for a broad group while another admin marks the same app **Uninstall** for an overlapping group. Intune flags this in the **App install status** view as a conflict, and neither install nor uninstall completes cleanly. You'll deliberately create this situation, find it, and resolve it.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **7-Zip Portable** (the v1 app you deployed in Exercise 2 — *not* the v2.0).

1. Select **Properties** from the left navigation, then in the **Assignments** section select **Edit**.

1. Under **Uninstall**, select **Add group**.

1. Search for and select **sg-Intune-Pilot-Users** (the same pilot cohort that already has **7-Zip Portable v2.0** assigned as **Required** via supersedence). Select **Select**.

1. Select **Review + save** → **Save**.

   > [!IMPORTANT]
   > You've now told Intune: "Uninstall **7-Zip Portable** from pilot users" AND (via the v2.0 supersedence relationship) "Install **7-Zip Portable v2.0** on pilot users, replacing v1." These two intents partially overlap and produce a conflict.

1. Trigger a sync on **SEA-DEV1** (Settings → Accounts → Access work or school → Sync). Wait 5–10 minutes for Intune to evaluate.

1. In **Apps** → **All apps** → **7-Zip Portable**, select **Device install status**. Locate SEA-DEV1 (or any pilot device) and observe the status — you should see **Conflict** or an explicit failure with an error message indicating multiple intents.

   > [!NOTE]
   > Intune surfaces app conflicts as either **Conflict** in the device install status column, or as a specific error in the per-device drill-in. **App install status** is the single most useful surface for diagnosing app assignment fights, the same way **Per-setting status** is for configuration profile conflicts (Lab 02 Exercise 6).

1. Resolve the conflict. The supersedence path is the correct one (v1 → v2.0 is automatic), so remove the redundant Uninstall assignment on v1:
   - On **7-Zip Portable** → **Properties** → **Assignments** → **Edit**.
   - Under **Uninstall**, hover over **sg-Intune-Pilot-Users** and select the **Remove** icon (trash can).
   - Select **Review + save** → **Save**.

1. Trigger another sync on SEA-DEV1, wait 5–10 minutes, and re-check **Device install status** on **7-Zip Portable v2.0**. Confirm SEA-DEV1 shows **Installed** with no remaining conflict on the v1 app.

   > [!NOTE]
   > In production, the upper-intermediate move is to set up **assignment audits** — review the **Audit logs** for app-assignment edits when you find a conflict to see who added the conflicting intent and when. You'll inspect audit logs in **Lab 05 Exercise 4**.

**You have successfully diagnosed and resolved an app-assignment conflict.**

---

## Lab Summary

Congratulations! You've completed Lab 03: Manage applications.

In this lab, you accomplished the following:

**Exercise 1: Deploy Microsoft Store apps**
- Added a Microsoft Store app (Microsoft To Do) to Intune
- Assigned the app as Required to automatically install on devices
- Verified installation on a managed device

**Exercise 2: Package and deploy a Win32 application**
- Packaged a Win32 app using the Intune Win32 Content Prep Tool
- Created a custom file-based detection rule
- Tagged the deployment with the `Pharmacy` scope tag for delegated administration
- Deployed the app to pilot users and monitored installation status

**Exercise 3: Deploy Microsoft 365 Apps**
- Configured Microsoft 365 Apps with Current Channel updates
- Assigned the suite to all Windows devices
- Monitored the large app deployment process

**Exercise 4: Use the Enterprise App Catalog**
- Browsed the Enterprise App Catalog (Intune Suite feature)
- Added Google Chrome with pre-configured settings and detection rules
- Deployed the app as Available in the Company Portal

**Exercise 5: Configure app supersedence**
- Created a newer version of an app (tagged `Pharmacy`)
- Configured a supersedence relationship to automatically replace the old version
- Verified automatic upgrade behavior on devices

**Exercise 6: Create an App Protection Policy**
- Created iOS and Android App Protection Policies
- Configured data protection controls (copy/paste restrictions, encryption, PIN requirements)
- Understood how APP enforces data protection without device enrollment

**Exercise 7: Monitor app deployment and troubleshoot failures**
- Reviewed the App overview dashboard
- Investigated failed app installations and interpreted error codes
- Exported app install status data to CSV for reporting
- Diagnosed and resolved an intentional Required vs. Uninstall app-assignment conflict

**Key Takeaways:**
- Microsoft Store apps provide modern, lightweight application deployment
- Win32 apps require packaging with the Content Prep Tool and custom detection rules
- Microsoft 365 Apps deployment includes update channel configuration for phased rollouts
- Enterprise App Catalog (Intune Suite) simplifies third-party app deployment with pre-configured installers
- App supersedence automates application upgrades without manual uninstall/reinstall
- App Protection Policies secure corporate data on mobile/BYOD devices without full enrollment
- Scope tags carry through the app surface just like configuration and compliance — tag clinical/regulated apps at create time so delegated admins (Pharmacy Helpdesk, Lab 05) can manage them
- App assignment conflicts (Required vs. Uninstall on overlapping groups) surface in **App install status**; resolve by removing the redundant intent and using audit logs (Lab 05) to find who introduced it
- Intune provides comprehensive monitoring and troubleshooting for app deployment

**Next Steps:**
In Lab 04, you'll protect devices using Microsoft Defender for Endpoint integration, endpoint security policies, BitLocker encryption, Microsoft Tunnel Gateway, and Microsoft Cloud PKI.

---

**END OF LAB**

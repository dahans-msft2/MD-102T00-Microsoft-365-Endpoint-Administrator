# Lab 03, Exercise 5: Configure app supersedence

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

**Previous:** [← Exercise 4: Use the Enterprise App Catalog](exercise-4.md) | **Next:** [→ Exercise 6: Create an App Protection Policy](exercise-6.md)

# Lab 06, Exercise 2: Deploy Remote Help

### Scenario

Remote Help provides secure, audited remote assistance for enrolled devices. IT administrators can remotely view and control devices to troubleshoot issues. You'll enable Remote Help, assign licenses, deploy the app, and initiate a remote session.

### Task 1: Enable Remote Help

1. In the **Microsoft Intune admin center**, expand **Tenant administration** and select **Remote Help**.

1. On the **Remote Help** page, select the **Settings** tab.

1. Configure:
   - **Enable Remote Help:** On
   - **Require organization consent:** On (recommended for compliance)
   - **Disable chat:** Off (allow chat during sessions)
   - **Allow session logs:** On (audit trail for security)

1. Select **Save**.

**You have successfully enabled Remote Help.**

---

### Task 2: Assign Remote Help licenses

Remote Help requires Microsoft Intune Suite licensing.

1. In **Microsoft Edge**, navigate to **https://admin.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft 365 admin center**, expand **Users** and select **Active users**.

1. Select **Megan Bowen** (helper role—help desk or admin).

1. Select the **Licenses and apps** tab.

1. Verify **Microsoft Intune Suite** is assigned (or assign it if not present).

1. Repeat for **Joni Sherman** (sharer role—end user receiving help).

   > [!NOTE]
   > Both the helper (IT admin) and sharer (end user) require Remote Help licensing.

**You have successfully assigned Remote Help licenses.**

---

### Task 3: Deploy the Remote Help app

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select **+ Create** from the top toolbar.

1. In the **Select app type** pane, set **Platform** to **Windows** and **App type** to **Windows app (Win32)**. Select **Create**.

   > [!NOTE]
   > Remote Help can also be deployed as a Microsoft Store app or pre-installed via OEM/image. For lab purposes, we'll deploy as a Win32 app.

1. On the **App information** page, select **Select app package file**.

1. Browse to the Remote Help installer (provided by your lab environment or download from **https://aka.ms/downloadremotehelp**).

1. Upload the `.intunewin` package (if pre-packaged) or the `.msi` installer.

1. On the **App information** page, enter:
   - **Name:** `Remote Help`
   - **Description:** `Secure remote assistance app for enrolled devices`
   - **Publisher:** Microsoft Corporation

1. Select **Next**.

1. On the **Program** page, configure:
   - **Install command:** `msiexec /i RemoteHelp.msi /quiet`
   - **Uninstall command:** `msiexec /x {GUID} /quiet` (replace {GUID} with product code)
   - **Install behavior:** System

1. Select **Next** → Configure detection rules (file-based: `C:\Program Files\Remote Help\RemoteHelp.exe`) → **Next**.

1. On the **Assignments** page, assign as **Required** to **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

**You have successfully deployed the Remote Help app.**

---

### Task 4: Initiate a Remote Help session

1. On **CL1** (helper device—Megan Bowen), wait for Remote Help to install.

1. After installation, launch **Remote Help** from the Start menu.

1. Sign in as **MeganB@<TenantPrefix>.OnMicrosoft.com** (helper role).

1. In the Remote Help app, select **Get help** → **Request help code**.

1. A 6-digit help code is displayed (e.g., `123-456`).

1. On **CL2** (sharer device—Joni Sherman), sign in as **JoniS@<TenantPrefix>.OnMicrosoft.com**.

1. Launch **Remote Help** from the Start menu.

1. Sign in as **JoniS@<TenantPrefix>.OnMicrosoft.com** (sharer role).

1. In the Remote Help app, select **Get help** → **Enter help code**.

1. Enter the 6-digit code from CL1.

1. On **CL2**, a consent prompt appears asking Joni to approve the remote session.

1. Select **Allow** to grant Megan remote access.

1. On **CL1**, Megan can now view Joni's desktop.

   > [!NOTE]
   > By default, Remote Help provides view-only access. Megan can request full control by selecting **Request control** in the Remote Help toolbar. Joni must approve the full control request.

1. Test remote actions:
   - Megan can use chat to communicate with Joni
   - Megan can request control to interact with applications
   - Megan can end the session at any time

1. After testing, select **End session** to disconnect.

**You have successfully initiated and tested a Remote Help session.**

---

### Task 5: Review Remote Help session logs

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Remote Help**.

   > [!NOTE]
   > The page opens on the **Monitor** tab by default. The three tabs are **Monitor** (current sessions, average session time, total sessions), **Settings** (where you enabled Remote Help in Task 1), and **Remote Help sessions** (per-session audit log).

1. Select the **Remote Help sessions** tab.

1. Review the session log:
   - **Helper:** Megan Bowen
   - **Sharer:** Joni Sherman
   - **Start time**
   - **End time**
   - **Duration**
   - **Session ID** (for audit purposes)

   > [!NOTE]
   > Session logs provide an audit trail for compliance and security reviews. All actions during the session are logged.

**You have successfully reviewed Remote Help session logs.**

---

### Task 6: Demonstrate Pharmacy Helpdesk Remote Help scope

The `Pharmacy Helpdesk` role assigned to **Lee Gu** in **Lab 05 Exercise 3** grants Read + remote-task permissions (including **Sync devices**, **Restart now**, **Collect diagnostics**) scoped to objects tagged **Pharmacy**. Remote Help inherits the same scope: Lee Gu can initiate a Remote Help session against Pharmacy-tagged devices, but not against devices outside her scope. This is the upper-intermediate "delegated remote-assistance" pattern.

1. Open a new **InPrivate** or **Incognito** browser window. Navigate to **https://intune.microsoft.com**.

1. Sign in as **LeeG@<TenantPrefix>.OnMicrosoft.com** (Lee Gu, the Pharmacy Helpdesk delegated admin).

1. In the Intune admin center as Lee Gu, navigate to **Devices** → **All devices**.

   > [!NOTE]
   > Lee Gu sees only devices that are in `dyn-Windows-Devices` AND are tagged with the Pharmacy scope tag (per the role assignment configured in Lab 05 Exercise 3 Task 3). Depending on which devices you tagged with Pharmacy when you created them, this list may be smaller than what your Global Admin sees.

1. Select a Pharmacy-tagged device (e.g., **CL1** if you tagged it).

1. In the device blade, locate the **New remote assistance session** option (toolbar or device actions menu).

1. Confirm Lee Gu can initiate the Remote Help session. The session opens in the Remote Help client — same flow as Task 4 above.

1. End the session.

1. Now try to select a device that's NOT Pharmacy-tagged (Lee Gu won't see one in her list, so this is a thought experiment): if such a device existed in her view, she would lack the **New remote assistance session** option because the role's scope tag intersection excludes it.

   > [!NOTE]
   > **The takeaway.** Scope tags on a custom role aren't just for the Configuration / Compliance / Apps surfaces — they apply to **remote-task operations** like Sync, Restart, and Remote Help. That's what makes scope-tag-based delegation actually safe: the Pharmacy Helpdesk physically cannot help (or accidentally disrupt) devices outside her domain.

1. Sign out of the InPrivate window.

**You have successfully demonstrated end-to-end that the Pharmacy Helpdesk delegated role, created in Lab 01 and assigned in Lab 05, scopes Remote Help operations exactly as designed. Thread A (custom RBAC + scope tag delegation) is now complete across all six labs.**

---

**Previous:** [← Exercise 1: Configure Endpoint Privilege Management (EPM)](exercise-1.md) | **Next:** [→ Exercise 3: Use Advanced Analytics and Device Query](exercise-3.md)

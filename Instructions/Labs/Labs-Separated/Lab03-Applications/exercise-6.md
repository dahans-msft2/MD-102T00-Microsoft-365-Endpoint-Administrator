# Lab 03, Exercise 6: Create an App Protection Policy

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

**Previous:** [← Exercise 5: Configure app supersedence](exercise-5.md) | **Next:** [→ Exercise 7: Monitor app deployment and troubleshoot failures](exercise-7.md)

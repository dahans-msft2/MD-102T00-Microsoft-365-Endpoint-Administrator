# Lab 01, Exercise 3: Configure device registration and settings

### Scenario

Before devices can enroll in Intune, you need to configure device registration settings in Microsoft Entra ID, including who can register devices, device limits, and additional local administrator accounts. You'll also enable Microsoft Entra LAPS for local administrator password management.

### Task 1: Configure device join settings

1. In the **Microsoft Entra admin center**, in the left navigation under **Entra ID**, select **Devices**, then select **Overview**.

1. Select **Device settings** from the left navigation.

1. On the **Device settings** page, under **Microsoft Entra join and registration settings**, configure the following:
   - **Users may join devices to Microsoft Entra:** Select **All** *(options: All / Selected / None)*
   - **Users may register their devices with Microsoft Entra:** Should already show **All**, and the control is **greyed out/non-interactive** — this is expected, not a bug
   - **Require Multifactor Authentication to register or join devices with Microsoft Entra:** Select **No**
   - **Maximum number of devices per user:** `50`

   > [!NOTE]
   > **"Users may register their devices" is greyed out at All** — expected, not a bug. Intune/MDM auto-enrollment is already active in this tenant, and registration is required for MDM enrollment, so Entra locks the toggle. Nothing to configure here.
   >   > You'll see a yellow recommendation banner advising you to require MFA via Conditional Access rather than this toggle. For this lab, leave the MFA toggle set to **No** — Conditional Access enforcement is covered in Lab 04. In a production environment, you would restrict device registration to specific groups and require MFA. For lab purposes, we're allowing all users to register devices without MFA to simplify enrollment.

1. Select **Save** at the top of the page.

**You have successfully configured device join settings.**

---

### Task 2: Configure additional local administrators on Microsoft Entra joined devices

By default, the user who performs a Microsoft Entra join becomes a local administrator on the device. You can add additional users or groups to the local administrators group.

1. On the **Device settings** page, scroll down to the **Local administrator settings** section.

   > [!NOTE]
   > Two preview toggles are visible here — **Global administrator role is added as local administrator on the device during Microsoft Entra join (Preview)** and **Registering user is added as local administrator on the device during Microsoft Entra join (Preview)**. Leave both at their default values for this lab.

1. Select the **Manage Additional local administrators on all Microsoft Entra joined devices** link.

1. On the **Device Administrators** page, select **Add assignments**.

1. Search for and select **Allan Deyoung** .
1. Select **Add**.

   > [!NOTE]
   > Allan Deyoung is now added to the local Administrators group on any Microsoft Entra joined device. This is useful for help desk staff who need local admin rights on managed devices. To delegate this via a group instead of individual users, you'd need a dedicated role-assignable group (**Microsoft Entra roles can be assigned to the group: Yes**, set at creation).

**You have successfully configured additional local administrators for Microsoft Entra joined devices.**

---

### Task 3: Enable Microsoft Entra Local Administrator Password Solution (LAPS)

Microsoft Entra LAPS automatically manages and rotates local administrator passwords on Microsoft Entra joined devices.

> [!IMPORTANT]
> Detailed LAPS policy configuration (password complexity, length, age, and managed account name) has moved out of the Entra admin center and into Microsoft Intune as an endpoint security policy. The Entra setting is now a single on/off toggle that enables the LAPS feature for the tenant; the password policy itself is configured in Intune.

**Part A — Enable LAPS at the tenant level (Entra admin center):**

1. In the **Microsoft Entra admin center**, in the left navigation under **Entra ID**, select **Devices**, then select **Device settings**.

1. Scroll down to the **Local administrator settings** section.

1. Set **Enable Microsoft Entra Local Administrator Password Solution (LAPS)** to **Yes**.

1. Select **Save** at the top of the page.

**Part B — Configure the LAPS password policy (Intune admin center):**

1. In the browser, navigate to **https://intune.microsoft.com**.

1. In the **Microsoft Intune admin center**, expand **Endpoint security** in the left navigation and select **Account protection**.

1. Select **+ Create Policy**.

1. In the **Create a profile** pane, configure the following:
   - **Platform:** Windows
   - **Profile:** Local admin password solution (Windows LAPS)

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Contoso LAPS Policy`
   - **Description:** `Manages and rotates the local Administrator password on Microsoft Entra joined devices`

1. Select **Next**.

1. On the **Configuration settings** page, configure the following:
   - **Backup Directory:** Backup the password to Microsoft Entra ID
   - **Password Age Days:** `30`
   - **Administrator Account Name:** Leave blank (uses the built-in Administrator)
   - **Password Complexity:** Large letters + small letters + numbers + special characters
   - **Password Length:** `14`
   - **Automatic Account Management Enabled:** **No** (leave default)
   - **Post Authentication Actions:** Reset the password and logoff the managed account
   - **Post Authentication Reset Delay:** `24` hours

   > [!NOTE]
   > **Automatic Account Management** (Windows 11 24H2+ only) lets LAPS create/enable a local admin account itself. Leave it **No** here — the lab VMs aren't guaranteed to be on 24H2, and we're already using the existing built-in Administrator account, so it isn't needed. **Post Authentication Actions** options are: *Reset the password* / *Reset the password and logoff the managed account* (the default, and what we're using) / *Reset the password and reboot*.

1. Select **Next**.

1. On the **Scope tags** page, select **Next**.

1. On the **Assignments** page, under **Included groups**, select **Add all devices**.

1. Select **Next**.

1. On the **Review + create** page, review the settings and select **Create**.

   > [!NOTE]
   > Microsoft Entra LAPS automatically rotates the local administrator password every 30 days and stores the password securely in Microsoft Entra ID. Authorized administrators can retrieve the password from the Entra admin center under **Devices** > **Local administrator password recovery**.

**You have successfully enabled Microsoft Entra LAPS and configured the password policy in Intune.**

---

**Previous:** [← Exercise 2: Configure administrative delegation](exercise-2.md) | **Next:** [→ Exercise 4: Configure Windows enrollment policies](exercise-4.md)

# Lab 02, Exercise 1: Create configuration profiles

### Scenario

Configuration profiles allow you to manage device settings at scale. You'll create profiles using the Settings Catalog (granular per-setting control) and built-in templates (pre-configured setting bundles).

### Task 1: Create a Settings Catalog profile

The Settings Catalog provides access to thousands of individual settings across Windows, macOS, iOS, and Android.

1. On **CL1**, open **Microsoft Edge** and navigate to **https://intune.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Intune admin center**, expand **Devices**, then under **Manage devices** select **Configuration**.

   > [!NOTE]
   > The page header reads **Devices | Configuration** and opens to the **Policies** tab by default. The other tabs are **Import ADMX** and **Monitor**.

1. Select **Create** → **New Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Settings catalog

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Config - Power Settings`
   - **Description:** `Manages power plan and display timeout settings for corporate devices`

1. Select **Next**.

1. On the **Configuration settings** page, select **Add settings**.

1. In the settings picker, search for `power`.

1. Expand **Power** and check the following settings:
   - **Unattended Sleep Timeout Plugged In**
   - **Unattended Sleep Timeout On Battery**

1. Select **Close** to return to the configuration settings page.

1. Configure the settings:
   - **Unattended Sleep Timeout Plugged In:** `0` (0 seconds = never sleep unattended)
   - **Unattended Sleep Timeout On Battery:** `1800` (seconds = 30 minutes)

   > [!NOTE]
   > These settings are configured in **seconds**, not minutes — that's how the underlying CSP (`Policy CSP - Power`) is defined, and the Settings Catalog doesn't convert the unit for you. A value of `0` means Windows never automatically sleeps when unattended (useful for kiosk or always-on devices plugged in); a nonzero value conserves battery when unplugged.

1. Select **Next**.

1. On the **Scope tags** page, select **+ Select scope tags**, add the **Pharmacy** scope tag (created in **Lab 01 Exercise 2 Task 6**), and select **Select**. Then select **Next**.

   > [!NOTE]
   > Applying scope tags at policy-creation time is what makes delegated administration actually work. The Pharmacy Helpdesk role you created in Lab 01 will be able to see and act on this policy (in **Lab 05 Exercise 3**) because of this tag.
   >
   > **Leave the Default scope tag checked too — don't remove it.** Unlike a role *definition's* own scope tag (Lab 01 Exercise 2 Task 6, where removing Default made sense because that role is Pharmacy-exclusive), this is a general policy assigned to every Windows device in the tenant, not a Pharmacy-only artifact. Adding Pharmacy alongside Default just gives the Pharmacy Helpdesk admin visibility into it too — it doesn't change what the policy actually applies to. This same rule applies everywhere else in the lab series you add the Pharmacy scope tag to a policy, app, or profile.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Applicability Rules** page, select **Next** (no rules needed).

1. On the **Review + create** page, review the settings and select **Create**.

**You have successfully created a Settings Catalog configuration profile.**

---

### Task 2: Create a Device Restrictions profile using a template

Templates provide pre-configured bundles of settings for common scenarios.

1. In the **Microsoft Intune admin center**, on the **Configuration** page, select **Create** → **New Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Templates → **Device restrictions**

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Config - Device Restrictions`
   - **Description:** `Restricts Windows features and user capabilities on corporate devices`

1. Select **Next**.

1. On the **Configuration settings** page, expand **General** and configure:
   - **Screen capture (mobile only):** Block
   - **Copy and paste (mobile only):** Not configured
   - **Manual unenrollment:** Block

1. Expand **Password** and configure:
   - **Password:** Require
   - **Required password type:** Alphanumeric
   - **Password complexity:** Numbers, lowercase, uppercase and special characters required
   - **Minimum password length:** 8
   - **Number of sign-in failures before wiping device:** 10

1. Expand **Microsoft Defender Antivirus** and configure:
   - **Real-time monitoring:** Require
   - **Behavior monitoring:** Require

1. Select **Next**.

1. On the **Scope tags** page, select **+ Select scope tags**, add **Pharmacy**, and select **Select**. Then select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Next**.

1. On the **Applicability Rules** page, select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created a Device Restrictions profile.**

---

### Task 3: Create compound assignment filters (include and exclude modes)

Assignment filters refine policy targeting based on device properties without forcing you to create new groups. Upper-intermediate use of filters means combining multiple properties in one filter (**compound rule**) and using **include vs. exclude** mode on the same policy to layer in and out. You'll create two filters: one compound include filter, and one simple exclude filter that you'll re-use in Task 4.

#### Filter 1 — compound include filter (corporate Microsoft devices, no kiosks)

1. In the **Microsoft Intune admin center**, in the left navigation, select **Tenant administration**, then select **Assignment filters**.

   > [!NOTE]
   > Assignment filters used to live under **Devices**. In the current portal it's a tenant-wide setting under **Tenant administration**.

1. Select **Create** → **Managed devices**.

1. On the **Basics** page, enter:
   - **Name:** `Filter - Microsoft corporate, no kiosks`
   - **Description:** `Compound rule: Microsoft-manufactured corporate devices that are not categorized as Kiosk`
   - **Platform:** Windows 10 and later

1. Select **Next**.

1. On the **Rule syntax** page, switch to the **rule syntax editor** (toggle near the top), then enter:

   ```text
   (device.manufacturer -eq "Microsoft") -and (device.deviceCategory -ne "Kiosk")
   ```

   > [!NOTE]
   > Compound filter rules use the same `-and` / `-or` / parentheses syntax as dynamic group rules. The rule-syntax editor is the only way to author compound filters — the simple property/operator/value picker is single-clause.

1. Select **Next**, skip **Scope Tags**.

1. On the **Review + create** page, select **Create**.

#### Filter 2 — simple exclude filter (CL1)

1. On the **Assignment filters** page, select **Create** → **Managed devices**.

1. On the **Basics** page, enter:
   - **Name:** `Filter - CL1 Exclude`
   - **Description:** `Excludes device CL1 from policy assignments`
   - **Platform:** Windows 10 and later

1. Select **Next**.

1. On the **Rule syntax** page, configure:
   - **Property:** Device name
   - **Operator:** Equals
   - **Value:** `CL1`

   > [!NOTE]
   > You're targeting CL1 with **Equals** here — the include-vs-exclude decision happens when you **apply** the filter to a policy in Task 4 (you'll choose **Exclude filtered devices from assignment**).

1. Select **Next**, skip **Scope Tags**.

1. On the **Review + create** page, select **Create**.

> [!IMPORTANT]
> **Include vs. exclude is set at apply-time, not on the filter itself.** A filter just defines a set of devices. When you attach a filter to a policy assignment, you pick whether the policy should apply to those devices (**Include**) or skip them (**Exclude**). The same filter can be used in either mode on different policies.

**You have successfully created compound and simple assignment filters.**

---

### Task 4: Apply the assignment filter to a profile

You'll modify the Device Restrictions profile to exclude CL1 using the filter you created in Task 3.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Manage devices** → **Configuration**.

1. Select **Config - Device Restrictions** from the list.

1. Select **Properties** from the left navigation.

1. In the **Assignments** section, select **Edit**.

1. Under the **sg-Intune-Pilot-Users** group assignment, expand the **Filter** dropdown and select **Exclude filtered devices from assignment**.

1. Under **Select filter**, choose **Filter - CL1 Exclude**.

1. Select **Review + save** → **Save**.

   > [!NOTE]
   > The Device Restrictions profile will now apply to all devices in `sg-Intune-Pilot-Users` **except** CL1. This is the include-vs-exclude pattern from Task 3: the filter defines "CL1", and the apply-time mode (**Exclude**) flips its meaning. The same `Filter - CL1 Exclude` could be used in **Include** mode on a different policy to *only* target CL1.

**You have successfully applied an assignment filter to a configuration profile.**

---

### Task 5: Create two intentionally conflicting profiles for the pilot cohort

Real Intune environments accumulate overlapping policies as different admins author them over time. Two profiles targeting the same setting on the same group produce a **conflict** that surfaces in the **Per-setting status** view. You'll deliberately set up that situation now so you can diagnose and resolve it in **Exercise 6 Task 2**.

You'll create two Settings Catalog profiles for the pilot cohort that disagree on a single setting: **Allow camera**. (Why camera? Pharmacy clinical areas have HIPAA-driven restrictions on cameras near patient records, but the broader pilot cohort has admin assistants who need cameras for Teams meetings. Two well-meaning admins might author opposite policies for the same group.)

**Profile 1 — `WIN - Camera - Enabled (Pilot)`**

1. In the **Microsoft Intune admin center**, on the **Configuration** page, select **Create** → **New Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Settings catalog

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `WIN - Camera - Enabled (Pilot)`
   - **Description:** `Allow camera use on pilot devices (Teams meetings)`

1. Select **Next**.

1. On the **Configuration settings** page, select **+ Add settings**.

1. In the settings picker, search for `camera`. Expand **Camera** (or **Devices > Camera**, depending on portal build) and check the **Allow Camera** setting. Close the picker.

1. Set **Allow Camera** to **Allowed**.

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**, search for and select **sg-Intune-Pilot-Users**, then **Select**. Select **Next**.

1. On the **Review + create** page, select **Create**.

**Profile 2 — `WIN - Camera - Disabled (Pilot)`** (the conflicting twin)

1. On the **Configuration** page, select **Create** → **New Policy**.

1. **Platform:** Windows 10 and later. **Profile type:** Settings catalog. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `WIN - Camera - Disabled (Pilot)`
   - **Description:** `Block camera on pilot devices (Pharmacy clinical areas — HIPAA)`

1. Select **Next**.

1. On the **Configuration settings** page, select **+ Add settings**, search for `camera`, check **Allow Camera**, close the picker.

1. Set **Allow Camera** to **Blocked**.

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**.

1. On the **Assignments** page, assign to **sg-Intune-Pilot-Users** (same group). Select **Next**.

1. On the **Review + create** page, select **Create**.

> [!IMPORTANT]
> You've intentionally created two profiles that **conflict** on the **Allow Camera** setting for the same group (`sg-Intune-Pilot-Users`). Intune does **not** silently merge or pick a winner — it surfaces the conflict in the **Per-setting status** view, and the affected setting on the device shows as **Conflict** with neither value applied. You'll diagnose and resolve this conflict in **Exercise 6 Task 2** — don't fix it now.

**You have successfully created two intentionally conflicting configuration profiles for the pilot cohort.**

---

**Previous:** [← Introduction](introduction.md) | **Next:** [→ Exercise 2: Configure compliance policies](exercise-2.md)

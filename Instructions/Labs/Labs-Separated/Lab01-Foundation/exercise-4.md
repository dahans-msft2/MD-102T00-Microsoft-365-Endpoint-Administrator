# Lab 01, Exercise 4: Configure Windows enrollment policies

### Scenario

In Exercise 5 your colleagues will sign in to **SEA-DEV1** and **SEA-DEV2** and perform a Microsoft Entra join, and in Exercise 6 you'll register **SEA-DEV3** for Windows Autopilot. Before any of that happens, you need to make sure the tenant is configured so the **first-run experience is right**: devices get automatically enrolled in Intune, the user can't start working until critical apps and policies are in place, and you have guardrails on how many devices each user can enroll.

In this exercise you'll:

- Verify that automatic Intune enrollment is configured correctly for new tenants
- Configure the **Enrollment Status Page (ESP)** so devices block until apps and policies are applied — the same gate that makes Autopilot deployments feel polished
- Create a targeted, stricter ESP profile for the pilot group
- Review the default platform restriction policy and create a device limit restriction policy

> [!NOTE]
> **Why automatic MDM enrollment isn't the focus anymore.** In modern, cloud-only Microsoft 365 tenants, **automatic Intune enrollment is on by default** for the All-users scope. The classic "configure MDM user scope" step is now most relevant in **hybrid identity** and **Configuration Manager co-management** scenarios where you need to scope which on-premises-synced users are auto-enrolled. You'll verify the setting in Task 1, then move on to the policies that actually shape the user's first-run experience.

### Task 1: Verify automatic MDM enrollment

1. In the browser, navigate to **https://intune.microsoft.com**.

1. In the **Microsoft Intune admin center**, expand **Devices** in the left navigation.

   > [!NOTE]
   > You may see a one-time **"Devices has changed"** tour banner. Select **Skip** to dismiss it.

1. Under **Device onboarding**, select **Enrollment**.

1. On the **Windows** tab, under **Enrollment options**, select **Automatic Enrollment**.

1. Confirm that **MDM user scope** is set to **All**.

   > [!NOTE]
   > In a brand-new cloud-only tenant, this setting is already configured. If it shows **None**, change it to **All** and select **Save**.

1. Note that **Windows Information Protection (WIP) user scope** is set to **None** and shows the banner: *"Creating new WIP without enrollment policies (WIP-ME) is no longer supported."* Leave this set to **None** — Windows Information Protection is deprecated. You'll use App Protection Policies (MAM) for mobile data protection in Lab 03.

1. Leave the **MDM terms of use URL**, **MDM discovery URL**, and **MDM compliance URL** at their auto-populated defaults.

1. If you made any change, select **Save** at the top of the page. Otherwise, close the **Automatic Enrollment** pane.

**You have verified that automatic MDM enrollment is configured for your tenant.**

---

### Task 2: Configure the Default Enrollment Status Page

The **Enrollment Status Page (ESP)** is shown to users during Windows enrollment (Microsoft Entra join, Autopilot, or device enrollment). It blocks device use until configured apps and policies are applied, so users don't sign in to a half-provisioned device. The **Default** ESP profile targets all users and all devices and ships disabled — you'll enable it to set a baseline for Contoso.

1. In the **Microsoft Intune admin center**, on the **Enrollment** page, on the **Windows** tab, under **Enrollment options**, select **Enrollment Status Page**.

1. On the **Enrollment Status Page** list, select **Default** (assigned to **All users and all devices**).

1. In the **Default** profile pane, select **Manage > Properties** in the left navigation, then select **Edit** next to **Settings**.

1. Configure the following settings:
   - **Show app and profile configuration progress:** Yes
   - **Show an error when installation takes longer than specified number of minutes:** `60`
   - **Show custom message when time limit or error occurs:** Yes
     - **Custom message:** `Contoso device setup is taking longer than expected. Contact the Service Desk at x4040 if this persists.`
   - **Turn on log collection and diagnostics page for end users:** Yes
   - **Only show page to devices provisioned by out-of-box experience (OOBE):** No
   - **Block device use until all apps and profiles are installed:** No

   > [!NOTE]
   > Setting **Block device use until all apps and profiles are installed** to **No** on the Default profile lets standard users sign in quickly while non-blocking policies finish in the background. In Task 3 you'll create a stricter, blocking ESP for the pilot group.

1. Select **Review + save**, then select **Save**.

**You have successfully configured the Default Enrollment Status Page.**

---

### Task 3: Create a blocking ESP profile for the pilot group

Pilot users at Contoso Healthcare receive corporate laptops pre-staged for clinical workflows. You'll create a stricter ESP profile that blocks device use until required apps are installed, and assign it to `sg-Intune-Pilot-Users` so it takes priority over the Default.

1. On the **Enrollment Status Page** list, select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `ESP - Pilot - Blocking`
   - **Description:** `Blocks pilot devices from use until clinical apps and security baseline are installed`

1. Select **Next**.

1. On the **Settings** page, configure:
   - **Show app and profile configuration progress:** Yes
   - **Show an error when installation takes longer than specified number of minutes:** `60`
   - **Show custom message when time limit or error occurs:** Yes
     - **Custom message:** `Contoso pilot device setup is in progress. Contact the Service Desk at x4040 if this persists.`
   - **Turn on log collection and diagnostics page for end users:** Yes
   - **Only show page to devices provisioned by out-of-box experience (OOBE):** No
   - **Block device use until all apps and profiles are installed:** Yes
   - **Allow users to reset device if installation error occurs:** Yes
   - **Allow users to use device if installation error occurs:** No
   - **Block device use until required apps are installed if they are assigned to the user/device:** **All**



1. Select **Next**.

1. On the **Assignments** page, under **Included groups**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**, then select **Select**.

1. Select **Next**, then **Next** again to skip **Scope tags**.

1. On the **Review + create** page, select **Create**.

1. Back on the **Enrollment Status Page** list, confirm `ESP - Pilot - Blocking` appears with **Priority 1** (above **Default**). The first profile a user/device matches wins.

   > [!NOTE]
   > ESP profiles are evaluated by priority. Because `ESP - Pilot - Blocking` is assigned to `sg-Intune-Pilot-Users` and sits at higher priority, pilot users will receive the blocking experience while everyone else falls through to **Default**.

**You have successfully created a targeted Enrollment Status Page profile for pilot users.**

---

### Task 4: Review default enrollment restrictions

Enrollment restrictions control which device platforms can enroll in Intune. Reviewing the defaults helps you understand what the Contoso tenant will accept before SEA-DEV1 and SEA-DEV2 enroll in Exercise 5.

1. In the **Microsoft Intune admin center**, on the **Enrollment** page, on the **Windows** tab, under **Enrollment options**, select **Device platform restriction**.

1. On the **Device platform restriction** page, select the **Default** restriction policy under **Device type restrictions**.

1. In the **Default** restriction policy, review the current settings:
   - **Platform settings:** Review which platforms are allowed (Windows, Android, iOS/iPadOS, macOS)
   - **Platform configurations:** Review specific restrictions (for example, personally owned devices, versions)

   > [!NOTE]
   > The default policy allows all platforms and personally owned devices. In production you might block personally owned Windows devices or restrict specific OS versions, but for the lab leave the defaults in place so SEA-DEV1 and SEA-DEV2 can enroll in Exercise 5.

1. Close the policy details pane without making changes.

**You have successfully reviewed the default enrollment restrictions.**

---

### Task 5: Create a device limit restriction policy

You'll create a policy that limits how many devices each user can enroll. This protects Contoso from license sprawl and stolen-credential abuse.

1. In the **Microsoft Intune admin center**, on the **Enrollment** page (**Devices** > **Device onboarding** > **Enrollment**), on the **Windows** tab, under **Enrollment options**, select **Device limit restriction**.

1. Select **Create restriction**.

1. In the **Create restriction** pane, enter the following:
   - **Name:** `Device Limit - 10 Devices`
   - **Description:** `Limit users to 10 enrolled devices`
   - **Device limit:** `10`

1. Select **Next** and skip **Scope tags**.

1. Under **Assignments**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Create**.

   > [!NOTE]
   > This policy limits all users to 10 enrolled devices. When a user reaches the limit, they must unenroll an existing device before enrolling a new one.

**You have successfully created and assigned a device limit restriction policy.**

---

### Task 6: Block personally owned Android devices

Contoso Healthcare doesn't want personal Android phones enrolling in Intune — only corporate-owned Android Enterprise devices (Samsung Knox / corporate-issued) are permitted, primarily because clinical data handling rules at Contoso require corporate ownership for any device that touches the network. You'll create a **Device platform restriction** that blocks personally owned Android enrollment while leaving corporate Android Enterprise allowed.

1. In the **Microsoft Intune admin center**, on the **Enrollment** page (**Devices** > **Device onboarding** > **Enrollment**), on the **Windows** tab, scroll across to the platform tabs at the top and select the **Android** tab.

   > [!NOTE]
   > Platform restrictions are configured per platform. The **Default** Android platform restriction allows all Android subtypes (personal work profile, corporate-owned work profile, fully managed, dedicated). You'll create a higher-priority custom restriction that blocks the personally owned subtypes.

1. Under **Enrollment options**, select **Device platform restriction**.

1. Select **+ Create restriction** → **Android restriction**.

1. On the **Basics** page, enter:
   - **Name:** `Android - Block personal`
   - **Description:** `Block personally owned Android enrollment; allow corporate-owned Android Enterprise only`

1. Select **Next**.

1. On the **Platform settings** page, you'll see a table with two rows — **Android Enterprise (work profile)** and **Android device administrator** — each with its own **Platform** (Allow/Block) and **Personally owned** (Allow/Block) toggle, plus optional version range and device manufacturer filters. There's no separate row or toggle for "corporate-owned"; ownership is set per-row via **Personally owned**, and leaving **Platform** = Allow while **Personally owned** = Block means that row still allows the type when it's corporate-owned.

   Configure:
   - **Android Enterprise (work profile) → Platform:** **Allow**
   - **Android Enterprise (work profile) → Personally owned:** **Block**
   - **Android device administrator → Platform:** **Block** (legacy DA enrollment is end-of-life — you'll also see a banner noting Intune ended support for Android device administrator management on GMS devices as of December 31, 2024)
   - **Android device administrator → Personally owned:** **Block**

   Leave version range and device manufacturer blank on both rows.

   > [!NOTE]
   > Net effect: personally owned Android Enterprise work-profile (BYOD) devices are blocked; corporate-owned Android Enterprise work-profile devices are allowed (Platform = Allow covers them since only the personal subset is blocked); Android device administrator is blocked outright regardless of ownership.

1. Select **Next**.

1. On the **Scope tags** page, leave the **default** scope tag (this restriction is tenant-wide, not Pharmacy-scoped). Select **Next**.

1. On the **Assignments** page, under **Included groups**, select **sg-Intune-Pilot-Users**. Select **Next**.

1. On the **Review + create** page, select **Create**.

1. On the **Device platform restriction** page, confirm `Android - Block personal` appears in the list with priority **1** (above **Default**). Higher-priority restrictions evaluate first.

   > [!NOTE]
   > In production, you'd typically do this for every platform you don't manage (block personal iOS, block Linux, etc.). The Pharmacy clinical workload at Contoso explicitly forbids personal devices on the network because Contoso can't enforce encryption, jailbreak detection, or app-protection baselines on devices it doesn't own.

**You have successfully blocked personally owned Android device enrollment.**

---

**Previous:** [← Exercise 3: Configure device registration and settings](exercise-3.md) | **Next:** [→ Exercise 5: Enroll Windows devices](exercise-5.md)

# Lab 03, Exercise 4: Use the Enterprise App Catalog

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

1. On **CL1**, open the **Start menu** and search for `Company Portal`.

1. Launch the **Company Portal** app.

1. Sign in as **MeganB@<TenantPrefix>.OnMicrosoft.com** (if not already signed in).

1. Navigate to the **Apps** section.

1. Verify **Google Chrome** appears in the available apps list.

1. Select **Install** to install the app.

1. Wait for installation to complete.

1. Open the **Start menu** and verify **Google Chrome** is present.

**You have successfully installed an app from the Company Portal.**

---

**Previous:** [← Exercise 3: Deploy Microsoft 365 Apps](exercise-3.md) | **Next:** [→ Exercise 5: Configure app supersedence](exercise-5.md)

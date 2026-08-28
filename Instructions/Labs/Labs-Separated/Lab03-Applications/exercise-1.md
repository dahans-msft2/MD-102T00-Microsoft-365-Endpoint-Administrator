# Lab 03, Exercise 1: Deploy Microsoft Store apps

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

**Previous:** [← Introduction](introduction.md) | **Next:** [→ Exercise 2: Package and deploy a Win32 application](exercise-2.md)

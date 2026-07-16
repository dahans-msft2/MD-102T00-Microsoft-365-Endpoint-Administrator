# Lab 03, Exercise 3: Deploy Microsoft 365 Apps

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

**Previous:** [← Exercise 2: Package and deploy a Win32 application](exercise-2.md) | **Next:** [→ Exercise 4: Use the Enterprise App Catalog](exercise-4.md)

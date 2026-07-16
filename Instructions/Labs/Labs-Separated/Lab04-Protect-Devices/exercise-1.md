# Lab 04, Exercise 1: Integrate Microsoft Defender for Endpoint

### Scenario

Microsoft Defender for Endpoint provides EDR (Endpoint Detection and Response), advanced threat protection, and automated investigation capabilities. You'll enable the Intune-to-Defender connector and onboard Windows devices using an EDR configuration policy.

### Task 1: Enable the Microsoft Defender for Endpoint connector

The Intune ↔ Defender for Endpoint connector is a **two-portal** setup: you flip the **Microsoft Intune connection** toggle in the **Microsoft Defender portal** *first*, and only then do the **Connect Windows devices...** toggles in the **Intune** admin center become enabled. If you skip the Defender-portal step, the Intune page shows **Connection status: Unavailable** and every toggle is grayed out.

#### Part A — Establish the connection from the Microsoft Defender portal

1. In **Microsoft Edge**, open a new tab and navigate to **https://security.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Defender portal**, in the left navigation, select **System** → **Settings** → **Endpoints**.

1. Under **General**, select **Advanced features**.

1. Locate the **Microsoft Intune connection** toggle and set it to **On**.

1. Select **Save preferences** at the bottom of the page.

   > [!NOTE]
   > Saving here is what establishes the bidirectional connector. Without this step, the Intune admin center's Defender for Endpoint page is read-only.

#### Part B — Configure the connector from the Intune admin center

1. Switch back to the Intune admin center tab (or open **https://intune.microsoft.com**).

1. In the **Microsoft Intune admin center**, expand **Endpoint security** and (under the **Setup** group) select **Microsoft Defender for Endpoint**.

1. At the top of the page, select **Refresh**. **Connection status** should change from **Unavailable** to **Available** within a minute (it may take 1–2 minutes the first time).

1. On the **Microsoft Defender for Endpoint** page, under **MDM Compliance Policy Settings**, configure:
   - **Connect Windows devices version 10.0.15063 and above to Microsoft Defender for Endpoint:** **On**
   - **Allow Microsoft Defender for Endpoint to enforce Endpoint Security Configurations:** **On**

   > [!NOTE]
   > Enabling the connector allows Intune to send device data to Defender for Endpoint and receive threat intelligence. The second setting allows Defender to enforce security configurations even on devices that aren't yet fully managed by Intune.

1. Select **Save** at the top of the page.

**You have successfully enabled the Microsoft Defender for Endpoint connector.**

---

### Task 2: Create an Endpoint Detection and Response policy

Endpoint Detection and Response policies onboard devices to Defender for Endpoint by deploying the required sensor and configuration.

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Endpoint detection and response**.

1. Select **Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10, Windows 11, and Windows Server
   - **Profile:** Endpoint detection and response

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `EDR - Defender Onboarding`
   - **Description:** `Onboards Windows devices to Microsoft Defender for Endpoint`

1. Select **Next**.

1. On the **Configuration settings** page, configure:
   - **Endpoint detection and response:** Select **Require**
   - **Sample Sharing:** Select **All samples**
   - **Telemetry reporting frequency:** Select **Expedite**

   > [!NOTE]
   > "Expedite" sends telemetry data more frequently for faster threat detection. "All samples" allows Defender to submit suspicious files to Microsoft for analysis.

1. Select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created an EDR policy to onboard devices to Defender for Endpoint.**

---

### Task 3: Verify device onboarding in the Microsoft Defender portal

1. In **Microsoft Edge**, open a new tab and navigate to **https://security.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com** (if not already signed in).

1. In the **Microsoft Defender portal**, expand **Assets** in the left navigation and select **Devices**.

1. Wait 10–15 minutes for SEA-DEV1 and SEA-DEV2 to onboard to Defender for Endpoint.

   > [!NOTE]
   > Device onboarding can take 10–30 minutes after the EDR policy is applied. You can force a device sync in Intune to accelerate the process.

1. After devices appear, select **SEA-DEV1** from the device list.

1. Review the device details:
   - **Risk level:** Low, Medium, High, or Secure
   - **Exposure level:** Based on security configuration score
   - **Health status:** Active, Inactive, or Misconfigured
   - **Onboarding status:** Onboarded

**You have successfully verified device onboarding to Microsoft Defender for Endpoint.**

---

**Previous:** [← Introduction](introduction.md) | **Next:** [→ Exercise 2: Deploy endpoint security policies](exercise-2.md)

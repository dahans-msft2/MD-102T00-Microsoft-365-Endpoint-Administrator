# Lab 01, Exercise 5: Enroll Windows devices

### Scenario

You'll now enroll two Windows 11 devices (CL1 and CL2) into Intune by performing a Microsoft Entra join. This simulates a user-driven enrollment scenario where an employee joins their device to the corporate tenant.

### Task 1: Perform a Microsoft Entra join and enrollment on CL1

1. On **CL1**, sign out of the current session if signed in.

1. At the Windows sign-in screen, select **Other user**.

1. Sign in with the local administrator account:
   - **Username:** `Admin`
   - **Password:**

1. After signing in, open **Settings** (press `Windows + I`).

1. Navigate to **Accounts** → **Access work or school**.

1. Select **Connect**.

1. In the **Set up a work or school account** dialog, select **Join this device to Microsoft Entra ID**.

1. On the **Sign in** page, enter:
   - **Email address:** `MeganB@<TenantPrefix>.OnMicrosoft.com`
   - Select **Next**

1. On the **Enter password** page, enter Megan Bowen's password and select **Sign in**.

1. On the **Make sure this is your organization** page, verify the tenant is **<TenantPrefix>.onmicrosoft.com** and select **Join**.

1. On the **You're all set!** page, select **Done**.

   > [!NOTE]
   > The device is now Microsoft Entra joined and automatically enrolled in Intune. Megan sees the Enrollment Status Page you configured in Exercise 4 while apps and policies are applied. Because Megan isn't in the `sg-Intune-Pilot-Users` group, she gets the non-blocking **Default** profile rather than the stricter **ESP - Pilot - Blocking** profile.

**You have successfully enrolled CL1 in Microsoft Entra and Intune.**

---

### Task 2: Verify CL1 enrollment in the Intune admin center

1. On **CL1**, open **Microsoft Edge** and navigate to **https://intune.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com** (if not already signed in).

1. In the **Microsoft Intune admin center**, expand **Devices** and select **All devices**.

1. Verify that **CL1** appears in the device list with:
   - **Managed by:** Intune
   - **Ownership:** Corporate
   - **Compliance:** (may show "Not evaluated" initially)

1. Select **CL1** from the list to view device details.

1. Review the following tabs:
   - **Overview:** Device name, OS version, last check-in time
   - **Hardware:** Serial number, TPM version, total storage
   - **Discovered apps:** (will populate over time as app inventory syncs)

**You have successfully verified CL1 enrollment in Intune.**

---

### Task 3: Perform a Microsoft Entra join and enrollment on CL2

1. Switch to **CL2**.

1. Sign in with the local administrator account:
   - **Username:** `Admin`
   - **Password:** 

1. Open **Settings** (`Windows + I`).

1. Navigate to **Accounts** → **Access work or school**.

1. Select **Connect**.

1. In the **Set up a work or school account** dialog, select **Join this device to Microsoft Entra ID**.

1. On the **Sign in** page, enter:
   - **Email address:** `JoniS@<TenantPrefix>.OnMicrosoft.com`
   - Select **Next**

1. On the **Enter password** page, enter Joni Sherman's password and select **Sign in**.

1. On the **Make sure this is your organization** page, select **Join**.

1. On the **You're all set!** page, select **Done**.

1. Restart **CL2**.

1. After restart, sign in as:
   - **User:** `JoniS@<TenantPrefix>.OnMicrosoft.com`
   - **Password:** (Joni Sherman's password)

**You have successfully enrolled CL2 in Microsoft Entra and Intune.**

---

### Task 4: Verify both devices are enrolled

1. On **CL1**, in the **Microsoft Intune admin center**, navigate to **Devices** → **All devices**.

1. Verify both **CL1** and **CL2** appear in the device list.

1. Verify the **dyn-Windows-Devices** dynamic group now contains both devices:
   - In the **Microsoft Intune admin center**, navigate to **Groups** → **All groups**.
   - Select **dyn-Windows-Devices**.
   - Select the **Members** tab.
   - Verify CL1 and CL2 are listed (may take 5–10 minutes for dynamic group membership to update).

**You have successfully verified both devices are enrolled and automatically added to the dynamic device group.**

---

**Previous:** [← Exercise 4: Configure Windows enrollment policies](exercise-4.md) | **Next:** [→ Exercise 6: Configure Windows Autopilot](exercise-6.md)

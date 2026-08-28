# Lab 05, Exercise 3: Assign and verify the Pharmacy Helpdesk delegated role end-to-end

### Scenario

In **Lab 01 Exercise 2 Task 6** you created the **`Pharmacy Helpdesk`** custom Intune role and the **`Pharmacy`** scope tag. In **Labs 02–04** you applied the `Pharmacy` scope tag to configuration profiles (Lab 02 Ex 1–2), a compliance policy (Lab 02 Ex 2), the pilot update ring (Lab 02 Ex 4), a Win32 LOB app (Lab 03 Ex 2), the Defender security baseline + Antivirus + ASR (Lab 04 Ex 2), and the BitLocker policy (Lab 04 Ex 3). Now you'll **assign** the role to a delegated administrator (**Lee Gu**, `LeeG@<TenantPrefix>.OnMicrosoft.com`), then **sign in as Lee Gu** and verify end-to-end that the delegated admin sees only Pharmacy-scoped objects — not the whole tenant.

This is the culmination of Thread A across the whole lab series. By the end of this exercise, Lee Gu can manage Pharmacy clinical policies but is invisibly walled off from the rest of the tenant.

### Task 1: Review the `Pharmacy Helpdesk` role and `Pharmacy` scope tag

1. In the **Microsoft Intune admin center**, expand **Tenant administration** and select **Roles**.

1. Select **All roles**. Locate and select **Pharmacy Helpdesk** (created in **Lab 01 Exercise 2 Task 6**).

1. Review the **Permissions** tab. Confirm:
   - **Managed devices:** Read, Set primary user, Update (no Delete, no Wipe)
   - **Remote tasks:** Sync devices, Restart now, Collect diagnostics
   - **Organization:** Read
   - **Roles:** Read
   - **Apps**, **Device compliance policies**, **Device configurations**, **Endpoint protection**: all No

   > [!NOTE]
   > This is the principle-of-least-privilege role you defined in Lab 01: enough to operate devices day-to-day, but no authority to change policy. The Pharmacy Helpdesk can sync a device, force a restart, or collect diagnostics — but can't author or delete the compliance policy that says "BitLocker must be on."

1. Switch to the **Scope (Tags)** tab on the role. Confirm the **Pharmacy** scope tag is listed.

1. Navigate back to **Tenant administration** → **Roles** → **Scope (Tags)** and select **Pharmacy**. Review the tag and note that it's been applied to numerous objects across Labs 02–04 (you'll see object counts).

**You have successfully reviewed the role and scope tag created in Lab 01.**

---

### Task 2: Inventory the Pharmacy-tagged objects across the lab series

Before assigning the role, confirm which objects Lee Gu will gain visibility to. This matches the Graph PowerShell query you ran in **Exercise 1 Task 6**, now in the portal UI.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Manage devices** → **Configuration**.

1. In the policy list, look for the **Scope tags** column (add it via the column picker if it's not visible). Filter or scroll to find policies showing **Pharmacy** in the Scope tags column. Expected: Settings Catalog and Device Restrictions profiles from **Lab 02 Exercise 1**, and the camera disabled profile if you kept it from the conflict resolution.

1. Navigate to **Devices** → **Manage devices** → **Compliance**. Confirm `Compliance - Windows Security Baseline` shows **Pharmacy**.

1. Navigate to **Apps** → **All apps**. Confirm `7-Zip Portable` and `7-Zip Portable v2.0` show **Pharmacy**.

1. Navigate to **Endpoint security** → **Security baselines** and **Antivirus** and **Attack surface reduction** and **Disk encryption**. Confirm `Security Baseline - Defender for Endpoint`, `Antivirus - Defender Configuration`, `ASR - Block (Pilot)`, and the BitLocker policy all show **Pharmacy**.

   > [!NOTE]
   > If any expected object doesn't show **Pharmacy**, go back to that lab's exercise and add the scope tag (it's never too late — scope tags are editable after the fact via the policy **Properties** → **Scope tags** → **Edit**).

**You have successfully inventoried the Pharmacy-tagged objects.**

---

### Task 3: Assign the `Pharmacy Helpdesk` role to Lee Gu

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Roles** → **All roles**.

1. Select **Pharmacy Helpdesk**.

1. Select **Assignments** from the left navigation.

1. Select **Assign**.

1. On the **Basics** page, enter:
   - **Assignment name:** `Pharmacy Helpdesk - Lee Gu`
   - **Description:** `Grants Lee Gu Pharmacy-scoped helpdesk access`

1. Select **Next**.

1. On the **Admin Groups** page, select **Add groups**.

   > [!NOTE]
   > In production you'd assign to a group (e.g., `sg-Pharmacy-Helpdesk-Admins`). For this lab, assigning directly to Lee Gu demonstrates the concept.

1. Search for and select **Lee Gu** (`LeeG@<TenantPrefix>.OnMicrosoft.com`).

1. Select **Select**, then **Next**.

1. On the **Scope (Groups)** page, select **Add groups** and add **dyn-Windows-Devices** (the device target for Pharmacy operations). Select **Select**, then **Next**.

1. On the **Scope (Tags)** page, select **Add scope tags** and choose **Pharmacy**. Select **Select**.

   > [!IMPORTANT]
   > **Scope (Tags) is what makes the role actually scoped.** Without a scope tag on the assignment, Lee Gu would see all objects in the device target group. The scope tag intersects with the role's permissions and the assignment's group target to produce the final visibility — only Pharmacy-tagged objects that are also in dyn-Windows-Devices.

1. Select **Next** → **Create**.

**You have successfully assigned the Pharmacy Helpdesk role to Lee Gu.**

---

### Task 4: Sign in as Lee Gu and verify scoped visibility end-to-end

This is the moment of truth for Thread A. You'll sign in as Lee Gu and confirm that the entire Pharmacy-scoped chain you built across Labs 01–04 is visible — and that nothing else is.

1. Open a new **InPrivate** or **Incognito** browser window.

1. Navigate to **https://intune.microsoft.com**.

1. Sign in as **LeeG@<TenantPrefix>.OnMicrosoft.com**. Use Lee Gu's password (provided in the lab credentials handout).

   > [!NOTE]
   > If Lee Gu hasn't completed MFA setup, you'll be prompted to enroll. Complete the Authenticator setup. The Conditional Access policy from **Lab 02 Exercise 2** in Report-only mode (or enforced after **Lab 04 Exercise 6**) does not block Lee Gu because Lee isn't in `sg-Intune-Pilot-Users`.

1. In the Intune admin center as Lee Gu, navigate to **Devices** → **Manage devices** → **Configuration**.

1. Confirm Lee Gu sees **only** the configuration profiles tagged with **Pharmacy**. Profiles tagged with **Default** only (the Feature update profile, Expedited Quality update policy, ASR Audit Fleet policy) should **not** appear in Lee Gu's view.

1. Navigate to **Devices** → **Manage devices** → **Compliance**. Confirm `Compliance - Windows Security Baseline` is visible; no other compliance policies appear.

1. Navigate to **Apps** → **All apps**. Confirm `7-Zip Portable` and `7-Zip Portable v2.0` are visible; Microsoft 365 Apps, Microsoft To Do, Google Chrome (Default-tagged) do **not** appear.

1. Navigate to **Endpoint security** → **Security baselines** / **Antivirus** / **Attack surface reduction** / **Disk encryption**. Confirm only the Pharmacy-tagged policies are visible.

1. Try to **edit** the `Compliance - Windows Security Baseline` policy:
   - Open the policy.
   - Select **Properties** → attempt to select **Edit** on the Settings section.
   - The Edit button should be grayed out or selecting it returns an authorization error. Lee Gu's role grants **Read** on compliance policies but not **Create/Update/Delete**.

   > [!NOTE]
   > **You've just proven that Lee Gu can see and audit Pharmacy clinical policies, sync devices, and run remote tasks — but cannot edit or delete policy.** That's exactly the upper-intermediate delegation pattern: scoped visibility + bounded write authority. The Pharmacy Helpdesk handles day-to-day device operations; central IT (Jordan Chen, Global Admin) retains policy authorship.

1. Try **Remote Help** preview (you'll exercise this fully in **Lab 06 Exercise 2**): navigate to a Pharmacy-managed device and select **Remote Help**. Lee Gu can initiate; she can't on a device outside her scope.

1. Sign out of the InPrivate window and return to your Jordan Chen admin session.

**You have successfully verified end-to-end that the Pharmacy Helpdesk role + Pharmacy scope tag delegation works exactly as designed across the entire lab series.**

---

**Previous:** [← Exercise 2: Deploy proactive remediations](exercise-2.md) | **Next:** [→ Exercise 4: Monitor audit logs and operational health](exercise-4.md)

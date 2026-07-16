# Lab 01, Exercise 1: Configure users and groups

### Scenario

Contoso has 33 existing users across multiple departments (Marketing, Legal, IT, Sales, HR, Operations, Engineering, etc.). You'll verify these users, create additional test users for lab scenarios, and configure dynamic groups to enable policy targeting by department and device type.

### Task 1: Review existing users and licenses

1. On **CL1**, open **Microsoft Edge**.

1. Navigate to **https://admin.microsoft.com**.

1. Sign in with the **Global Administrator** account:
   - **Username:** `admin@<TenantPrefix>.onmicrosoft.com`
   - **Password:** (provided by your lab environment)

1. In the left navigation, expand **Users** and select **Active users**.

1. Review the list of users. You should see approximately **33 licensed active users** including:
   - Megan Bowen (Marketing Manager)
   - Alex Wilber (Marketing Assistant)
   - Joni Sherman (Paralegal, Legal)
   - Allan Deyoung (IT Admin)
   - Adele Vance (Retail Manager)
   - And others across various departments

   > [!NOTE]
   > The list may also contain unlicensed service accounts (for example, Automate Bot, Conf Room *). To see only the 33 licensed users, change the view filter from **All users** to **Licensed users** above the list. These users are pre-provisioned in the Contoso tenant and have Microsoft 365 E5 licenses assigned. You'll use these existing users for policy targeting throughout the labs.

1. Select **Megan Bowen** from the list.

1. In the Megan Bowen user details pane, select the **Licenses and apps** tab.

1. Verify that the following licenses are assigned:
   - **Microsoft 365 E5 (no Teams)**
   - **Microsoft Teams Enterprise**

1. Close the user details pane.

**You have successfully reviewed the existing users and verified licensing.**

---

### Task 2: Create test users for additional scenarios

While Contoso has 33 existing users, you'll create two additional test users for specific lab scenarios.

1. In the **Microsoft 365 admin center**, on the **Active users** page, select **Add a user** from the top toolbar.

1. In the **Set up the basics** page, enter the following:
   - **First name:** `Lab`
   - **Last name:** `User1`
   - **Display name:** `Lab User1`
   - **Username:** `LabUser1`
   - **Domains:** Select `<TenantPrefix>.onmicrosoft.com`
   - **Password settings:** Uncheck **Automatically create a password**, then enter a strong password, such as the pre-provided `<UserPassword>`, in the password field (or use a secure password of your choice).
   - **Require this user to change their password when they first sign in:** Uncheck this box

1. Select **Next**.

1. On the **Assign product licenses** page, leave both licenses **unchecked** and select **Create user without product license**, then select **Next**.

   > [!NOTE]
   > Lab User1 and Lab User2 don't need a license. They exist only to (1) populate `sg-Intune-Pilot-Users` in Task 3 and (2) receive a scoped Intune Administrator role in Exercise 2 Task 5 — neither use touches a licensed workload (Teams, Exchange, Intune device enrollment). Skipping the license also avoids a real capacity problem: the Contoso lab tenant's trial SKUs are fully consumed by the 33 existing users (**Microsoft 365 E5 (no Teams): 20/20 assigned**, **Microsoft Teams Enterprise: 20/20 assigned**), so there are no seats left to give a new user anyway.

1. On the **Optional settings** page, expand **Profile info**.

1. Set the following:
   - **Job title:** `Test User`
   - **Department:** `IT`

1. Select **Next**.

1. On the **Review and finish** page, review the settings and select **Finish adding**.

1. Select **Close** on the confirmation page.

1. Repeat steps 1–10 to create a second test user:
   - **Name:** Lab User2
   - **Username:** `LabUser2@<TenantPrefix>.onmicrosoft.com`
   - **Password:** `<UserPassword>`
   - **Job title:** Test User
   - **Department:** Engineering
   - **Licenses:** Leave unassigned (same reason as Lab User1)

**You have successfully created two additional test users.**

---

### Task 3: Create an assigned security group

You'll create an assigned (static membership) security group for Intune policy targeting.

> [!NOTE]
> If `sg-Intune-Pilot-Users` already exists from a prior lab run, you'll see a name-collision error when you try to create it. In that case, skip the creation steps and jump to step 9 to add members to the existing group.

1. In the **Microsoft 365 admin center**, in the left navigation, expand **Teams & groups** and select **Active teams & groups**.

1. Select the **Security groups** tab.

1. Select **Add a security group**.

1. On the **Choose a group type** page, select **Security** and select **Next**.

1. On the **Set up the basics** page, enter the following:
   - **Name:** `sg-Intune-Pilot-Users`
   - **Description:** `Pilot users for Intune policy testing`

1. Select **Next**.

1. On the **Review and finish adding group** page, select **Create group**.

1. Select **Close** on the confirmation page.

1. On the **Security groups** tab, select **sg-Intune-Pilot-Users** from the list.

1. In the group details pane, select the **Members** tab.

1. Select **View all and manage members**.

1. Select **Add members**.

1. Search for and select the following users:
   - **Megan Bowen**
   - **Alex Wilber**
   - **Joni Sherman**
   - **Lab User1**
   - **Lab User2**

1. Select **Add (5)**.

1. Close the group details pane.

**You have successfully created an assigned security group with five pilot users.**

---

### Task 4: Create a dynamic user group with a compound rule

Dynamic groups automatically update membership based on user attributes. For the Pharmacy clinical workload, you'll create a dynamic group that uses a **compound rule** — combining two conditions with `-and` — to target users in the Pharmacy department who are also located in the US. Compound rules are the canonical pattern for regulatory and per-region scoping (for example, Contoso Healthcare applies stricter compliance to US clinical workloads).

1. In the browser, navigate to **https://entra.microsoft.com**.

1. In the **Microsoft Entra admin center**, expand **Groups** in the left navigation and select **All groups**.

1. Select **New group** from the top toolbar.

1. In the **New Group** pane, configure the following:
   - **Group type:** Security
   - **Group name:** `dyn-Pharmacy-Users`
   - **Group description:** `Dynamic group for Pharmacy department users located in the US`
   - **Microsoft Entra roles can be assigned to the group:** No
   - **Membership type:** Dynamic User

1. Under **Dynamic user members**, select **Add dynamic query**.

1. In the **Dynamic membership rules** page, switch from the property/operator/value builder to the **Rule syntax editor** (toggle near the top of the rule pane). Compound rules are easier to author and read in the syntax editor.

1. In the **Rule syntax** box, enter the following compound rule exactly:

   ```text
   (user.department -eq "Pharmacy") -and (user.country -eq "US")
   ```

   > [!NOTE]
   > The `-and` operator means **both** conditions must be true for a user to be included. You can also use `-or` to include users matching either condition, and group sub-expressions in parentheses for more complex logic. The Rule syntax editor validates the expression — fix any red underlines before saving. You may also see a preview banner about the `MemberOf` operator; you can dismiss it because this rule uses `-eq`, not `MemberOf`.

1. Select **Save**.

1. Back in the **New Group** pane, select **Create**.

1. After the group is created, select **dyn-Pharmacy-Users** from the groups list.

1. In the group details, verify the **Membership processing status** shows **Update in progress** or **Update complete**.

   > [!NOTE]
   > Dynamic group membership evaluation can take 5–15 minutes. Once complete, the group will contain only users whose `department` attribute equals `Pharmacy` **and** whose `country` attribute equals `US`. If no Contoso sample users currently match both attributes, the group will be empty — that's expected for this lab tenant and doesn't affect later exercises.

1. Select the **Members** tab to view group members.

**You have successfully created a dynamic user group with a compound membership rule.**

---

### Task 5: Create a dynamic device group

You'll create a dynamic group that automatically includes all Windows devices enrolled in Intune.

1. In the **Microsoft Entra admin center**, on the **All groups** page, select **New group**.

1. In the **New Group** pane, configure the following:
   - **Group type:** Security
   - **Group name:** `dyn-Windows-Devices`
   - **Group description:** `Dynamic group for all Windows devices`
   - **Membership type:** Dynamic Device

1. Under **Dynamic device members**, select **Add dynamic query**.

1. In the **Dynamic membership rules** page, configure the following rule:
   - **Property:** deviceOSType
   - **Operator:** Equals
   - **Value:** `Windows`

1. Select **Save**.

1. Back in the **New Group** pane, select **Create**.

   > [!NOTE]
   > This group will automatically populate with Windows devices after they are enrolled in Intune (Exercise 5).

**You have successfully created a dynamic device group for Windows devices.**

---

### Task 6: Create a dynamic device group for Windows Autopilot

You'll create a second dynamic device group, this one for Windows Autopilot registration. You'll use it in **Exercise 6** when you register CL3 for Autopilot and assign it a deployment profile.

1. In the **Microsoft Entra admin center**, on the **All groups** page, select **New group**.

1. In the **New Group** pane, configure the following:
   - **Group type:** Security
   - **Group name:** `dyn-Autopilot-Devices`
   - **Group description:** `Dynamic group for all Windows Autopilot-registered devices`
   - **Membership type:** Dynamic Device

1. Under **Dynamic device members**, select **Add dynamic query**.

1. In the **Dynamic membership rules** page, switch to the **Rule syntax editor** and enter:

   ```text
   (device.devicePhysicalIds -any _ -startsWith "[ZTDId]")
   ```

1. Select **Save**, then back in the **New Group** pane, select **Create**.

   > [!NOTE]
   > `[ZTDId]` (Zero Touch Deployment ID) is set on a device's directory object as soon as its hardware hash is registered with Windows Autopilot — well before the device goes through OOBE. Unlike `dyn-Windows-Devices` (which only matches devices that have already enrolled), this rule lets you target a device the moment it's registered, which is exactly what an Autopilot deployment profile assignment needs.

**You have successfully created a dynamic device group for Windows Autopilot.**

---

**Previous:** [← Introduction](introduction.md) | **Next:** [→ Exercise 2: Configure administrative delegation](exercise-2.md)

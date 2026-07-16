# Lab 01, Exercise 2: Configure administrative delegation

### Scenario

You need to delegate administrative access to team members who will manage different aspects of Intune and device management. You'll use Microsoft Entra ID roles and administrative units to scope permissions appropriately.

### Task 1: Assign the Intune Administrator role

1. In the **Microsoft Entra admin center**, in the left navigation under **Entra ID**, select **Users**, then select **All users**.

1. Search for and select **Allan Deyoung** from the user list.

1. In Allan Deyoung's user details, select **Assigned roles** from the left navigation.

   > [!NOTE]
   > In some Contoso lab tenants, Allan Deyoung is pre-assigned the **Global Administrator** role (visible on the **Active assignments** tab). Adding the Intune Administrator role on top of Global Administrator is functionally redundant — Global Administrator already inherits all Intune permissions. Perform the steps anyway to practice the role-assignment workflow.

1. Select **Add assignments** from the top toolbar.

1. In the **Add assignments** pane, on the **Membership** tab, search for and select **Intune Administrator**.

1. Select the **Setting** tab and configure the following:
   - **Assignment type:** **Active** (not **Eligible** — Eligible would require Allan Deyoung to manually activate the role later through PIM before he could use it; Active grants the permissions immediately)
   - **Permanently eligible / Permanently assigned:** Leave checked
   - **Assignment starts:** Leave the auto-populated current date and time
   - **Assignment ends:** Leave blank (grayed out while the permanent checkbox is checked)

1. In the **Justification** box, enter a reason (for example: `Lab 01 role delegation exercise — assigning Intune Administrator to the IT admin`). PIM requires a justification for every Active assignment, even permanent ones.

1. Select **Add**.

   > [!NOTE]
   > The **Membership**/**Setting** two-tab flow appears because the Contoso lab tenant has Microsoft Entra ID P2 and Privileged Identity Management (PIM) enabled — every directory role assignment goes through PIM by default. **Active** + **Permanently assigned** replicates a classic, always-on role assignment.

   > [!NOTE]
   > The Intune Administrator role grants permissions to manage all aspects of Microsoft Intune, including device configuration, compliance policies, applications, and enrollment settings. This is a less privileged role than Global Administrator.

   > [!NOTE]
   > **This lab uses permanent Active assignments, not PIM's just-in-time (Eligible) model, and that's a deliberate simplification, not the recommended production pattern.** Microsoft's guidance — and this course's own unit content ([Assign Microsoft Entra roles for device management](../Learning%20Path%201%20-%20Prepare%20infrastructure%20for%20devices%20using%20Microsoft%20Intune%20and%20Microsoft%20Entra%20ID/configure-entraid-device-management/includes/04-assign-entra-id-roles-device-management.md)) — recommends **Eligible** assignments for sensitive roles, where the admin activates the role only when needed and the activation expires automatically. We use **Active** here purely so Allan, Joni, and Lab User1 have working permissions for the rest of this lab series without an extra activation step every time. **No lab in this series has learners perform an Eligible-role self-activation** (request access → provide justification → time-boxed activation) — that workflow is covered conceptually in the unit content only. The closest hands-on tie-in is **Lab 06 Exercise 5** (LP6 Unit 05), which has you review PIM activation audit logs, not perform an activation.

**You have successfully assigned the Intune Administrator role to Allan Deyoung.**

---

### Task 2: Assign the Cloud Device Administrator role

1. In the **Microsoft Entra admin center**, under **Entra ID** > **Users** > **All users**, search for and select **Joni Sherman**.

1. In Joni Sherman's user details, select **Assigned roles**.

1. Select **Add assignments**.

1. In the **Add assignments** pane, on the **Membership** tab, search for and select **Cloud Device Administrator**.

1. Select the **Setting** tab and configure the same way as Task 1:
   - **Assignment type:** **Active**
   - **Permanently eligible / Permanently assigned:** Leave checked
   - **Assignment starts / ends:** Leave the defaults (auto-populated start, no end date)

1. In the **Justification** box, enter a reason (for example: `Lab 01 role delegation exercise — assigning Cloud Device Administrator to help desk staff`).

1. Select **Add**.

   > [!NOTE]
   > The Cloud Device Administrator role allows managing device identities in Microsoft Entra ID, including enabling, disabling, and deleting devices. This role is useful for help desk staff who need to manage device objects without full Intune access.

**You have successfully assigned the Cloud Device Administrator role to Joni Sherman.**

---

### Task 3: Create an administrative unit

Administrative units allow you to restrict administrative permissions to a subset of users or devices. You'll create an administrative unit for the IT department.

1. In the **Microsoft Entra admin center**, in the left navigation under **Entra ID**, select **Roles & admins**, then select **Administrative units**.

1. Select **Add** from the top toolbar.

1. In the **Add administrative unit** pane, enter the following:
   - **Name:** `IT Department`
   - **Description:** `Administrative unit for IT department users and devices`

1. Select **Next**.

1. On the **Assign roles** page, select **Next** (we'll assign roles after adding members).

1. On the **Review + create** page, select **Create**.

**You have successfully created an administrative unit for the IT department.**

---

### Task 4: Add members to the administrative unit

1. On the **Admin units** page, select **IT Department** from the list.

1. In the **IT Department** administrative unit details, select **Users** from the left navigation.

1. Select **Add** from the top toolbar.

1. Search for and select **Allan Deyoung** (IT Admin).

1. Select **Add**.

1. In the **IT Department** administrative unit details, select **Groups** from the left navigation.

1. Select **Add** from the top toolbar.

1. Search for and select the existing **sg-IT** security group (pre-existing group for IT department users).

1. Select **Add**.

   > [!NOTE]
   > By adding users and groups to the administrative unit, you can scope administrative roles to only manage these objects. This is useful for delegating regional or departmental administration.

**You have successfully added members to the IT Department administrative unit.**

---

### Task 5: Assign a scoped role to the administrative unit

You'll assign a Helpdesk Administrator role scoped to only the IT Department administrative unit.

> [!NOTE]
> **Intune Administrator can't be assigned with administrative unit scope.** Only a fixed set of Microsoft Entra roles support AU scoping — Authentication Administrator, Attribute Assignment Administrator/Reader, Cloud Device Administrator, Groups Administrator, **Helpdesk Administrator**, License Administrator, Password Administrator, Printer Administrator, Privileged Authentication Administrator, SharePoint Administrator, Teams Administrator, Teams Devices Administrator, User Administrator, and any custom role — Intune Administrator isn't one of them. This is exactly why Intune has its own separate scope-tag system (Task 6): that's the supported way to delegate Intune-specific administration to a subset of devices/policies. Helpdesk Administrator is Microsoft's own canonical example for AU-scoped delegation, so we'll use it here to demonstrate the Entra-layer scoping mechanic.

1. In the **IT Department** administrative unit details, select **Roles and administrators** from the left navigation.

1. On the list of roles, search for and select **Helpdesk Administrator** by clicking its name (this page only lists roles that support administrative unit scope — there's no toolbar **Add** button that lets you search for an arbitrary role; you pick from the list shown).

1. On the role's assignment page, select **Add assignments**.

1. In the **Add assignments** pane, on the **Membership** tab, search for and select **Lab User1** (created in Exercise 1).

1. Select the **Setting** tab and configure:
   - **Assignment type:** **Active**
   - **Permanently eligible / Permanently assigned:** Leave checked
   - **Assignment starts / ends:** Leave the defaults

1. In the **Justification** box, enter a reason (for example: `Lab 01 role delegation exercise — scoped Helpdesk Administrator for IT Department AU`).

1. Select **Add**.

   > [!NOTE]
   > Lab User1 now has Helpdesk Administrator permissions, but only for users and devices within the IT Department administrative unit. This demonstrates role-based access control (RBAC) scoping at the Microsoft Entra layer.

**You have successfully assigned a scoped Helpdesk Administrator role.**

---

### Task 6: Create a custom Intune role and scope tag for the Pharmacy clinical workload

Microsoft Entra ID roles (Task 1–5) delegate Entra-level permissions. Intune itself has a **separate RBAC system** with its own custom roles and **scope tags**. Contoso Healthcare wants the Pharmacy helpdesk to see and act on Pharmacy clinical devices only — not the whole tenant — so you'll create a `Pharmacy` scope tag and a `Pharmacy Helpdesk` custom Intune role now. In **Labs 2–4** you'll apply the `Pharmacy` scope tag to specific configuration, compliance, app, and security policies. In **Lab 05 Exercise 3** you'll assign the `Pharmacy Helpdesk` role to a delegated administrator (Lee Gu) and verify end-to-end that they see only Pharmacy-scoped objects.

**Part A — Create the `Pharmacy` scope tag**

1. In the browser, navigate to **https://intune.microsoft.com** (Microsoft Intune admin center).

1. In the left navigation, expand **Tenant administration**, then select **Roles**.

1. On the **Roles** page, select **Scope (Tags)** (also labeled **Scope tags** in some portal builds).

1. Select **+ Create**.

1. On the **Basics** page, enter:
   - **Name:** `Pharmacy`
   - **Description:** `Pharmacy clinical devices and policies (Contoso Healthcare)`

1. Select **Next**.

1. On the **Assignments** page, leave **Selected groups** empty for now — you'll tag specific policies (not groups) starting in **Lab 02 Exercise 1**. Select **Next**.

1. On the **Review + create** page, select **Create**.

**Part B — Create the `Pharmacy Helpdesk` custom Intune role**

1. In **Tenant administration**, select **Roles**, then select **All roles**.

1. Select **+ Create** → **Intune role**.

1. On the **Basics** page, enter:
   - **Name:** `Pharmacy Helpdesk`
   - **Description:** `Delegated helpdesk role scoped to Pharmacy clinical devices. Read + remote actions on devices; no policy authoring.`

1. Select **Next**.

1. On the **Permissions** page, select **Yes** for the following permissions (leave everything else **No** — this is principle of least privilege). Portal labels group permissions into categories like **Managed devices**, **Remote tasks**, **Organization**, and **Roles**. Match the closest available labels in your portal:

   - **Managed devices:** **Read**, **Set primary user**, **Update**
   - **Remote tasks:** **Sync devices**, **Restart now** (or **Reboot now**), **Collect diagnostics**
   - **Organization:** **Read**
   - **Roles:** **Read**

   > [!IMPORTANT]
   > Leave **all** permissions on **Apps**, **Device compliance policies**, **Device configurations**, **Endpoint protection**, **Enrollment programs**, and **Policy sets** set to **No**. The Pharmacy Helpdesk should be able to act on devices but **not** author or modify any policy. This is the upper-intermediate delegation pattern: a narrow remote-action role layered on top of broad read.

1. Select **Next**.

1. On the **Scope (Tags)** page, select **+ Select** and add the **Pharmacy** scope tag you created in Part A. Select **Select**.

1. Remove the **Default** scope tag chip (select its **x**) so only **Pharmacy** remains selected.

   > [!NOTE]
   > This step scopes the **role definition itself**, not what the assigned admin can manage — those are two different things. Per Microsoft: *"The scope tag added on a role controls visibility of the role itself. The scope tag added in role assignment limits the visibility of Intune objects, like policies, apps, or devices, to only administrators in that role assignment."* Removing **Default** here keeps the Pharmacy Helpdesk role definition visible only to admins who already have the Pharmacy scope tag (Global/Intune Administrators still see everything — scope tags don't apply to Entra roles). The step that actually restricts what Lee Gu can manage day-to-day happens in **Lab 05 Exercise 3**, when you assign this role with Pharmacy as the assignment's scope.

1. Select **Next**.

1. On the **Assignments** page, select **Next** — you'll add a real assignment (to Lee Gu) in **Lab 05 Exercise 3** after the rest of the Pharmacy-scoped policies exist.

1. On the **Review + create** page, select **Create**.

> [!NOTE]
> The `Pharmacy` scope tag and `Pharmacy Helpdesk` role you just created are the foundation for delegated administration across the rest of this lab series. In **Labs 02–04** you'll apply the `Pharmacy` scope tag to configuration profiles, compliance policies, an LOB app, and a security baseline. In **Lab 05 Exercise 3** you'll assign the `Pharmacy Helpdesk` role to a delegated administrator (Lee Gu) and verify they see only Pharmacy-scoped objects. In **Lab 06 Exercise 2** the Pharmacy Helpdesk admin uses Remote Help on Pharmacy devices.

**You have successfully created the `Pharmacy` scope tag and the `Pharmacy Helpdesk` custom Intune role.**

---

**Previous:** [← Exercise 1: Configure users and groups](exercise-1.md) | **Next:** [→ Exercise 3: Configure device registration and settings](exercise-3.md)

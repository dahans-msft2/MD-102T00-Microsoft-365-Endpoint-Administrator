# Lab 02, Exercise 6: Use the Troubleshooting blade

### Scenario

The Troubleshooting blade provides a consolidated view of a user's devices, policies, app installations, and enrollment status. You'll use it to investigate device compliance and policy assignment.

### Task 1: Investigate a user's device status

1. In the **Microsoft Intune admin center**, expand **Troubleshooting + support** and select **Troubleshoot**.

1. In the **User** field (placeholder text "Search by display name or email"), search for and select **Megan Bowen**.

1. After selecting the user, the page populates with these sections (scrollable):
   - **Assignments** — group memberships and role assignments
   - **Devices** — devices owned by the user
   - **Enrollment restrictions** — platform restrictions that apply
   - **Applications** — assigned apps
   - **Compliance** — compliance policies assigned
   - **Configuration** — configuration profiles assigned
   - **Updates** — update rings assigned
   - **Policy conflicts** — settings that conflict between policies

1. Scroll to the **Devices** section.

1. Verify **SEA-DEV1** is listed in Megan Bowen's devices.

1. Select **SEA-DEV1** from the list to open the device blade.

1. Review:
   - **Enrollment date**
   - **Last check-in**
   - **Compliance status**
   - **Primary user**
   - **Management channel**

**You have successfully investigated a user's device status.**

---

### Task 2: Diagnose and resolve a policy conflict using Per-setting status

In **Exercise 1 Task 5** you intentionally created two configuration profiles — `WIN - Camera - Enabled (Pilot)` and `WIN - Camera - Disabled (Pilot)` — that conflict on the **Allow Camera** setting for the `sg-Intune-Pilot-Users` group. Now you'll find that conflict in the portal and resolve it. **Per-setting status** is the single most useful surface for this in Intune.

> [!IMPORTANT]
> **Device prerequisite.** The **Conflict** state only appears after a Windows device has actually checked in with the conflicting policies applied. **SEA-DEV1** (enrolled in **Lab 01 Exercise 5**) must be online and have synced at least once with the two camera profiles assigned. If you don't see **Conflict** in the steps below — only **Pending** or **Not evaluated** — go to **Devices** → **SEA-DEV1** → **Sync** and wait 5\u201310 minutes. If SEA-DEV1 isn't enrolled yet, return to **Lab 01 Exercise 5** before continuing.

1. On the **Troubleshoot** page (with **Megan Bowen** selected if she's a pilot member, or another pilot-cohort user), scroll to the **Configuration** section.

   > [!NOTE]
   > If Megan isn't in `sg-Intune-Pilot-Users`, switch to a user who is. In the validated lab tenant the pilot group contains the test users Jordan added in Lab 01 Exercise 1 Task 2.

1. Locate the two profiles in the list: `WIN - Camera - Enabled (Pilot)` and `WIN - Camera - Disabled (Pilot)`. Each entry shows a status column. You should see one or both displaying **Conflict** (it may also briefly show **Pending** if the device hasn't checked in yet — force a sync in the device blade first if needed).

1. Select one of the two conflicting profiles to open its detail blade.

1. In the profile blade, select **Device and user check-in status** → select the affected device (e.g., **SEA-DEV1**) → then drill into **Per-setting status**.

   > [!NOTE]
   > The Per-setting status view is the canonical conflict-diagnosis surface. It shows every individual setting in the profile and the device's resolution state for each (**Success**, **Pending**, **Error**, **Conflict**, **Not applicable**). A **Conflict** row means two or more policies are trying to set the same setting to different values — Intune cannot resolve, so it applies neither, and the device retains its existing local value.

1. Find the **Allow Camera** row. Confirm it shows **Conflict**.

1. Resolve the conflict. Pharmacy clinical regulations win at Contoso — cameras off in clinical areas — so you'll keep the **Disabled** profile and delete the **Enabled** one:
   - Navigate back to **Devices** → **Manage devices** → **Configuration**.
   - Select **WIN - Camera - Enabled (Pilot)**.
   - From the toolbar, select **Delete**, then confirm.

1. Trigger a device sync (Troubleshoot blade → device → **Sync**) and wait 2–5 minutes for the device to re-evaluate.

1. Return to **Per-setting status** for `WIN - Camera - Disabled (Pilot)` and confirm **Allow Camera** now shows **Success** (no longer **Conflict**), with the **Disabled** value applied.

   > [!NOTE]
   > Alternative resolutions you could have used in production: (a) change one profile's assignment so the two no longer overlap on the same group; (b) move the conflicting setting out of one profile entirely; (c) use **Settings catalog precedence** by ordering policies (where supported). Deleting the loser is the simplest — but on a real fleet, audit who created each conflicting profile and why before deleting.

**You have successfully diagnosed and resolved a real policy conflict using Per-setting status.**

---

### Task 3: Force a device sync from the Troubleshooting blade

1. On the **Troubleshoot** page (with Megan Bowen selected), in the **Devices** section, select **SEA-DEV1**.

1. Select **Sync** from the device actions toolbar.

1. Wait for the sync to complete (typically 1–2 minutes).

1. Refresh the page and verify the **Last check-in** timestamp updated.

   > [!NOTE]
   > The Sync action forces the device to check in with Intune immediately, retrieve new policies, and report current status. This is useful when troubleshooting policy deployment delays.

**You have successfully forced a device sync from the Troubleshooting blade.**

---

### Task 4: Investigate compliance state and Conditional Access (Report-only) impact

The `CA - Require compliant device (Pharmacy pilot)` Conditional Access policy you created in **Exercise 2 Task 3** is running in **Report-only** mode — it doesn't enforce, but it does log what *would* have happened on every sign-in. You'll inspect those logs now to see the policy's impact before flipping it to **On** in **Lab 04 Exercise 6**.

1. On the **Troubleshoot** page, with a pilot-cohort user selected (Megan Bowen or another `sg-Intune-Pilot-Users` member), scroll to the **Compliance** section.

1. Note the user's device compliance state. A **Not compliant** or **Not evaluated** state means the CA policy in enforcement mode would block the sign-in.

1. Open a new browser tab to **https://entra.microsoft.com** → **Identity** → **Monitoring & health** → **Sign-in logs**.

1. Filter the **User sign-ins (interactive)** view to the same pilot user, time range = Last 24 hours.

1. Select any recent sign-in entry to open its details pane.

1. Switch to the **Conditional Access** tab in the details pane. You should see `CA - Require compliant device (Pharmacy pilot)` listed with a **Result** of **Report-only: Success**, **Report-only: Failure**, **Report-only: Not applied**, or **Report-only: User action required**.

   > [!NOTE]
   > **Report-only result decoder:**
   > - **Success** — the user/device would have satisfied the grant (e.g., device is compliant). Enforcing the policy now would not block this sign-in.
   > - **Failure** — the grant requirement (compliance) was *not* met. Enforcing now **would block** this sign-in. This is what you're watching for.
   > - **Not applied** — the policy didn't match the sign-in's user/app/condition criteria. Expected for non-pilot users.
   > - **User action required** — the user could remediate (e.g., complete MFA). Less common for compliance-only grants.

1. Open a second sign-in entry from a user *outside* `sg-Intune-Pilot-Users` (e.g., the admin account). Confirm the CA policy shows **Report-only: Not applied** — because the policy is scoped only to the pilot group.

   > [!IMPORTANT]
   > Report-only → On is a deliberate, two-step rollout: watch the report for at least a few hours (production: days), confirm the **Failure** count is what you expect (i.e., only non-compliant devices), and only then switch to **On**. You'll perform the switch in **Lab 04 Exercise 6** after Lab 04's endpoint security policies have made more devices verifiably compliant.

**You have successfully investigated the Conditional Access policy's report-only impact and the compliance state behind it.**

---

**Previous:** [← Exercise 5: Enable Endpoint analytics and proactive remediations](exercise-5.md) | **Next:** [Lab summary →](summary.md)

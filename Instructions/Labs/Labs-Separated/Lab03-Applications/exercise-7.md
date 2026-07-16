# Lab 03, Exercise 7: Monitor app deployment and troubleshoot failures

### Scenario

You'll use the Intune admin center to monitor app deployment across all devices, identify failed installations, and troubleshoot common issues.

### Task 1: Review the App overview dashboard

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **Overview**.

1. Review the **App protection status** dashboard:
   - **iOS:** Number of users with protected apps
   - **Android:** Number of users with protected apps
   - **Windows:** (App Protection Policies not applicable to Windows)

1. Review the **App install status** dashboard:
   - **Failed:** Apps that failed to install
   - **In progress:** Apps currently installing
   - **Installed:** Successfully installed apps
   - **Not installed:** Apps not yet evaluated

1. Select **Failed** to view a list of failed app installations.

**You have successfully reviewed the App overview dashboard.**

---

### Task 2: Investigate a failed app installation

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps**.

1. Select an app that shows installation failures (e.g., **7-Zip Portable**).

1. Select **Device install status** from the left navigation.

1. Locate a device with status **Failed** and select it.

1. Review the error details:
   - **Error code:** Numeric code (e.g., 0x80070005 = Access Denied)
   - **Error message:** Description of the failure
   - **Last modified:** Timestamp of last installation attempt

1. Common failure reasons and resolutions:
   - **0x80070005 (Access Denied):** App installer requires elevation—set install behavior to "System" instead of "User"
   - **Detection rule not met:** App installed successfully but detection rule failed—verify detection rule logic
   - **Download failed:** Device has no internet connectivity or cannot reach Intune endpoints
   - **Disk space insufficient:** Device does not have enough free space for installation

**You have successfully investigated a failed app installation.**

---

### Task 3: Export app install status to CSV

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **Monitor** → **App install status**.

1. Select an app from the list (e.g., **Microsoft 365 Apps (Current Channel)**).

1. On the **Device install status** page, select **Export** from the top toolbar.

1. Wait for the export to complete (typically 1–2 minutes).

1. Select **Download** to save the CSV file.

1. Open the CSV in **Excel** and review the columns:
   - **Device name**
   - **User name**
   - **Platform**
   - **Status** (Installed, Failed, In Progress)
   - **Last check-in**

**You have successfully exported app installation data for reporting.**

---

### Task 4: Diagnose an intentional app-assignment conflict

App assignment intents can collide just like configuration profiles can. The classic example is one admin marking an app **Required** for a broad group while another admin marks the same app **Uninstall** for an overlapping group. Intune flags this in the **App install status** view as a conflict, and neither install nor uninstall completes cleanly. You'll deliberately create this situation, find it, and resolve it.

1. In the **Microsoft Intune admin center**, navigate to **Apps** → **All apps** → **7-Zip Portable** (the v1 app you deployed in Exercise 2 — *not* the v2.0).

1. Select **Properties** from the left navigation, then in the **Assignments** section select **Edit**.

1. Under **Uninstall**, select **Add group**.

1. Search for and select **sg-Intune-Pilot-Users** (the same pilot cohort that already has **7-Zip Portable v2.0** assigned as **Required** via supersedence). Select **Select**.

1. Select **Review + save** → **Save**.

   > [!IMPORTANT]
   > You've now told Intune: "Uninstall **7-Zip Portable** from pilot users" AND (via the v2.0 supersedence relationship) "Install **7-Zip Portable v2.0** on pilot users, replacing v1." These two intents partially overlap and produce a conflict.

1. Trigger a sync on **SEA-DEV1** (Settings → Accounts → Access work or school → Sync). Wait 5–10 minutes for Intune to evaluate.

1. In **Apps** → **All apps** → **7-Zip Portable**, select **Device install status**. Locate SEA-DEV1 (or any pilot device) and observe the status — you should see **Conflict** or an explicit failure with an error message indicating multiple intents.

   > [!NOTE]
   > Intune surfaces app conflicts as either **Conflict** in the device install status column, or as a specific error in the per-device drill-in. **App install status** is the single most useful surface for diagnosing app assignment fights, the same way **Per-setting status** is for configuration profile conflicts (Lab 02 Exercise 6).

1. Resolve the conflict. The supersedence path is the correct one (v1 → v2.0 is automatic), so remove the redundant Uninstall assignment on v1:
   - On **7-Zip Portable** → **Properties** → **Assignments** → **Edit**.
   - Under **Uninstall**, hover over **sg-Intune-Pilot-Users** and select the **Remove** icon (trash can).
   - Select **Review + save** → **Save**.

1. Trigger another sync on SEA-DEV1, wait 5–10 minutes, and re-check **Device install status** on **7-Zip Portable v2.0**. Confirm SEA-DEV1 shows **Installed** with no remaining conflict on the v1 app.

   > [!NOTE]
   > In production, the upper-intermediate move is to set up **assignment audits** — review the **Audit logs** for app-assignment edits when you find a conflict to see who added the conflicting intent and when. You'll inspect audit logs in **Lab 05 Exercise 4**.

**You have successfully diagnosed and resolved an app-assignment conflict.**

---

**Previous:** [← Exercise 6: Create an App Protection Policy](exercise-6.md) | **Next:** [Lab summary →](summary.md)

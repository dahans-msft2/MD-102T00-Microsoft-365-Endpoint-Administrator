# Lab 02, Exercise 4: Configure Windows Update management

### Scenario

You'll use Windows Update for Business policies (Update rings) to control when devices receive feature and quality updates. You'll create multiple rings for phased rollouts (pilot, standard, and conservative).

### Task 1: Create a pilot update ring

1. In the **Microsoft Intune admin center**, expand **Devices**, then under **By platform** select **Windows**, then on the Windows blade select **Windows updates**.

   > [!NOTE]
   > The page header reads **Devices | Windows updates**. The tabs are **Releases**, **Update rings**, **Feature updates**, **Quality updates**, **Driver updates**, and **Monitor**. The page opens on **Releases** — you'll switch tabs in the next step.
   >
   > The page may also display two banners that are safe to ignore for the lab:
   >
   > - **Hotpatch Enablement** — eligible devices auto-receive Hotpatch quality updates. Leave the **Opt out** button alone.
   > - **Windows 10 reached end of support on October 14, 2025** — informational; the lab still references Windows 10.

1. Select the **Update rings** tab.

1. Select **Create profile**.

1. On the **Basics** page, enter:
   - **Name:** `Update Ring - Pilot`
   - **Description:** `Pilot ring for early adopters—receives updates immediately`

1. Select **Next**.

1. On the **Update ring settings** page, configure:
   - **Microsoft product updates:** Allow
   - **Windows drivers:** Allow

1. Under **Quality updates**:
   - **Quality update deferral period (days):** 0
   - **Set quality update uninstall period (2–60 days):** 30

1. Under **Feature updates**:
   - **Feature update deferral period (days):** 0
   - **Set feature update uninstall period (2–60 days):** 30

1. Under **User experience settings**:
   - **Automatic update behavior:** Auto install and restart at maintenance time
   - **Active hours start:** 8 AM
   - **Active hours end:** 5 PM
   - **Restart checks:** Allow
   - **Option to pause updates:** Disable
   - **Option to check for Windows updates:** Enable

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**.

   > [!NOTE]
   > Tagging the pilot ring with `Pharmacy` keeps it visible to the Pharmacy Helpdesk (who pilots clinical updates first) when you assign the role in **Lab 05 Exercise 3**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created a pilot update ring.**

---

### Task 2: Create a standard update ring

1. On the **Update rings** page, select **Create profile**.

1. On the **Basics** page, enter:
   - **Name:** `Update Ring - Standard`
   - **Description:** `Standard ring for general users—defers updates by 7 days`

1. Select **Next**.

1. On the **Update ring settings** page, configure:
   - **Quality update deferral period (days):** 7
   - **Feature update deferral period (days):** 14
   - **Automatic update behavior:** Auto install and restart at maintenance time
   - **Active hours start:** 8 AM
   - **Active hours end:** 5 PM
   - **Option to pause updates:** Enable (allows users to pause updates for up to 7 days)

1. Select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Under **Exclude groups**, select **Add groups**.

1. Search for and select **sg-Intune-Pilot-Users** (to exclude pilot users who already have the Pilot ring assigned).

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created a standard update ring with deferrals.**

---

### Task 3: Monitor Windows Update deployment status

The pilot cohort (`sg-Intune-Pilot-Users`, created in **Lab 01 Exercise 1**) is the same group that received the blocking ESP in **Lab 01 Exercise 4** and the pilot configuration profile in this lab's Exercise 1. That single cohort threads through every rollout in this lab series — update rings here, ASR rules in Lab 04, remediation rollout in Lab 05, EPM in Lab 06. Watching one consistent pilot cohort across rings is what makes phased rollouts work in production.

1. In the **Microsoft Intune admin center**, navigate to **Reports** → **Windows updates**.

   The page header reads **Reports | Windows updates** and opens to the **Summary** tab, which shows two aggregated reports: **Windows Feature updates** and **Windows Expedited Quality updates**. A second **Reports** tab on the same page lists the detailed drill-in reports.

1. On the **Summary** tab, in the **Windows Feature updates** section, select **Generate report**.

1. Review the report data:
   - **Policy**
   - **Versions**
   - **In progress**
   - **Success**
   - **Error**
   - **Rollback initiated or completed**
   - **Cancelled**
   - **On hold**

1. Navigate to **Devices** → **All devices** → Select **CL1**.

1. In the CL1 device blade, select **Monitor** in the left navigation, then select **Windows update**.

1. Review the update status:
   - **Last check-in:** Timestamp of last Windows Update check
   - **Pending updates:** List of available updates
   - **Installed updates:** List of updates already installed

**You have successfully monitored Windows Update deployment status.**

---

### Task 4: Create a Feature update profile

Update rings control *when* updates install. **Feature update profiles** control *which version* of Windows devices are pinned to — a separate axis. You'll create a Feature update profile that pins the broader fleet to Windows 11 24H2 while the pilot cohort runs ahead via the Pilot update ring.

1. In the **Microsoft Intune admin center**, in **Devices** → **Windows updates**, select the **Feature updates** tab.

1. Select **+ Create profile**.

1. On the **Basics** page, enter:
   - **Name:** `Feature Update - Win11 24H2`
   - **Description:** `Pin Contoso fleet to Windows 11 24H2`

1. Select **Next**.

1. On the **Deployment settings** page, configure:
   - **Feature update version to deploy:** **Windows 11, version 24H2**
   - **Rollout options:** **Make update available as soon as possible**

   > [!NOTE]
   > Use the **Gradual rollout** option in production to release the feature update to subsets of the fleet on a schedule. For this lab, immediate availability keeps the flow simple.

1. Select **Next**.

1. On the **Scope tags** page, leave the **Default** scope tag (this profile is tenant-wide). Select **Next**.

1. On the **Assignments** page, assign to **dyn-Windows-Devices**. Under **Exclude groups**, add **sg-Intune-Pilot-Users** (the pilot cohort runs ahead via the Pilot update ring, so excluding them here prevents the Feature update profile from holding them back).

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created a Feature update profile.**

---

### Task 5: Create an Expedited Quality update policy

**Expedited Quality updates** push out-of-band security patches faster than the normal deferral window. They're the right answer for an active zero-day. You'll create a policy that installs the latest critical security patch within 2 days, overriding any deferral the regular Update ring would apply.

1. In **Devices** → **Windows updates**, select the **Quality updates** tab.

1. Select **+ Create profile** (or **Create profile**).

1. On the **Basics** page, enter:
   - **Name:** `Quality Update - Expedited critical patches`
   - **Description:** `Push out-of-band security patches within 2 days, overriding ring deferrals`

1. Select **Next**.

1. On the **Expedited update settings** page, configure:
   - **Expedite installation of quality updates if a device's OS version is less than:** select the most recent monthly security update offered in the dropdown.
   - **Number of days from update release until restart is required:** `2`

1. Select **Next**.

1. On the **Scope tags** page, leave **Default**. Select **Next**.

1. On the **Assignments** page, assign to **dyn-Windows-Devices** (no exclusions — expedited security updates apply to everyone, including pilot).

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

   > [!NOTE]
   > Update rings + Feature update profiles + Expedited Quality update policies are the three layers of Windows Update for Business in Intune. Rings control timing for routine quality updates; Feature update profiles control which Windows version is offered; Expedited Quality update policies override timing for security-critical patches.

**You have successfully created an Expedited Quality update policy.**

---

**Previous:** [← Exercise 3: Analyze Group Policy Objects](exercise-3.md) | **Next:** [→ Exercise 5: Enable Endpoint analytics and proactive remediations](exercise-5.md)

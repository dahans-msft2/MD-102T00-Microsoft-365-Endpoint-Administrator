# Lab 02, Exercise 2: Configure compliance policies

### Scenario

Compliance policies define security and health requirements for devices. Non-compliant devices can be marked as such in Microsoft Entra ID, triggering Conditional Access policies to block access to corporate resources.

### Task 1: Create a Windows compliance policy

1. In the **Microsoft Intune admin center**, expand **Devices**, then under **Manage devices** select **Compliance**.

   > [!NOTE]
   > The page header reads **Devices | Compliance** and opens to the **Policies** tab by default. The other tabs are **Notifications**, **Retire noncompliant devices**, **Compliance settings**, **Scripts**, and **Monitor**.

1. Select **Create policy**.
1. In the **Create a policy** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Windows 10/11 compliance policy

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Compliance - Windows Security Baseline`
   - **Description:** `Requires BitLocker encryption, antivirus, firewall, and secure boot`

1. Select **Next**.

1. On the **Compliance settings** page, expand **Device Health** and configure:
   - **BitLocker:** Require
   - **Secure Boot:** Require
   - **Code integrity:** Require

1. Expand **Device Properties** and configure:
   - **Minimum OS version:** `10.0.19045` (Windows 11 22H2 or Windows 10 21H2)

1. Expand **System Security** and configure:
   - **Require a password to unlock mobile devices:** Require
   - **Simple passwords:** Block
   - **Password type:** Alphanumeric
   - **Password Complexity:** Require digits, lowercase, uppercase, and special characters
   - **Minimum password length:** 8
   - **Require encryption of data storage on device:** Require
   - **Firewall:** Require
   - **Antivirus:** Require
   - **Antispyware:** Require
   - **Microsoft Defender Antimalware:** Require
   - **Microsoft Defender Antimalware minimum version:** Leave blank (any version)
   - **Microsoft Defender Antimalware intelligence up-to-date:** Require
   - **Real-tiem protection:** Require

1. Select **Next**.

1. On the **Actions for noncompliance** page, review the default action:
   - **Mark device noncompliant:** Immediately

1. Select **Add** to add an additional action.

1. Configure the new action:
   - **Action:** Send email to end user
   - **Schedule (days after noncompliance):** 1
   - **Message template:** Select **Default** (or create a custom template)
   - **Additional recipients:** Leave blank

   > [!NOTE]
   > This sends an email to the device's primary user 1 day after the device becomes non-compliant, giving them time to remediate the issue.
   >
   > If no Default message template is available, navigate to the **Notifications** tab on the **Compliance** page first and select **+ Create notification** to create one before configuring this action.

1. Select **Add** to add another action.

1. Configure:
   - **Action:** Mark device non-compliant
   - **Schedule (days after noncompliance):** 7

   > [!NOTE]
   > This provides a 7-day grace period before the device is officially marked non-compliant in Microsoft Entra ID (triggering Conditional Access blocks).

1. Select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully created a Windows compliance policy with grace periods and notification actions.**

---

### Task 2: Monitor compliance policy results

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Monitor**, then under **Compliance** select **Noncompliant devices**.

1. Review the compliance dashboard, which surfaces:
   - **Device compliance trend:** Shows compliance over time
   - **Policy compliance:** Shows per-policy compliance rates

1. Navigate to **Devices** → **All devices**.

1. Select **CL1** from the device list.

1. Review the **Compliance** tab:
   - **Compliance status:** May show "Not evaluated," "Compliant," or "Not compliant"
   - **Last check-in:** Timestamp of last sync with Intune

   > [!NOTE]
   > Compliance evaluation can take 5–10 minutes after policy assignment. If the status shows "Not evaluated," select **Sync** from the top toolbar to force a policy refresh, then wait a few minutes and refresh the page.

1. If the device shows non-compliant, select **Device compliance** to view which settings failed.

**You have successfully monitored compliance policy results.**

---

### Task 3: Create a Conditional Access policy that requires device compliance (Report-only)

A compliance policy on its own doesn't block anything — it just marks devices as compliant or noncompliant. The teeth come from a **Conditional Access (CA)** policy that requires the **Marked as compliant** state for access to corporate resources. You'll create that CA policy now, but you'll start it in **Report-only** mode so you can observe its impact in this lab and **Lab 04 Exercise 6** before flipping it to **On**.

1. Open a new browser tab and navigate to **https://entra.microsoft.com** (Microsoft Entra admin center). Sign in as **admin@<TenantPrefix>.onmicrosoft.com** if prompted.

1. In the left navigation, select **Protection**, then select **Conditional Access**.

1. On the **Conditional Access | Overview** page, select **Policies**, then select **+ New policy**.

1. On the **New** policy page, configure:
   - **Name:** `CA - Require compliant device (Pharmacy pilot)`

1. Under **Assignments** → **Users**, select **0 users and groups selected**:
   - On the **Include** tab, select **Select users and groups** → check **Users and groups** → select **sg-Intune-Pilot-Users** → **Select**.
   - On the **Exclude** tab, select **Users and groups** → select **admin@<TenantPrefix>.onmicrosoft.com** (or whichever account you signed in with) → **Select**.

   > [!WARNING]
   > **Always exclude at least one Global Administrator (break-glass account) from any Conditional Access policy that could block sign-in.** Report-only mode doesn't enforce, but this policy switches to **On** in **Lab 04 Exercise 6** — the exclusion must be in place *before* that switch, or you risk locking yourself out of the tenant.

1. Under **Assignments** → **Target resources**, select **0 resources selected**:
   - **Select what this policy applies to:** Cloud apps
   - **Include:** All cloud apps
   - Acknowledge the warning about including all apps.

1. Under **Assignments** → **Conditions**, select **0 conditions selected** → **Client apps** → **Configure: Yes** → check both **Browser** and **Mobile apps and desktop clients** → **Done**.

1. Under **Access controls** → **Grant**, select **0 controls selected**:
   - Select **Grant access**.
   - Check **Require device to be marked as compliant**.
   - Leave **For multiple controls** at **Require all the selected controls**.
   - Select **Select**.

1. Under **Enable policy**, select **Report-only**.

   > [!NOTE]
   > **Report-only** evaluates the policy on every sign-in and logs the result (Success / Failure / Not applied / User action required) but does **not** enforce it. This is the canonical safe-rollout pattern for any CA policy that could block sign-in.

1. Select **Create**.

> [!NOTE]
> This CA policy was created in **Report-only** mode. You'll inspect its sign-in-log impact in **Exercise 6 Task 4** of this lab, and you'll switch it to **On** in **Lab 04 Exercise 6** after reviewing the report.

**You have successfully created a Conditional Access policy that requires device compliance (Report-only mode).**

---

**Previous:** [← Exercise 1: Create configuration profiles](exercise-1.md) | **Next:** [→ Exercise 3: Analyze Group Policy Objects](exercise-3.md)

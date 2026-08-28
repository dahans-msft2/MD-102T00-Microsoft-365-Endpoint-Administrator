# Lab 04, Exercise 6: Monitor security posture and compliance

### Scenario

You'll use the Microsoft Defender portal and Intune admin center to monitor device security posture, compliance with policies, and threat detections.

### Task 1: Review the Microsoft Defender Secure Score

1. In **Microsoft Edge**, navigate to **https://security.microsoft.com**.

1. Sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. In the **Microsoft Defender portal**, select **Secure Score** from the left navigation.

1. Review the **Secure Score** dashboard:
   - **Overall score:** Percentage of achieved vs. maximum possible points
   - **Improvement actions:** Recommended security configurations to increase score
   - **Score over time:** Trend chart showing security posture changes

1. Select an improvement action (e.g., "Enable BitLocker on all devices") to view details and remediation guidance.

**You have successfully reviewed the Microsoft Defender Secure Score.**

---

### Task 2: Review threat detections and alerts

1. In the **Microsoft Defender portal**, select **Incidents & alerts** → **Alerts**.

1. Review the list of security alerts (if any):
   - **Severity:** High, Medium, Low, Informational
   - **Alert title:** Description of the detected threat
   - **Affected devices:** Devices where the threat was detected
   - **Status:** New, In progress, Resolved

1. Select an alert to view detailed investigation information:
   - **Alert story:** Timeline of events leading to the alert
   - **Evidence:** Files, processes, or network connections involved
   - **Recommended actions:** Steps to remediate the threat

   > [!NOTE]
   > In a new lab environment with no active threats, you may see no alerts. Review the dashboard structure to understand how alerts are presented.

**You have successfully reviewed threat detections and alerts in the Microsoft Defender portal.**

---

### Task 3: Switch the Conditional Access policy from Report-only to On

In **Lab 02 Exercise 2 Task 3** you created the Conditional Access policy `CA - Require compliant device (Pharmacy pilot)` in **Report-only** mode. In **Lab 02 Exercise 6 Task 4** you inspected its impact via Sign-in logs. The endpoint security policies you deployed in Exercises 1–3 of this lab (Defender baseline, Antivirus, Firewall, ASR, BitLocker) should now have more pilot devices passing compliance evaluation. It's time to switch the CA policy from Report-only to **On**.

> [!WARNING]
> Before you enable the policy, **verify the break-glass exclusion is still in place**. If your Global Admin account is no longer in the **Exclude** list, fix that first or you risk locking yourself out of the tenant.

1. Open a new browser tab to **https://entra.microsoft.com** and sign in as **admin@<TenantPrefix>.onmicrosoft.com**.

1. Navigate to **Protection** → **Conditional Access** → **Policies**.

1. Select `CA - Require compliant device (Pharmacy pilot)`.

1. Confirm:
   - **Users → Include:** `sg-Intune-Pilot-Users`
   - **Users → Exclude:** `admin@<TenantPrefix>.onmicrosoft.com` (or whichever Global Admin you use)
   - **Target resources:** All cloud apps
   - **Grant:** Require device to be marked as compliant

1. Before flipping the switch, run a **What If** analysis:
   - From the **Conditional Access** overview, select **What If** from the top toolbar.
   - **User or workload identity:** select a pilot-cohort user (e.g., Megan Bowen if she's in the pilot group).
   - **Cloud apps, actions, or authentication context:** All cloud apps.
   - Leave other conditions at defaults.
   - Select **What If**.

1. Review the results. The bottom panel shows **Policies that would apply** and **Policies that won't apply**. Confirm `CA - Require compliant device (Pharmacy pilot)` appears under **Policies that would apply** with the grant **Require device to be marked as compliant**.

   > [!NOTE]
   > **What If** is the production-safe rehearsal for enabling any CA policy. It runs the full evaluation engine against a simulated sign-in without affecting real users. If a non-pilot user accidentally lands under "would apply" — stop and fix the assignment scope before flipping the switch.

1. Return to the policy detail view and scroll to **Enable policy**.

1. Change **Enable policy** from **Report-only** to **On**.

1. Select **Save**.

   > [!IMPORTANT]
   > The policy is now **enforced**. The next time a pilot-cohort user signs in to any cloud app on a non-compliant device, the sign-in will be blocked with the message "Your device is not compliant with the policies set by your IT department." The user can self-remediate by addressing the failing compliance setting (e.g., enable BitLocker, install missing security updates).

1. Switch back to **Identity** → **Monitoring & health** → **Sign-in logs**. Filter to a pilot-cohort user. Open a recent sign-in entry and confirm the **Conditional Access** tab now shows the policy as **Success** or **Failure** (not **Report-only: ...**).

**You have successfully enabled the Conditional Access policy, completing the compliance → CA enforcement story that started in Lab 02.**

---

**Previous:** [← Exercise 5: Implement Microsoft Cloud PKI](exercise-5.md) | **Next:** [Lab summary →](summary.md)

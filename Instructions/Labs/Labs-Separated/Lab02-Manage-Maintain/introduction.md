---
lab:
  title: 'Lab 02: Manage and maintain devices'
  description: 'In this lab, you create device configuration profiles, compliance policies, and Windows Update rings, analyze Group Policy Objects for migration, and enable Endpoint analytics and proactive remediations.'
  duration: 100 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune
    - Windows
    - Windows Update for Business
---

# Lab 02: Manage and maintain devices

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With devices now enrolled in Intune (from Lab 01), you need to implement device configuration profiles, compliance policies, and Windows Update management. You'll also analyze existing Group Policy Objects for migration to Intune, enable Endpoint analytics for proactive monitoring, and deploy remediation scripts to maintain device health.

By the end of this lab, you'll have:
- Created configuration profiles using Settings Catalog and templates
- Applied the `Pharmacy` scope tag (from **Lab 01 Exercise 2 Task 6**) to configuration, compliance, and update policies
- Built compound assignment filters using both include and exclude modes
- Intentionally created conflicting configuration profiles and resolved the conflict with **Per-setting status**
- Configured compliance policies with grace-period actions for noncompliance
- Created a Conditional Access policy that requires compliant devices (**Report-only** mode — you switch it **On** in Lab 04)
- Analyzed Group Policy Objects for migration readiness using Group Policy analytics
- Configured update rings, a Feature update profile, and an Expedited Quality update policy
- Enabled Endpoint analytics and reviewed device performance insights
- Deployed a proactive remediation script
- Used the Troubleshooting blade to investigate device status, diagnose policy conflicts, and inspect Conditional Access impact

---

## Lab Duration

**Estimated Time:** 100 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled, groups configured)
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- Global Administrator or Intune Administrator credentials
- **SEA-DEV1** (enrolled device, Megan Bowen signed in)
- **SEA-DEV2** (enrolled device, Joni Sherman signed in)
- Group Policy backup XML files (provided in lab assets)

> [!NOTE]
> **The Intune Devices workload has been reorganized.** All the configuration, compliance, scripts, and Group Policy analytics surfaces now live under a **Manage devices** group inside the Devices left navigation. **Windows updates** lives under **By platform > Windows**. **Assignment filters** has moved to **Tenant administration > Assignment filters**. This lab uses the current navigation paths throughout.
>
> **Tenant prerequisite for Exercise 5 — Remediations:** Use of remediations requires **Windows license verification** to be enabled under **Tenant administration > Intune add-ons**. If your lab tenant doesn't have an Intune Suite or Remediations add-on entitlement, you can still walk through the wizard, but the script package won't execute on devices.

---

## Exercises in this lab

1. [Exercise 1: Create configuration profiles](exercise-1.md)
2. [Exercise 2: Configure compliance policies](exercise-2.md)
3. [Exercise 3: Analyze Group Policy Objects](exercise-3.md)
4. [Exercise 4: Configure Windows Update management](exercise-4.md)
5. [Exercise 5: Enable Endpoint analytics and proactive remediations](exercise-5.md)
6. [Exercise 6: Use the Troubleshooting blade](exercise-6.md)
7. [Lab summary](summary.md)

---

**Next:** [→ Exercise 1: Create configuration profiles](exercise-1.md)

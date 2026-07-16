---
lab:
  title: 'Lab 06: Extend capabilities'
  description: 'In this lab, you configure Endpoint Privilege Management, deploy Remote Help, use Advanced Analytics and Device Query, and explore Windows 365 and Azure Virtual Desktop cloud-hosted desktop provisioning.'
  duration: 90 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune Suite
    - Windows 365
    - Azure Virtual Desktop
---

# Lab 06: Extend capabilities

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. You've implemented a comprehensive Intune environment (Labs 01-05) and now want to leverage premium capabilities from the **Microsoft Intune Suite**. You'll configure Endpoint Privilege Management (EPM) to control application elevation, deploy Remote Help for secure remote assistance, review Advanced Analytics dashboards, and explore cloud-hosted desktop scenarios (Windows 365 and Azure Virtual Desktop).

By the end of this lab, you'll have:
- Enabled Endpoint Privilege Management in tenant settings
- Created Windows elevation settings and elevation rules policies
- Tested EPM elevation scenarios (automatic, user-confirmed, support-approved)
- Rolled EPM out to the pilot cohort first, then expanded to the fleet (the canonical pilot-first pattern)
- Enabled Remote Help and assigned licenses
- Deployed the Remote Help app to devices
- Initiated a Remote Help session between devices
- Demonstrated that the Pharmacy Helpdesk delegated admin (Lee Gu, from **Lab 05 Exercise 3**) can launch Remote Help on Pharmacy-scoped devices only
- Reviewed Advanced Analytics dashboards (demonstration)
- Explored Windows 365 Cloud PC provisioning (demonstration)
- Reviewed Azure Virtual Desktop session host enrollment (demonstration)

---

## Lab Duration

**Estimated Time:** 90 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled)
- **Microsoft Intune Suite trial active** (activated in **Lab 01** prerequisites) — required for Endpoint Privilege Management, Remote Help, and Advanced Analytics
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- Global Administrator or Intune Administrator credentials
- **CL1**, **CL2**, and **CL3** (enrolled Windows 11 devices)

---

## Exercises in this lab

1. [Exercise 1: Configure Endpoint Privilege Management (EPM)](exercise-1.md)
2. [Exercise 2: Deploy Remote Help](exercise-2.md)
3. [Exercise 3: Use Advanced Analytics and Device Query](exercise-3.md)
4. [Exercise 4: Explore Windows 365 Cloud PC provisioning](exercise-4.md)
5. [Exercise 5: Explore Azure Virtual Desktop session host enrollment](exercise-5.md)
6. [Lab summary](summary.md)

---

**Next:** [→ Exercise 1: Configure Endpoint Privilege Management (EPM)](exercise-1.md)

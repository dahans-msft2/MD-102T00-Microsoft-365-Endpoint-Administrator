---
lab:
  title: 'Lab 05: Automate and operate'
  description: 'In this lab, you automate device management with Microsoft Graph PowerShell, deploy proactive remediations, implement RBAC with scope tags for delegated administration, and review audit logs and built-in reports.'
  duration: 100 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune
    - Microsoft Graph
    - PowerShell
---

# Lab 05: Automate and operate

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With your Intune environment fully deployed (devices enrolled, apps deployed, security policies configured), you now need to implement automation and operational excellence practices. You'll use Microsoft Graph PowerShell for scripted device management, deploy proactive remediations, implement role-based access control (RBAC) with scope tags for delegated administration, configure audit logging, and leverage built-in reporting for operational insights.

By the end of this lab, you'll have:
- Registered an app in Microsoft Entra ID for unattended Graph API automation
- Authenticated with Microsoft Graph PowerShell SDK
- Queried managed devices and policies using Graph API — including filtering by the `Pharmacy` scope tag
- Deployed a proactive remediation script package using a **pilot-first** rollout pattern
- Assigned the **`Pharmacy Helpdesk`** custom role (created in **Lab 01 Exercise 2 Task 6**) to a delegated administrator (**Lee Gu**) and verified end-to-end scope behavior across all Pharmacy-scoped objects created in Labs 02–04
- Reviewed audit logs for admin activity tracking, including Conditional Access policy edits, compliance policy changes, and scope-tag operations
- Used built-in reports to export device and compliance data
- Monitored tenant health and service status

---

## Lab Duration

**Estimated Time:** 100 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled, groups configured)
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- Global Administrator credentials
- **SEA-DEV1** (enrolled device, Megan Bowen signed in)
- Microsoft Graph PowerShell SDK installed on SEA-DEV1

---

## Exercises in this lab

1. [Exercise 1: Automate with Microsoft Graph PowerShell](exercise-1.md)
2. [Exercise 2: Deploy proactive remediations](exercise-2.md)
3. [Exercise 3: Assign and verify the Pharmacy Helpdesk delegated role end-to-end](exercise-3.md)
4. [Exercise 4: Monitor audit logs and operational health](exercise-4.md)
5. [Exercise 5: Use built-in reports](exercise-5.md)
6. [Lab summary](summary.md)

---

**Next:** [→ Exercise 1: Automate with Microsoft Graph PowerShell](exercise-1.md)

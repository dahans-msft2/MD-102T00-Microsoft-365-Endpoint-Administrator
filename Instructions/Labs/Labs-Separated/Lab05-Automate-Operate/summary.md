# Lab 05: Automate and operate — Summary

Congratulations! You've completed Lab 05: Automate and operate.

In this lab, you accomplished the following:

**Exercise 1: Automate with Microsoft Graph PowerShell**
- Installed the Microsoft Graph PowerShell SDK
- Registered an application for unattended automation
- Granted API permissions and created a client secret
- Authenticated with Microsoft Graph using application credentials
- Queried managed devices using Graph PowerShell
- Created and assigned a compliance policy using Graph API

**Exercise 2: Deploy proactive remediations**
- Created detection and remediation PowerShell scripts
- Uploaded a remediation script package to Intune and assigned to the pilot cohort
- Monitored remediation execution on pilot devices
- Expanded the rollout from pilot to the broader fleet

**Exercise 3: Assign and verify the Pharmacy Helpdesk delegated role end-to-end**
- Reviewed the `Pharmacy Helpdesk` role and `Pharmacy` scope tag created in **Lab 01 Exercise 2 Task 6**
- Inventoried Pharmacy-tagged objects across **Labs 02–04** (configuration, compliance, app, security baseline, ASR, BitLocker)
- Assigned the `Pharmacy Helpdesk` role to Lee Gu with the `Pharmacy` scope tag on the assignment
- Signed in as Lee Gu and verified end-to-end that only Pharmacy-tagged objects are visible — and that policy editing is blocked

**Exercise 4: Monitor audit logs and operational health**
- Reviewed Intune audit logs for administrative actions
- Exported audit logs to CSV for reporting
- Understood diagnostic settings for long-term log retention in Azure Monitor
- Traced the Conditional Access, compliance, conflict-resolution, and RBAC operations from Labs 02–04 across both the **Intune audit log** and the **Entra audit log**

**Exercise 5: Use built-in reports**
- Generated device compliance and configuration reports
- Exported report data to CSV
- Reviewed the Tenant status dashboard for service health and connector status

**Key Takeaways:**
- Microsoft Graph PowerShell enables scripted automation for bulk operations, reporting, and scope-tag-aware queries (`roleScopeTagIds` is the underlying property)
- Application permissions and client secrets allow unattended automation without user interaction
- Proactive remediations detect and fix common issues before users report problems; pilot-first rollout is the canonical pattern
- Custom RBAC roles + scope tags + group scope = the three dimensions of Intune delegated administration; the role's permissions intersect with the scope tag and the group target to produce the final visibility a delegated admin sees
- Pharmacy Helpdesk → Lee Gu is the end-to-end demonstration: a role created on day one (Lab 01) gates visibility across every policy created in Labs 02–04, with no further configuration needed in Lab 05
- Intune and Entra each have their own audit log — reach for both when investigating an incident or change
- Built-in reports and the Tenant status dashboard provide operational visibility

**Next Steps:**
In Lab 06, you'll extend Intune capabilities using the Intune Suite (Endpoint Privilege Management, Remote Help, Advanced Analytics) and explore cloud-hosted desktops (Windows 365 and Azure Virtual Desktop).

---

**END OF LAB**

---

**Previous:** [← Exercise 5: Use built-in reports](exercise-5.md)

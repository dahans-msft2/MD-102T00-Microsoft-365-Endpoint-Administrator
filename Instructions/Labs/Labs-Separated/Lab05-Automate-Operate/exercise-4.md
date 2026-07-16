# Lab 05, Exercise 4: Monitor audit logs and operational health

### Scenario

Audit logs track administrative actions in Intune, providing accountability and troubleshooting insights. You'll review audit logs and configure diagnostic settings to route logs to Azure Monitor (conceptual).

### Task 1: Review audit logs

1. In the **Microsoft Intune admin center**, expand **Tenant administration** and select **Audit logs**.

1. On the **Audit logs** page, review the list of recent administrative actions:
   - **Activity:** Type of action (Create, Update, Delete, Assign, etc.)
   - **Date:** Timestamp of the action
   - **Initiated by (actor):** User or service principal who performed the action
   - **Target(s):** Object that was modified (policy, device, app, etc.)

1. Filter logs by activity:
   - Use the **Activity** dropdown to filter by action type (e.g., "Create policy")
   - Use the **Date range** picker to filter by time period

1. Select an audit log entry to view detailed information:
   - **Properties:** JSON payload showing before/after state (for Update actions)
   - **Actor:** UPN and IP address of the user who performed the action

   > [!NOTE]
   > Audit logs are retained for 30 days in Intune. For long-term retention, export logs to Azure Monitor or a SIEM system.

**You have successfully reviewed Intune audit logs.**

---

### Task 2: Export audit logs to CSV

1. On the **Audit logs** page, select **Export** from the top toolbar.

1. Wait for the export to complete (typically 1–2 minutes for small datasets).

1. Select **Download** to save the CSV file.

1. Open the CSV file in **Excel** and review the columns:
   - **Date**
   - **Activity**
   - **Initiated By**
   - **Target**
   - **Category**

**You have successfully exported audit logs for reporting.**

---

### Task 3: Understand diagnostic settings (conceptual)

Diagnostic settings route Intune logs to Azure Monitor Log Analytics for long-term retention and advanced querying.

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Diagnostics settings**.

   > [!NOTE]
   > Diagnostic settings require an Azure subscription and Log Analytics workspace. For lab purposes, review the configuration options conceptually.

1. Review the available log categories:
   - **AuditLogs:** Administrative actions in Intune
   - **OperationalLogs:** Device sync events, policy application, enrollment events
   - **DeviceComplianceOrg:** Compliance policy evaluation results

1. Understand the configuration workflow (do not create):
   - Create a Log Analytics workspace in Azure
   - In Intune, create a diagnostic setting pointing to the workspace
   - Logs are routed to Azure Monitor for querying with KQL (Kusto Query Language)
   - Retention can be extended to 90 days, 1 year, or longer

**You now understand how diagnostic settings enable long-term log retention and advanced analytics.**

---

### Task 4: Trace the Conditional Access, compliance, and RBAC operations from earlier labs

Audit logs are how you reconstruct "who changed what, when, and why" — the bedrock of post-incident review. You'll trace the specific operations you performed across the lab series:

1. In the **Microsoft Intune admin center**, in **Tenant administration** → **Audit logs**, filter the log:
   - **Date range:** Last 7 days
   - **Activity:** **Create** (to find policy/role creation events)

1. Locate the audit log entry for **Pharmacy Helpdesk** custom role creation (from **Lab 01 Exercise 2 Task 6**). Select it and review the **Properties** → JSON payload showing the role's permission grants.

1. Locate the audit log entry for **Compliance - Windows Security Baseline** creation (from **Lab 02 Exercise 2 Task 1**). Note the **Initiated by** field shows your Global Admin account and the **Target** shows the compliance policy ID.

1. Locate the audit log entry for the **Pharmacy Helpdesk → Lee Gu** role assignment (just created in **Exercise 3 Task 3** of this lab). Confirm the assignment payload includes the **Pharmacy** scope tag and the **dyn-Windows-Devices** group.

1. Locate the audit log entry where you **deleted** `WIN - Camera - Enabled (Pilot)` to resolve the conflict in **Lab 02 Exercise 6 Task 2**. The activity will be **Delete deviceConfiguration**. The Properties pane includes the deleted object's last-known state — useful for rollback decisions.

1. Switch to the **Microsoft Entra admin center** at **https://entra.microsoft.com**. Navigate to **Identity** → **Monitoring & health** → **Audit logs** (the Entra audit log, distinct from Intune's).

1. Filter the Entra audit log:
   - **Service:** **Conditional Access**
   - **Date:** Last 7 days

1. Locate the entry where you **switched** `CA - Require compliant device (Pharmacy pilot)` from **Report-only** to **On** (from **Lab 04 Exercise 6 Task 3**). The Properties show the policy's state change.

   > [!NOTE]
   > **Two separate audit logs.** Intune-specific actions (compliance, configuration, app, RBAC, scope tag) live in the **Intune audit log** under **Tenant administration**. Conditional Access policies, Entra role assignments, and directory operations live in the **Entra audit log** under **Identity → Monitoring & health**. When you investigate a real incident, you usually need both.

**You have successfully traced operations across both Intune and Entra audit logs.**

---

**Previous:** [← Exercise 3: Assign and verify the Pharmacy Helpdesk delegated role end-to-end](exercise-3.md) | **Next:** [→ Exercise 5: Use built-in reports](exercise-5.md)

# Lab 05, Exercise 5: Use built-in reports

### Scenario

Intune provides built-in reports for devices, compliance, configuration, applications, and more. You'll generate and export reports for operational insights.

### Task 1: Generate a device compliance report

1. In the **Microsoft Intune admin center**, navigate to **Reports** → **Device compliance**.

1. Select **Noncompliant devices** report.

1. Select **Generate report** (or **Run report** if previously generated).

1. Review the report data:
   - **Device name**
   - **User principal name**
   - **Compliance state**
   - **Last check-in**
   - **Operating system**

1. Use the **Filter** option to narrow results (e.g., filter by OS = Windows).

1. Select **Export** to download the report as CSV.

**You have successfully generated and exported a device compliance report.**

---

### Task 2: Generate a device configuration report

1. In the **Microsoft Intune admin center**, navigate to **Reports** → **Device configuration**.

1. Select **Assignment status** report.

1. Select **Generate report**.

1. Review the report data:
   - **Policy name**
   - **Assigned devices**
   - **Succeeded**
   - **Failed**
   - **Pending**

1. Select a policy to drill down into per-device status.

**You have successfully generated a device configuration report.**

---

### Task 3: Review the Tenant status dashboard

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Tenant status**.

1. Review the **Tenant status** dashboard:
   - **Service health:** Shows active incidents or advisories affecting Intune
   - **Connector status:** Shows health of connectors (Defender for Endpoint, Microsoft Tunnel, etc.)
   - **Intune news:** Product updates and feature announcements

1. Select **Service health** to view detailed incident information.

1. Select **Message center** to view upcoming changes and feature rollouts.

**You have successfully reviewed the Tenant status dashboard.**

---

**Previous:** [← Exercise 4: Monitor audit logs and operational health](exercise-4.md) | **Next:** [Lab summary →](summary.md)

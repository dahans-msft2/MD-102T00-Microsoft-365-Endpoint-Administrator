# Lab 02, Exercise 3: Analyze Group Policy Objects

### Scenario

Contoso has existing Group Policy Objects (GPOs) from an on-premises Active Directory environment. You'll use Group Policy analytics to identify which GPO settings are supported in Intune and generate a migration report.

### Task 1: Import a Group Policy backup

1. On **CL1**, ensure the GPO backup XML files are accessible (provided in lab assets at `C:\LabAssets\GPO-Backups\`).

   > [!NOTE]
   > If the files are not present, ask your lab instructor or copy them from the lab hosting platform's file share.

1. In the **Microsoft Intune admin center**, expand **Devices**, then under **Manage devices** select **Group Policy analytics**.

   > [!NOTE]
   > Group Policy analytics is no longer flagged as **(preview)** — it's a generally available feature in the current portal.

1. Select **Import** from the top toolbar.

1. In the **Import GPO** pane, select **Browse** and navigate to `C:\LabAssets\GPO-Backups\`.

1. Select **GPO_Desktop_Settings.xml** and select **Open**.

1. Select **Import**.

1. Wait for the import to complete (typically 1–2 minutes).

1. After import, the GPO appears in the list. The **MDM support** column shows how many settings are supported, and the aggregated **Group policy migration readiness** bars at the top of the page summarize **Ready for migration**, **Not supported**, and **Deprecated** counts.

**You have successfully imported a Group Policy backup into Group Policy analytics.**

---

### Task 2: Review the migration readiness report

1. On the **Group Policy analytics** page, select **GPO_Desktop_Settings** from the list.

1. The detail view opens to a single settings table. Each row shows:
   - **Setting name**
   - **Setting category**
   - **Configured value**
   - **MDM support** (the CSP equivalent if Intune supports the setting)
   - **Migration readiness** — one of **Supported**, **Unsupported**, or **Deprecated**

1. Select a setting with **Supported** status to view the recommended Intune configuration.

   Example: If the GPO configured "Prevent access to registry editing tools":
   - **Intune equivalent:** Device Configuration → Templates → Device Restrictions → General → Registry editing

1. Select a setting with **Unsupported** or **Deprecated** status to view the reason and any workarounds.

   > [!NOTE]
   > Group Policy analytics helps you plan GPO-to-Intune migrations by identifying which settings can be directly migrated vs. which require alternative approaches (custom scripts, third-party tools, or re-architecting).

**You have successfully reviewed a Group Policy migration readiness report.**

---

### Task 3: Export the analysis results

1. On the **Group Policy analytics** list page, select the **GPO_Desktop_Settings** row, then select **Export** from the top toolbar.

1. The download starts immediately as a CSV file. Save it to `C:\LabAssets\GPO-Analysis-Results.csv`.

1. Open the CSV file in **Excel** or **Notepad** to review the exported data.

   The CSV contains:
   - Setting name
   - Setting category
   - Configured value
   - Migration readiness status
   - Intune equivalent (if available)

**You have successfully exported Group Policy analysis results.**

---

**Previous:** [← Exercise 2: Configure compliance policies](exercise-2.md) | **Next:** [→ Exercise 4: Configure Windows Update management](exercise-4.md)

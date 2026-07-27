# Lab 02, Exercise 3: Analyze Group Policy Objects

### Scenario

Contoso has existing Group Policy Objects (GPOs) from an on-premises Active Directory environment. You'll use Group Policy analytics to identify which GPO settings are supported in Intune and generate a migration report.

### Task 1: Import a Group Policy backup

1. On **SEA-DEV1**, ensure the GPO backup XML files are accessible (provided in lab assets at `C:\LabAssets\GPO-Backups\`).

   > [!NOTE]
   > If the files are not present, ask your lab instructor or copy them from the lab hosting platform's file share.

1. In the **Microsoft Intune admin center**, expand **Devices**, then under **Manage devices** select **Group Policy analytics**.

   > [!NOTE]
   > Group Policy analytics is no longer flagged as **(preview)** — it's a generally available feature in the current portal.

1. Select **Import** from the top toolbar.

1. In the **Import GPO** pane, select **Browse** and navigate to `C:\LabAssets\GPO-Backups\`.

1. Select **GPO_Desktop_Settings.xml** and select **Open**.

1. Select **Next**.

1. On the **Scope tags** page, leave the **Default** scope tag (don't add Pharmacy here — this GPO analysis isn't part of the Pharmacy Helpdesk delegation thread used later in Lab 05). Select **Next**.

   > [!NOTE]
   > If you don't select a scope tag here, Default is applied automatically. Only admins scoped to whichever tag(s) you pick can see this imported GPO in the analytics list — leaving Default means any admin with Default scope (essentially everyone without a narrower custom role) can see it.

1. On the **Review + create** page, select **Create**.

1. Wait for the import to complete (typically 1–2 minutes).

1. After import, the GPO appears in the list. The **MDM support** column shows how many settings are supported, and the aggregated **Group policy migration readiness** bars at the top of the page summarize **Ready for migration**, **Not supported**, and **Deprecated** counts.

**You have successfully imported a Group Policy backup into Group Policy analytics.**

---

### Task 2: Review the migration readiness report and migrate supported settings

1. On the **Group Policy analytics** page, select **GPO_Desktop_Settings** from the list.

1. The **Settings** tab opens to a table with one row per setting. Review the columns:
   - **Setting name** and **Group policy setting category**
   - **MDM support** — a green **Yes** or amber **No** icon (not a clickable drill-down; the row itself carries no extra detail beyond these columns)
   - **Value**, **Scope** (User/Device), **Min OS version**, **CSP name**, and **CSP mapping** (the OMA-URI, shown only for **Yes** rows)

   > [!NOTE]
   > There's no per-setting detail panel or "view recommended configuration" page — everything Group Policy analytics knows about a setting is already in this row. For `GPO_Desktop_Settings`, two settings show **Yes**: **Remove Run menu from Start Menu** and **Prevent changes to Taskbar and Start Menu Settings** (both map to `Policy` CSP settings). The rest show **No** — they're either not exposed to any MDM provider or fall outside the supported CSP list (Policy, PassportForWork, BitLocker, Firewall, AppLocker, Group Policy Preferences).

1. Select **Back** to return to the **Group Policy analytics** list.

1. Select the checkbox next to **GPO_Desktop_Settings**, then select **Migrate** from the toolbar.

1. On the **Settings to migrate** tab, select the **Migrate** checkbox for the two supported settings only:
   - **Remove Run menu from Start Menu**
   - **Prevent changes to Taskbar and Start Menu Settings**

   Leave the **No**-support settings unchecked — migrating them wouldn't produce a working setting anyway. Select **Next**.

1. On the **Configuration** page, review the imported values (carried over from the GPO), then select **Next**.

1. On the **Profile info** page, enter:
   - **Name:** `Migrated - GPO Desktop Settings`
   - **Description:** `Settings Catalog profile migrated from the on-premises GPO_Desktop_Settings GPO`

1. Select **Next**.

1. On the **Scope tags** page, select **+ Select scope tags**, add **Pharmacy**, and select **Select**. Then select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**, search for and select **dyn-Windows-Devices**, then select **Select** and **Next**.

1. On the **Review + deploy** page, review the settings and select **Create**.

   > [!NOTE]
   > Group Policy analytics helps you plan GPO-to-Intune migrations by identifying which settings can be directly migrated vs. which require alternative approaches (custom scripts, third-party tools, or re-architecting). The **Migrate** feature is best-effort — some settings translate to a similar-but-not-identical Settings Catalog equivalent, and AppLocker/Firewall GPO settings disable **Migrate** entirely since those are configured through Endpoint Security instead.

**You have successfully reviewed a Group Policy migration readiness report and migrated the supported settings to a new Settings Catalog profile.**

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

# Lab 04, Exercise 2: Deploy endpoint security policies

### Scenario

Endpoint security policies provide targeted security controls without the complexity of full configuration profiles. You'll deploy the Microsoft Defender security baseline, antivirus policies, firewall policies, and attack surface reduction rules.

### Task 1: Deploy the Microsoft Defender security baseline

Security baselines are pre-configured collections of recommended settings based on Microsoft security guidance.

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Security baselines**.

1. Select **Microsoft Defender for Endpoint Baseline** from the list.

1. Select **Create profile**.

1. On the **Basics** page, enter:
   - **Name:** `Security Baseline - Defender for Endpoint`
   - **Description:** `Microsoft-recommended security settings for Defender for Endpoint`

1. Select **Next**.

1. On the **Configuration settings** page, review the default settings.

   > [!NOTE]
   > The baseline includes settings for:
   > - BitLocker encryption
   > - Credential Guard
   > - Application Guard
   > - Attack Surface Reduction rules
   > - Exploit protection
   > - Network protection

1. Scroll through the categories and note the pre-configured values. You can customize individual settings, but for this lab, accept the defaults.

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** (created in **Lab 01 Exercise 2 Task 6**) and select **Next**.

1. On the **Assignments** page, under **Assign to**, select **Add groups**.

1. Search for and select **dyn-Windows-Devices**.

1. Select **Select**.

1. Select **Next**.

1. On the **Review + create** page, select **Create**.

**You have successfully deployed the Microsoft Defender security baseline.**

---

### Task 2: Create an Antivirus policy

Antivirus policies configure Microsoft Defender Antivirus settings, including real-time protection, cloud protection, and scanning behavior.

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Antivirus**.

1. Select **Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10, Windows 11, and Windows Server
   - **Profile:** Microsoft Defender Antivirus

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Antivirus - Defender Configuration`
   - **Description:** `Configures real-time protection, cloud protection, and scan settings`

1. Select **Next**.

1. On the **Configuration settings** page, expand **Defender** and configure:
   - **Allow Real Time Monitoring:** Allowed
   - **Allow Behavior Monitoring:** Allowed
   - **Allow Intrusion Prevention System:** Allowed
   - **Allow IO AV Protection:** Allowed
   - **Allow On Access Protection:** Allowed
   - **Allow Scanning Network Files:** Allowed
   - **Allow Cloud Protection:** Allowed
   - **Cloud Block Level:** High
   - **Cloud Extended Timeout:** 50 seconds
   - **Submit Samples Consent:** Send all samples automatically

1. Expand **Scans** and configure:
   - **Scan Type:** Quick scan
   - **Schedule Scan Day:** Every day
   - **Schedule Scan Time:** 2:00 AM
   - **Scan Archive Files:** Allowed
   - **Scan Removable Drives During Full Scan:** Allowed

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**.

1. On the **Assignments** page, assign to **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

> [!IMPORTANT]
> **Endpoint security policy precedence.** You just deployed the Defender security baseline (Task 1) AND a standalone Antivirus policy (Task 2). Both touch some of the same Defender Antivirus settings (real-time monitoring, cloud protection). Intune resolves overlapping endpoint-security settings using policy **priority** — the more recently created or higher-priority policy wins per setting, and any unresolvable conflict surfaces in **Endpoint security** → **All devices** with a **Conflict** state. In production, choose one source of truth per setting category: either let the baseline own it, or strip the setting out of the baseline and use a standalone policy.

**You have successfully created an Antivirus policy.**

---

### Task 3: Create a Firewall policy

Firewall policies configure Windows Defender Firewall rules and behavior.

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Firewall**.

1. Select **Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10, Windows 11, and Windows Server
   - **Profile:** Microsoft Defender Firewall

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Firewall - Defender Configuration`
   - **Description:** `Enables firewall for all network profiles and configures logging`

1. Select **Next**.

1. On the **Configuration settings** page, expand **Domain Profile** and configure:
   - **Enable Firewall:** Yes
   - **Enable Stealth Mode:** Yes
   - **Enable Log Success Connections:** Yes
   - **Enable Log Dropped Packets:** Yes

1. Expand **Private Profile** and configure the same settings as Domain Profile.

1. Expand **Public Profile** and configure:
   - **Enable Firewall:** Yes
   - **Enable Stealth Mode:** Yes
   - **Block Inbound Connections:** Yes (more restrictive for public networks)
   - **Enable Log Success Connections:** Yes
   - **Enable Log Dropped Packets:** Yes

1. Select **Next**.

1. On the **Assignments** page, assign to **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

**You have successfully created a Firewall policy.**

---

### Task 4: Create an Attack Surface Reduction (ASR) policy with split pilot/audit assignment

Attack Surface Reduction rules block behaviors commonly used by malware, such as launching executables from Office documents or running obfuscated scripts. The upper-intermediate ASR rollout pattern is to enable rules in **Block** mode on the pilot cohort while keeping them in **Audit** mode for everyone else — you get real enforcement on a small group to surface false positives early, while the rest of the fleet generates Audit logs you can use to predict broad-rollout impact. You'll do that here by creating two policies with the same rules but different modes, assigned to different groups.

#### Policy 1 — ASR Block mode for the pilot cohort

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Attack surface reduction**.

1. Select **Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10, Windows 11, and Windows Server
   - **Profile:** Attack surface reduction rules

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `ASR - Block (Pilot)`
   - **Description:** `ASR rules in Block mode for pilot cohort — real enforcement on a small group`

1. Select **Next**.

1. On the **Configuration settings** page, configure the following ASR rules **all in Block mode**:

   - **Block executable content from email client and webmail:** Block
   - **Block all Office applications from creating child processes:** Block
   - **Block Office applications from creating executable content:** Block
   - **Block Office applications from injecting code into other processes:** Block
   - **Block JavaScript or VBScript from launching downloaded executable content:** Block
   - **Block execution of potentially obfuscated scripts:** Block
   - **Block Win32 API calls from Office macros:** Block
   - **Block credential stealing from the Windows local security authority subsystem (lsass.exe):** Block
   - **Block process creations originating from PSExec and WMI commands:** Block
   - **Block untrusted and unsigned processes that run from USB:** Block
   - **Block persistence through WMI event subscription:** Block

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**.

1. On the **Assignments** page, assign to **sg-Intune-Pilot-Users** (the pilot cohort from **Lab 01 Exercise 1**).

1. Select **Next** → **Create**.

#### Policy 2 — ASR Audit mode for the broader fleet

1. On the **Attack surface reduction** page, select **Create Policy** again.

1. **Platform:** Windows 10, Windows 11, and Windows Server. **Profile:** Attack surface reduction rules. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `ASR - Audit (Fleet)`
   - **Description:** `Same ASR rules in Audit mode for the broader fleet — generates Audit logs without enforcement`

1. Select **Next**.

1. On the **Configuration settings** page, configure the **same ASR rules listed above**, but set each one to **Audit mode** instead of **Block mode**. (One exception: keep `Block credential stealing from lsass.exe` in **Block mode** — it's the lowest false-positive rate ASR rule and worth enforcing fleet-wide on day one.)

1. Select **Next**.

1. On the **Scope tags** page, leave the **Default** scope tag (this is fleet-wide). Select **Next**.

1. On the **Assignments** page, assign to **dyn-Windows-Devices**. Under **Exclude groups**, add **sg-Intune-Pilot-Users** (so pilot members only get the Block policy, not both).

1. Select **Next** → **Create**.

> [!NOTE]
> The split-mode pattern (Block on pilot, Audit on everyone else) is the canonical ASR rollout. Watch **Reports** → **Endpoint security** → **Attack surface reduction rules** for a week or two; when the Audit log shows the rules would have fired only on legitimate threats (no false positives in the broader fleet), flip the Audit policy to Block.

**You have successfully created split-assignment ASR policies for pilot Block and fleet Audit.**

---

**Previous:** [← Exercise 1: Integrate Microsoft Defender for Endpoint](exercise-1.md) | **Next:** [→ Exercise 3: Configure BitLocker encryption](exercise-3.md)

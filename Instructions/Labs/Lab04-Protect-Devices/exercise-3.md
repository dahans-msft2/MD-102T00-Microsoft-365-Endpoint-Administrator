# Lab 04, Exercise 3: Configure BitLocker encryption

### Scenario

BitLocker encrypts the entire OS drive, protecting data at rest. You'll configure a BitLocker policy that requires TPM+PIN protection and escrows recovery keys to Microsoft Entra ID.

### Task 1: Create a BitLocker policy

1. In the **Microsoft Intune admin center**, navigate to **Endpoint security** → **Disk encryption**.

1. Select **Create Policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile:** BitLocker

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `BitLocker - Full Disk Encryption`
   - **Description:** `Requires BitLocker encryption with TPM and PIN, recovery keys escrowed to Entra ID`

1. Select **Next**.

1. On the **Configuration settings** page, expand **BitLocker – Base Settings** and configure:
   - **Require storage cards to be encrypted (mobile only):** Not configured
   - **Enable full disk encryption for OS and fixed data drives:** Yes
   - **Hide prompt about third-party encryption:** Yes

1. Expand **BitLocker - Fixed Drive Settings** and configure:
   - **BitLocker fixed drive policy:** Enable
   - **Fixed drive recovery:** Configure recovery options
   - **Configure storage of recovery information to Microsoft Entra ID:** Required
   - **Store recovery information in Microsoft Entra ID before enabling BitLocker:** Require

1. Expand **BitLocker – OS Drive Settings** and configure:
   - **BitLocker system drive policy:** Enable
   - **Startup authentication required:** Yes
   - **Compatible TPM startup:** Required
   - **Compatible TPM startup PIN:** Required
   - **Compatible TPM startup key:** Not allowed
   - **Compatible TPM startup key and PIN:** Not allowed
   - **Require additional authentication at startup:** Allow
   - **Configure PCR validation profile for UEFI firmware configurations:** Configure
   - **Minimum PIN length:** 6
   - **System drive recovery:** Configure recovery options
   - **Configure storage of recovery information to Microsoft Entra ID:** Required
   - **Store recovery information in Microsoft Entra ID before enabling BitLocker:** Require

   > [!NOTE]
   > Requiring TPM+PIN provides two-factor protection: something you have (TPM chip) + something you know (PIN). Recovery keys escrowed to Entra ID allow IT admins to retrieve keys when users forget their PIN.

1. Select **Next**.

1. On the **Scope tags** page, add **Pharmacy** and select **Next**. BitLocker on Pharmacy clinical workstations is a HIPAA control \u2014 keeping the policy under the `Pharmacy` scope tag means the Pharmacy Helpdesk (assigned in **Lab 05 Exercise 3**) can see and audit it.

1. On the **Assignments** page, assign to **dyn-Windows-Devices**.

1. Select **Next** \u2192 **Create**.

**You have successfully created a BitLocker encryption policy.**

---

### Task 2: Monitor BitLocker encryption status

1. On **CL1**, wait 10–15 minutes for the BitLocker policy to apply.

   > [!NOTE]
   > BitLocker encryption can take 1–3 hours to complete depending on drive size and system performance. For lab purposes, you'll verify the policy was applied and encryption started.

1. On **CL1**, open **Windows Terminal (Admin)**.

1. Check BitLocker status:

   ```powershell
   manage-bde -status C:
   ```

1. Review the output:
   - **Conversion Status:** Should show "Encryption in Progress" or "Fully Encrypted"
   - **Encryption Method:** XTS-AES 128 or XTS-AES 256
   - **Protection Status:** Protection On
   - **Lock Status:** Unlocked

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **All devices** → **CL1**.

1. Select **Recovery keys** from the left navigation.

1. Verify the BitLocker recovery key for the C: drive is escrowed to Microsoft Entra ID.

   > [!NOTE]
   > Recovery keys are stored in Entra ID and can be retrieved by Global Administrators or Helpdesk Administrators when a user forgets their BitLocker PIN.

**You have successfully monitored BitLocker encryption status and verified recovery key escrow.**

---

### Task 3: Retrieve a BitLocker recovery key

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **All devices** → **CL1**.

1. Select **Recovery keys** from the left navigation.

1. Locate the recovery key for the **C:** drive.

1. Select **Show recovery key** (if prompted, confirm with MFA or re-authenticate).

1. The recovery key is displayed in the following format:
   ```
   123456-789012-345678-901234-567890-123456-789012-345678
   ```

   > [!NOTE]
   > This key can be used to unlock the drive if the TPM fails or the user forgets their PIN. In a production environment, only authorized help desk staff should have access to recovery keys.

**You have successfully retrieved a BitLocker recovery key from Microsoft Entra ID.**

---

**Previous:** [← Exercise 2: Deploy endpoint security policies](exercise-2.md) | **Next:** [→ Exercise 4: Deploy Microsoft Tunnel Gateway](exercise-4.md)

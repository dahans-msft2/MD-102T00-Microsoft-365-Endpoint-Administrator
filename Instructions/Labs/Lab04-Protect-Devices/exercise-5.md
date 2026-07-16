# Lab 04, Exercise 5: Implement Microsoft Cloud PKI

### Scenario

Microsoft Cloud PKI (part of the Intune Suite) provides a cloud-hosted certificate authority for issuing certificates to devices and users. You'll create a root CA, an issuing CA anchored to it, and a SCEP certificate profile for device authentication (e.g., for Wi-Fi, VPN, or S/MIME encryption). With the Suite trial active (from **Lab 01** prerequisites), this exercise is fully hands-on.

### Task 1: Create a root Certificate Authority

The root CA is the trust anchor for your Cloud PKI hierarchy. You must create at least one root CA before you can create an issuing CA.

1. In the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Cloud PKI**.

1. Select **+ Create** from the top toolbar.

   > [!NOTE]
   > **+ Create** opens the **Create certification authority** wizard directly. There's no dropdown menu choice between "Root CA" and "Issuing CA" — you pick the **CA type** on the **Configuration settings** tab inside the wizard.

1. On the **Basics** tab, enter:
   - **Name:** `Contoso Root CA`
   - **Description:** `Microsoft Cloud PKI root CA for Contoso Healthcare`

1. Select **Next** to continue to **Configuration settings**.

1. On the **Configuration settings** tab, configure:
   - **CA type:** **Root CA**
   - **Validity period:** **25 years** (allowed values: 5, 10, 15, 20, or 25)

1. Under **Extended Key Usages**, choose how the CA can be used. For this lab, leave **Client Authentication (1.3.6.1.5.5.7.3.2)** and **Server Authentication (1.3.6.1.5.5.7.3.1)** selected (the common defaults for SCEP-issued device certificates).

   > [!IMPORTANT]
   > Root CA EKU constraints are a **superset** of the issuing CA. Any EKU you want on a downstream issuing CA must be defined here on the root first. The **Any Purpose (2.5.29.37.0)** EKU is intentionally absent — it's overly permissive and a security risk.

1. Under **Subject attributes**, enter:
   - **Common name (CN):** `Contoso Root Certificate Authority`
   - **Organization (O):** `Contoso Healthcare`
   - **Country (C):** `US` (Intune enforces a two-character limit per PKI standards)

1. Under **Encryption**, set **Key size and algorithm** to **RSA-4096 and SHA-512** (the strongest available; this is the upper bound that downstream issuing CAs and SCEP profiles can use).

1. Select **Next** to continue to **Scope tags**.

1. On the **Scope tags** tab, leave the **Default** scope tag (Cloud PKI infrastructure is typically tenant-wide). Select **Next**.

1. On the **Review + create** tab, review the summary. CA properties **can't be edited after creation** — if anything's wrong, select **Back** now.

1. Select **Create**.

1. Wait for the root CA to provision (typically 2–3 minutes). Select **Refresh** on the Cloud PKI list to see it appear with **Status: Active** and **Type: Root**.

**You have successfully created a cloud-hosted root Certificate Authority.**

---

### Task 2: Create an issuing Certificate Authority

Issuing CAs are subordinate to a root CA and they're what your devices actually request certificates from (via the SCEP service Cloud PKI provides automatically).

1. On the **Cloud PKI** page, select **+ Create** again.

1. On the **Basics** tab, enter:
   - **Name:** `Contoso Issuing CA`
   - **Description:** `Microsoft Cloud PKI issuing CA anchored to Contoso Root CA`

1. Select **Next**.

1. On the **Configuration settings** tab, configure:
   - **CA type:** **Issuing CA**
   - **Root CA source:** **Intune** (use a root CA you created in this tenant)
   - **Root CA:** Select **Contoso Root CA** (the root you created in Task 1)
   - **Validity period:** **10 years** (allowed: 2, 4, 6, 8, or 10 — must be less than or equal to the root CA's remaining lifetime)

1. Under **Extended Key Usages**, the picker is constrained to EKUs you defined on the root in Task 1. Confirm **Client Authentication** and **Server Authentication** are selected.

1. Under **Subject attributes**, enter:
   - **Common name (CN):** `Contoso Issuing Certificate Authority`
   - **Organization (O):** `Contoso Healthcare`
   - **Country (C):** `US`

1. Under **Encryption**, set **Key size and algorithm** to **RSA-2048 and SHA-256** (sufficient for SCEP leaf certificates; smaller key = faster TLS handshakes on devices).

1. Select **Next** → **Scope tags** (leave Default) → **Next** → **Review + create**.

1. Select **Create**. Provisioning takes 2–3 minutes while the root CA signs the issuing CA's certificate.

**You have successfully created an issuing Certificate Authority.**

---

### Task 3: Download the root and issuing CA certificates

1. On the **Cloud PKI** page, select **Contoso Root CA** from the list.

1. Select **Download certificate** and save the file as `ContosRootCA.cer`.

1. Return to the **Cloud PKI** page and select **Contoso Issuing CA**.

1. Select **Download certificate** and save the file as `ContosoIssuingCA.cer`.

   > [!NOTE]
   > These certificates will be deployed to devices as trusted roots, allowing them to trust certificates issued by the Cloud PKI infrastructure.

**You have successfully downloaded the root and issuing CA certificates.**

---

### Task 4: Create a trusted certificate profile

Trusted certificate profiles deploy root and intermediate CA certificates to devices.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Configuration profiles**.

1. Select **Create** → **New policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Templates → Trusted certificate

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `Trusted Cert - Contoso Root CA`
   - **Description:** `Deploys the Contoso Root CA certificate to the Trusted Root store`

1. Select **Next**.

1. On the **Configuration settings** page, configure:
   - **Certificate file:** Browse and select `ContosoRootCA.cer`
   - **Destination store:** Computer certificate store - Root

1. Select **Next**.

1. On the **Assignments** page, assign to **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

1. Repeat steps 1–11 to create a second trusted certificate profile for the issuing CA:
   - **Name:** `Trusted Cert - Contoso Issuing CA`
   - **Certificate file:** `ContosoIssuingCA.cer`
   - **Destination store:** Computer certificate store - Intermediate Certification Authorities

**You have successfully created trusted certificate profiles to deploy the CA chain.**

---

### Task 5: Create a SCEP certificate profile

SCEP (Simple Certificate Enrollment Protocol) profiles allow devices to request certificates from the Cloud PKI issuing CA.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Configuration profiles**.

1. Select **Create** → **New policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** Windows 10 and later
   - **Profile type:** Templates → SCEP certificate

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `SCEP - Device Authentication`
   - **Description:** `Issues device authentication certificates from Cloud PKI`

1. Select **Next**.

1. On the **Configuration settings** page, configure:
   - **Certificate type:** Device
   - **Subject name format:** Common name
   - **Subject alternative name:** DNS = `{{DeviceName}}.contoso.com`
   - **Certificate validity period:** 1 year
   - **Key storage provider (KSP):** Enroll to Trusted Platform Module (TPM) KSP
   - **Key usage:** Digital signature, Key encipherment
   - **Key size (bits):** 2048
   - **Hash algorithm:** SHA-2
   - **Root Certificate:** Select **Trusted Cert - Contoso Root CA**
   - **Extended key usage:** Client Authentication (1.3.6.1.5.5.7.3.2)
   - **Renewal threshold (%):** 20
   - **SCEP Server URLs:** (Auto-populated by Cloud PKI integration)
   - **Certificate authority:** Select **Contoso Issuing CA**

1. Select **Next**.

1. On the **Assignments** page, assign to **dyn-Windows-Devices**.

1. Select **Next** → **Create**.

**You have successfully created a SCEP certificate profile for device authentication.**

---

### Task 6: Verify certificate enrollment on CL1

1. On **CL1**, wait 10–15 minutes for the SCEP profile to apply and the certificate to be issued.

1. Open **Windows Terminal (Admin)** and run:

   ```powershell
   Get-ChildItem -Path Cert:\LocalMachine\My
   ```

1. Verify a certificate issued by **Contoso Issuing CA** is present with:
   - **Subject:** CN=CL1.contoso.com (or similar)
   - **Enhanced Key Usage:** Client Authentication

1. Open **Microsoft Management Console** (`mmc.exe`).

1. Add the **Certificates** snap-in (Computer account → Local computer).

1. Navigate to **Certificates (Local Computer)** → **Personal** → **Certificates**.

1. Verify the device authentication certificate is present and valid.

**You have successfully verified certificate enrollment using Microsoft Cloud PKI.**

---

**Previous:** [← Exercise 4: Deploy Microsoft Tunnel Gateway](exercise-4.md) | **Next:** [→ Exercise 6: Monitor security posture and compliance](exercise-6.md)

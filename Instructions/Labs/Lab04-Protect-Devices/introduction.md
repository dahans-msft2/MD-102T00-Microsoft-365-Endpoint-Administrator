---
lab:
  title: 'Lab 04: Protect devices'
  description: 'In this lab, you integrate Microsoft Defender for Endpoint, deploy endpoint security and BitLocker encryption policies, configure Microsoft Tunnel Gateway, and implement Microsoft Cloud PKI for certificate-based authentication.'
  duration: 110 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune
    - Microsoft Defender for Endpoint
    - Windows
---

# Lab 04: Protect devices

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With devices enrolled and applications deployed, you now need to implement comprehensive security controls. You'll integrate Microsoft Defender for Endpoint for EDR capabilities, deploy endpoint security policies (antivirus, firewall, attack surface reduction), configure BitLocker encryption with Microsoft Entra key escrow, deploy Microsoft Tunnel Gateway for secure VPN access, and implement Microsoft Cloud PKI for certificate-based authentication.

By the end of this lab, you'll have:
- Enabled Microsoft Defender for Endpoint integration with Intune
- Onboarded Windows devices to Defender for Endpoint using EDR policies
- Deployed Microsoft Defender security baselines (tagged with the `Pharmacy` scope tag)
- Configured Antivirus, Firewall, and Attack Surface Reduction policies — with ASR split-assigned in **Block** mode to the pilot cohort and **Audit** mode to the broader fleet
- Created BitLocker encryption policies with Microsoft Entra recovery key escrow (tagged `Pharmacy`)
- Deployed Microsoft Tunnel Gateway on an Ubuntu server
- Created VPN profiles for Microsoft Tunnel connectivity
- Implemented Microsoft Cloud PKI with root and issuing CAs
- Created and deployed SCEP certificate profiles for device authentication
- Switched the Conditional Access policy from **Report-only** to **On** after verifying its impact

---

## Lab Duration

**Estimated Time:** 110 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled)
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- **Microsoft 365 E5** licensing (includes Defender for Endpoint P2)
- **Microsoft Intune Suite trial active** (activated in **Lab 01** prerequisites) — required for Cloud PKI (Exercise 5). Microsoft Tunnel (Exercise 4) is included in Intune Plan 1 and doesn't require the Suite, but it does require the **LX1** Ubuntu server
- Global Administrator or Intune Administrator credentials
- **CL1** and **CL2** (enrolled Windows 11 devices)
- **LX1** (Ubuntu 22.04 server for Microsoft Tunnel Gateway)

---

## Exercises in this lab

1. [Exercise 1: Integrate Microsoft Defender for Endpoint](exercise-1.md)
2. [Exercise 2: Deploy endpoint security policies](exercise-2.md)
3. [Exercise 3: Configure BitLocker encryption](exercise-3.md)
4. [Exercise 4: Deploy Microsoft Tunnel Gateway](exercise-4.md)
5. [Exercise 5: Implement Microsoft Cloud PKI](exercise-5.md)
6. [Exercise 6: Monitor security posture and compliance](exercise-6.md)
7. [Lab summary](summary.md)

---

**Next:** [→ Exercise 1: Integrate Microsoft Defender for Endpoint](exercise-1.md)

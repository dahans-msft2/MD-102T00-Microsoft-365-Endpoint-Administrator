# Lab 04: Protect devices — Summary

Congratulations! You've completed Lab 04: Protect devices.

In this lab, you accomplished the following:

**Exercise 1: Integrate Microsoft Defender for Endpoint**
- Enabled the Intune-to-Defender connector
- Created an EDR policy to onboard devices to Defender for Endpoint
- Verified device onboarding in the Microsoft Defender portal

**Exercise 2: Deploy endpoint security policies**
- Deployed the Microsoft Defender security baseline (tagged `Pharmacy`)
- Created Antivirus and Firewall policies (Antivirus tagged `Pharmacy`)
- Created split-assignment ASR policies: Block mode on the pilot cohort, Audit mode on the broader fleet
- Observed endpoint security policy precedence and conflict surfacing

**Exercise 3: Configure BitLocker encryption**
- Created a BitLocker policy requiring TPM+PIN protection (tagged `Pharmacy`)
- Configured recovery key escrow to Microsoft Entra ID
- Verified encryption status and retrieved recovery keys

**Exercise 4: Deploy Microsoft Tunnel Gateway**
- Installed Microsoft Tunnel Gateway on an Ubuntu server
- Registered the Tunnel Gateway in Intune
- Created a VPN profile for mobile device secure access

**Exercise 5: Implement Microsoft Cloud PKI**
- Created a root Certificate Authority and issuing CA in Cloud PKI
- Deployed trusted certificate profiles to establish the CA chain
- Created a SCEP certificate profile for device authentication
- Verified certificate enrollment on managed devices

**Exercise 6: Monitor security posture and compliance**
- Reviewed the Microsoft Defender Secure Score and improvement actions
- Reviewed threat detections and alerts in the Microsoft Defender portal
- Switched the `CA - Require compliant device (Pharmacy pilot)` policy from **Report-only** to **On** after a What If rehearsal

**Key Takeaways:**
- Microsoft Defender for Endpoint provides EDR, threat protection, and automated investigation for enrolled devices
- Endpoint security policies provide targeted controls for antivirus, firewall, and exploit mitigation; overlapping settings across baselines and standalone policies resolve via priority, with unresolvable conflicts surfaced in the portal
- Security baselines implement Microsoft-recommended settings in a single policy
- The canonical ASR rollout is **Block on pilot, Audit on fleet** — enforce on a small group while predicting broader impact via Audit logs
- BitLocker with Entra ID key escrow protects data at rest and enables IT recovery
- Microsoft Tunnel provides secure VPN access for mobile devices without traditional VPN infrastructure
- Microsoft Cloud PKI eliminates the need for on-premises PKI infrastructure while providing certificate-based authentication
- The Microsoft Defender portal consolidates security monitoring, scoring, and incident response
- Flipping a Conditional Access policy from **Report-only** to **On** is a deliberate two-step process: rehearse with **What If**, verify the break-glass exclusion, then switch

**Next Steps:**
In Lab 05, you'll automate endpoint management using Microsoft Graph PowerShell, deploy proactive remediations, configure RBAC with scope tags, and use reporting and monitoring tools.

---

**END OF LAB**

---

**Previous:** [← Exercise 6: Monitor security posture and compliance](exercise-6.md)

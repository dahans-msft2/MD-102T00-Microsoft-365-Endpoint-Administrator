# Lab 06: Extend capabilities — Summary

Congratulations! You've completed Lab 06: Extend capabilities — the final lab in the MD-102 series.

In this lab, you accomplished the following:

**Exercise 1: Configure Endpoint Privilege Management (EPM)**
- Enabled Endpoint Privilege Management in tenant settings
- Created an elevation settings policy defining default elevation behavior
- Created automatic, user-confirmed, and support-approved elevation rules — all targeted to the pilot cohort first
- Tested EPM elevation scenarios on a standard user device
- Monitored elevation reports for audit and compliance
- Established the pilot → fleet expansion plan for EPM rollout

**Exercise 2: Deploy Remote Help**
- Enabled Remote Help and assigned licenses to helpers and sharers
- Deployed the Remote Help app to managed devices
- Initiated a Remote Help session and tested view-only and full control access
- Reviewed Remote Help session logs for audit purposes
- Demonstrated that the Pharmacy Helpdesk delegated admin (Lee Gu, from **Lab 05 Exercise 3**) can launch Remote Help on Pharmacy-scoped devices only — completing **Thread A (custom RBAC + scope tag delegation)** end-to-end across all six labs

**Exercise 3: Use Advanced Analytics and Device Query**
- Reviewed Advanced Analytics dashboards for anomaly detection, resource performance, and battery health
- Ran live single-device KQL queries via Device Query (CPU info, BitLocker status verification, OS version)
- Ran multi-device KQL queries to find unencrypted devices and devices below the 24H2 feature-update target
- Built a Microsoft Entra security group (`sg-Devices-Unencrypted`) directly from a Device Query result set

**Exercise 4: Explore Windows 365 Cloud PC provisioning**
- Reviewed the Windows 365 provisioning policy workflow
- Understood how Cloud PCs are automatically provisioned and managed in Intune

**Exercise 5: Explore Azure Virtual Desktop session host enrollment**
- Understood AVD architecture and session host enrollment
- Reviewed how AVD session hosts are managed in Intune with user-based and device-based policies

**Key Takeaways:**
- Endpoint Privilege Management allows granular control of application elevation without granting full administrator rights; pilot-first rollout (same cohort as ESP, update ring, ASR) limits blast radius
- Remote Help provides secure, audited remote assistance with session logging for compliance
- Scope tags on a custom role apply to remote-task operations including Remote Help — the Pharmacy Helpdesk physically cannot initiate Remote Help on devices outside the Pharmacy scope
- Advanced Analytics surfaces ML-driven anomaly detection against each device's own historical baseline (not a fleet threshold); Device Query lets you ask live KQL questions of one device or the whole fleet without remote control
- The **"build a Microsoft Entra security group from query results"** pattern is the upper-intermediate move: query reality, then target policy at exactly what you found
- Windows 365 Cloud PCs are provisioned via Intune policies and managed like physical devices
- Azure Virtual Desktop session hosts enroll in Intune and receive policies for multi-session environments

**Course Completion:**
You have completed all 6 labs in the MD-102: Microsoft 365 Endpoint Administrator certification course. You are now prepared to:
- Deploy and manage Microsoft Intune in a cloud-pure environment
- Enroll devices using Microsoft Entra join and Windows Autopilot
- Configure device policies, compliance, and Windows Update management
- Deploy applications using multiple methods (Store, Win32, Microsoft 365 Apps, Enterprise App Catalog)
- Implement endpoint security with Microsoft Defender for Endpoint, BitLocker, and endpoint security policies
- Automate management with Microsoft Graph PowerShell
- Implement RBAC with scope tags for delegated administration
- Extend capabilities with Microsoft Intune Suite (EPM, Remote Help, Cloud PKI, Microsoft Tunnel)
- Support cloud-hosted desktops with Windows 365 and Azure Virtual Desktop

**Next Steps:**
- Review the MD-102 exam objectives and map your lab experience to the exam skills measured
- Practice additional scenarios in your own test tenant
- Explore the Microsoft Learn modules for MD-102 for additional conceptual knowledge
- Schedule your MD-102 certification exam when ready

Thank you for completing the MD-102 hands-on lab series!

---

**END OF LAB**

---

**Previous:** [← Exercise 5: Explore Azure Virtual Desktop session host enrollment](exercise-5.md)

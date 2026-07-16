# Lab 01: Foundation — Identity, enrollment, and Autopilot — Summary

Congratulations! You've completed Lab 01: Foundation — Identity, enrollment, and Autopilot.

In this lab, you accomplished the following:

**Exercise 1: Configure users and groups**
- Reviewed existing Contoso users and verified licensing
- Created two additional test users
- Created an assigned security group for pilot users
- Created dynamic user and device groups for policy targeting

**Exercise 2: Configure administrative delegation**
- Assigned the Intune Administrator role
- Assigned the Cloud Device Administrator role
- Created an administrative unit and scoped administrative access
- Created the `Pharmacy` Intune scope tag and the `Pharmacy Helpdesk` custom Intune role (threaded across Labs 02–06)

**Exercise 3: Configure device registration and settings**
- Configured device join settings in Microsoft Entra ID
- Added additional local administrators for Microsoft Entra joined devices
- Enabled Microsoft Entra LAPS for local administrator password management

**Exercise 4: Configure Windows enrollment policies**
- Verified automatic Intune enrollment for the tenant
- Configured the Default Enrollment Status Page to gate the first-run experience
- Created a stricter, blocking Enrollment Status Page profile for the pilot group
- Reviewed default enrollment restrictions
- Created and assigned a device limit restriction policy
- Blocked personally owned Android enrollment with a custom platform restriction

**Exercise 5: Enroll Windows devices**
- Enrolled SEA-DEV1 (as Megan Bowen) via Microsoft Entra join
- Enrolled SEA-DEV2 (as Joni Sherman) via Microsoft Entra join
- Verified both devices in Intune and dynamic group membership

**Exercise 6: Configure Windows Autopilot**
- Generated the Autopilot hardware hash for SEA-DEV3
- Uploaded the hardware hash to Intune
- Created a Windows Autopilot deployment profile
- Assigned the profile to SEA-DEV3

**Key Takeaways:**
- Microsoft Entra ID is the foundation for modern device management—devices must be joined or registered before enrolling in Intune
- Dynamic groups automate policy targeting based on user or device attributes; compound rules using `-and`/`-or` are the canonical pattern for regulatory or per-region scoping
- Microsoft Entra ID roles + administrative units delegate Entra-level permissions; Intune has a **separate** RBAC system with **custom roles + scope tags** for delegating policy and device administration
- Scope tags created on day one (Pharmacy) thread through every Intune object you create later — apply them at policy creation time to keep the delegated admin model intact
- In modern cloud-only tenants, automatic Intune enrollment is on by default; explicit MDM-scope configuration is primarily a hybrid identity and co-management concern
- The Enrollment Status Page is what shapes the user's first-run experience—use targeted, prioritized profiles to give pilot users a stricter, blocking experience and standard users a faster sign-in
- Device platform restrictions are the safety net against unauthorized platforms or ownership types (e.g., personal Android blocked, corporate Android Enterprise allowed)
- Windows Autopilot streamlines device provisioning by pre-registering devices and applying deployment profiles during OOBE

**Next Steps:**
The devices you enrolled in this lab (SEA-DEV1 and SEA-DEV2) will be used in subsequent labs to deploy configuration profiles, compliance policies, applications, and security baselines. Lab 02 focuses on managing and maintaining these devices using Intune policies.

---

**END OF LAB**

---

**Previous:** [← Exercise 6: Configure Windows Autopilot](exercise-6.md)

# Lab 03: Manage applications — Summary

Congratulations! You've completed Lab 03: Manage applications.

In this lab, you accomplished the following:

**Exercise 1: Deploy Microsoft Store apps**
- Added a Microsoft Store app (Microsoft To Do) to Intune
- Assigned the app as Required to automatically install on devices
- Verified installation on a managed device

**Exercise 2: Package and deploy a Win32 application**
- Packaged a Win32 app using the Intune Win32 Content Prep Tool
- Created a custom file-based detection rule
- Tagged the deployment with the `Pharmacy` scope tag for delegated administration
- Deployed the app to pilot users and monitored installation status

**Exercise 3: Deploy Microsoft 365 Apps**
- Configured Microsoft 365 Apps with Current Channel updates
- Assigned the suite to all Windows devices
- Monitored the large app deployment process

**Exercise 4: Use the Enterprise App Catalog**
- Browsed the Enterprise App Catalog (Intune Suite feature)
- Added Google Chrome with pre-configured settings and detection rules
- Deployed the app as Available in the Company Portal

**Exercise 5: Configure app supersedence**
- Created a newer version of an app (tagged `Pharmacy`)
- Configured a supersedence relationship to automatically replace the old version
- Verified automatic upgrade behavior on devices

**Exercise 6: Create an App Protection Policy**
- Created iOS and Android App Protection Policies
- Configured data protection controls (copy/paste restrictions, encryption, PIN requirements)
- Understood how APP enforces data protection without device enrollment

**Exercise 7: Monitor app deployment and troubleshoot failures**
- Reviewed the App overview dashboard
- Investigated failed app installations and interpreted error codes
- Exported app install status data to CSV for reporting
- Diagnosed and resolved an intentional Required vs. Uninstall app-assignment conflict

**Key Takeaways:**
- Microsoft Store apps provide modern, lightweight application deployment
- Win32 apps require packaging with the Content Prep Tool and custom detection rules
- Microsoft 365 Apps deployment includes update channel configuration for phased rollouts
- Enterprise App Catalog (Intune Suite) simplifies third-party app deployment with pre-configured installers
- App supersedence automates application upgrades without manual uninstall/reinstall
- App Protection Policies secure corporate data on mobile/BYOD devices without full enrollment
- Scope tags carry through the app surface just like configuration and compliance — tag clinical/regulated apps at create time so delegated admins (Pharmacy Helpdesk, Lab 05) can manage them
- App assignment conflicts (Required vs. Uninstall on overlapping groups) surface in **App install status**; resolve by removing the redundant intent and using audit logs (Lab 05) to find who introduced it
- Intune provides comprehensive monitoring and troubleshooting for app deployment

**Next Steps:**
In Lab 04, you'll protect devices using Microsoft Defender for Endpoint integration, endpoint security policies, BitLocker encryption, Microsoft Tunnel Gateway, and Microsoft Cloud PKI.

---

**END OF LAB**

---

**Previous:** [← Exercise 7: Monitor app deployment and troubleshoot failures](exercise-7.md)

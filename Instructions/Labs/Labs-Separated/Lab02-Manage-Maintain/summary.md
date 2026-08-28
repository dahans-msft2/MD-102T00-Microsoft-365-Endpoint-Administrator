# Lab 02: Manage and maintain devices — Summary

Congratulations! You've completed Lab 02: Manage and maintain devices.

In this lab, you accomplished the following:

**Exercise 1: Create configuration profiles**
- Created a Settings Catalog profile for power management (tagged with `Pharmacy`)
- Created a Device Restrictions profile using a built-in template (tagged with `Pharmacy`)
- Created compound and simple assignment filters and applied one in **exclude** mode
- Intentionally created two conflicting camera profiles for the pilot cohort (resolved in Exercise 6)

**Exercise 2: Configure compliance policies**
- Created a Windows compliance policy with device health and security requirements (tagged with `Pharmacy`)
- Configured grace periods and notification actions for noncompliance
- Created a Conditional Access policy (`CA - Require compliant device (Pharmacy pilot)`) in **Report-only** mode — switched to **On** in Lab 04 Exercise 6
- Monitored compliance policy results for enrolled devices

**Exercise 3: Analyze Group Policy Objects**
- Imported a Group Policy backup XML into Group Policy analytics
- Reviewed the migration readiness report to identify supported/unsupported settings
- Exported the analysis results for planning

**Exercise 4: Configure Windows Update management**
- Created a pilot update ring with no deferrals for early adopters (tagged with `Pharmacy`)
- Created a standard update ring with 7-day quality and 14-day feature update deferrals
- Created a Feature update profile pinning the fleet to Windows 11 24H2 (with the pilot cohort excluded so they run ahead)
- Created an Expedited Quality update policy for out-of-band security patches
- Monitored Windows Update deployment status across devices

**Exercise 5: Enable Endpoint analytics and proactive remediations**
- Enabled Endpoint analytics to monitor device performance and user experience
- Created a proactive remediation script package to detect and clear old temp files
- Monitored remediation execution results

**Exercise 6: Use the Troubleshooting blade**
- Investigated a user's device status and policy assignments
- Diagnosed and resolved a real policy conflict using **Per-setting status**
- Forced a device sync to retrieve new policies immediately
- Inspected the Conditional Access policy's **Report-only** impact via sign-in logs

**Key Takeaways:**
- Configuration profiles can be created using Settings Catalog (granular control) or templates (pre-configured bundles)
- Assignment filters refine policy targeting without creating additional groups
- Compliance policies with grace periods provide users time to remediate issues before access is blocked
- Group Policy analytics helps plan on-premises-to-cloud migration by identifying supported settings
- Windows Update rings enable phased rollouts with deferrals for stability
- Endpoint analytics and proactive remediations enable proactive device management and issue resolution
- The Troubleshooting blade consolidates device, policy, and app status for efficient troubleshooting

**Next Steps:**
In Lab 03, you'll deploy applications to managed devices using Microsoft Store apps, Win32 packages, Microsoft 365 Apps, and App Protection Policies.

---

**END OF LAB**

---

**Previous:** [← Exercise 6: Use the Troubleshooting blade](exercise-6.md)

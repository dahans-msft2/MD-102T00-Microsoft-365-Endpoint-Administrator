---
lab:
  title: 'Lab 03: Manage applications'
  description: 'In this lab, you deploy Microsoft Store apps, a packaged Win32 application, Microsoft 365 Apps, and Enterprise App Catalog apps, then configure app supersedence and App Protection Policies.'
  duration: 100 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune
    - Microsoft 365 Apps
    - Windows
---

# Lab 03: Manage applications

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. With devices enrolled and managed (Labs 01-02), you now need to deploy applications to users and devices. You'll use multiple deployment methods: Microsoft Store apps (modern apps), Win32 packages (legacy applications), Microsoft 365 Apps (productivity suite), and the Enterprise App Catalog (curated third-party apps). You'll also configure App Protection Policies to secure corporate data on mobile and unenrolled devices.

By the end of this lab, you'll have:
- Deployed a Microsoft Store app
- Packaged and deployed a Win32 application with custom detection rules (tagged with the `Pharmacy` scope tag from Lab 01)
- Deployed Microsoft 365 Apps with update channel configuration
- Added and assigned an app from the Enterprise App Catalog
- Configured app supersedence to automatically upgrade an application (still scoped to the pilot cohort and tagged `Pharmacy`)
- Created an App Protection Policy for mobile devices
- Monitored app deployment status, troubleshot failures, and diagnosed an intentional app-assignment conflict

---

## Lab Duration

**Estimated Time:** 100 minutes

---

## Instructions

### Before you begin

This lab requires:
- Completion of **Lab 01** (devices enrolled, groups configured)
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com`)
- Global Administrator or Intune Administrator credentials
- **CL1** (enrolled device, Megan Bowen signed in)
- **CL2** (enrolled device, Joni Sherman signed in)
- Win32 app source files (provided in lab assets at `C:\LabAssets\Win32-App\`)
- **Microsoft Intune Suite trial active** (activated in **Lab 01** prerequisites) — required for Exercise 4 (Enterprise App Catalog)

---

## Exercises in this lab

1. [Exercise 1: Deploy Microsoft Store apps](exercise-1.md)
2. [Exercise 2: Package and deploy a Win32 application](exercise-2.md)
3. [Exercise 3: Deploy Microsoft 365 Apps](exercise-3.md)
4. [Exercise 4: Use the Enterprise App Catalog](exercise-4.md)
5. [Exercise 5: Configure app supersedence](exercise-5.md)
6. [Exercise 6: Create an App Protection Policy](exercise-6.md)
7. [Exercise 7: Monitor app deployment and troubleshoot failures](exercise-7.md)
8. [Lab summary](summary.md)

---

**Next:** [→ Exercise 1: Deploy Microsoft Store apps](exercise-1.md)

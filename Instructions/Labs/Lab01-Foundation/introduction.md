---
lab:
  title: 'Lab 01: Foundation — Identity, enrollment, and Autopilot'
  description: 'In this lab, you configure Microsoft Entra ID identity governance, device registration and enrollment policies, and Windows Autopilot to prepare a Microsoft 365 tenant for Intune device management.'
  duration: 90 minutes
  level: 200
  islab: true
  primarytopics:
    - Microsoft Intune
    - Microsoft Entra ID
    - Windows
    - Windows Autopilot
---

# Lab 01: Foundation — Identity, enrollment, and Autopilot

## Lab scenario

You are **Jordan Chen**, Modern Endpoint Administrator at Contoso Healthcare. Contoso is adopting a cloud-first endpoint management strategy using Microsoft Intune and Microsoft Entra ID. Your first task is to prepare the Microsoft 365 tenant for device management by configuring identity governance (users, groups, and roles), device registration policies, Windows enrollment policies, and Windows Autopilot. This foundational configuration will enable the device enrollment and policy deployment work in subsequent labs.

By the end of this lab, you'll have:
- Configured users and dynamic groups (including a compound-rule dynamic group) for organizational targeting
- Delegated administrative access using Microsoft Entra ID roles, administrative units, and a custom Intune RBAC role with a scope tag
- Set device registration policies and enabled Microsoft Entra Local Administrator Password Solution (LAPS)
- Verified automatic Intune enrollment and configured Enrollment Status Page profiles
- Blocked personally owned Android device enrollment
- Enrolled two Windows 11 devices via Microsoft Entra join
- Registered a device for Windows Autopilot with a deployment profile

---

## Lab Duration

**Estimated Time:** 90 minutes

---

## Instructions

### Before you begin

This lab requires:
- Access to the Contoso Microsoft 365 tenant (`<TenantPrefix>.onmicrosoft.com` or equivalent)
- Global Administrator credentials
- Four virtual machines: **CL1**, **CL2**, **CL3**, and **LX1**
- Internet connectivity from all VMs

**Important:** This is the foundational lab for the MD-102 lab series. All subsequent labs assume the configuration completed in this lab (enrolled devices, users, groups, and policies).

> [!IMPORTANT]
> **Complete multifactor authentication (MFA) enrollment before starting Exercise 2.** Some Contoso lab tenants have a Conditional Access policy that enforces the `p1` (MFA) authentication context for the Azure management API. This blocks access to **entra.microsoft.com** and **intune.microsoft.com** until your admin account is enrolled in MFA. The Microsoft 365 admin center (**admin.cloud.microsoft**) is exempt and works without MFA. If you're prompted to set up additional security verification on first sign-in, complete the Microsoft Authenticator setup before continuing.
>
> The Microsoft 365 admin center may open in **Simplified view** by default. Switch to **Dashboard view** from the toggle in the top-right corner to match the screenshots in this lab.

---

> [!IMPORTANT]
> **Activate the Microsoft Intune Suite 90-day trial now — before you start Lab 03.** Several later exercises (Lab 03 Exercise 4, Lab 04 Exercises 4–5, Lab 06 Exercises 1–3) require Intune Suite capabilities. Activating the trial up front means every downstream lab “just works” and avoids surprise blockers mid-lab. The trial is free, 90 days, up to 250 users per tenant, and reuses your existing tenant billing relationship — no payment method is required.
>
> **Steps (takes about two minutes):**
>
> 1. In the **Microsoft Intune admin center** (`intune.microsoft.com`), expand **Tenant administration** and select **Intune add-ons**.
> 2. Select the **All add-ons** tab.
> 3. In the row for **Microsoft Intune Suite**, in the **Try or buy** column, select **View details**.
> 4. In the details pane, select **To try or buy, go to Microsoft 365 admin center**. A new tab opens to the Microsoft 365 admin center product page.
> 5. On the **Microsoft Intune Suite** offer page, select **Start free trial**.
> 6. On the **Checkout** page, confirm: **Microsoft Intune Suite Trial**, 90-day term, 250 licenses, **USD 0.00**, no payment method required. Select **Try now**.
> 7. Return to the Intune admin center. Refresh **Tenant administration → Intune add-ons**. Select the **Your add-ons** tab — within a few minutes you should see **Microsoft Intune Suite Trial** listed with a **Purchased quantity** of **250**. The Suite includes: **Intune Plan 2**, **Remote Help**, **Endpoint Privilege Management**, **Enterprise App Management**, **Advanced Analytics**, and **Cloud PKI**.
>
> **Don't be misled by the All add-ons tab.** The **Microsoft Intune Suite** row will show **"~90 days left in trial"** in the Subscription status column, but the individual capability rows (Intune Plan 2, Endpoint Privilege Management, Remote Help, Enterprise App Management, Advanced Analytics, Cloud PKI) will continue to show **"Available for trial or purchase"**. That's expected — those are the *standalone* add-on SKUs; the Suite trial bundles all of them at the Suite level. To confirm a capability is actually usable, browse to its blade (e.g., **Endpoint security → Endpoint Privilege Management** or **Tenant administration → Cloud PKI**) and look for the *"\~89/90 days left in trial"* banner at the top.
>
> The trial runs for 90 days, followed by a 30-day grace period. **You can only start the trial once per tenant**, so plan to complete Labs 02–06 inside that window. If the trial is already active, you'll see **Active** in the Subscription status column and can skip the steps above.

---

## Exercises in this lab

1. [Exercise 1: Configure users and groups](exercise-1.md)
2. [Exercise 2: Configure administrative delegation](exercise-2.md)
3. [Exercise 3: Configure device registration and settings](exercise-3.md)
4. [Exercise 4: Configure Windows enrollment policies](exercise-4.md)
5. [Exercise 5: Enroll Windows devices](exercise-5.md)
6. [Exercise 6: Configure Windows Autopilot](exercise-6.md)
7. [Lab summary](summary.md)

---

**Next:** [→ Exercise 1: Configure users and groups](exercise-1.md)

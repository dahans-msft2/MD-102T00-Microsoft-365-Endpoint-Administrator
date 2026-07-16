# Lab 06, Exercise 5: Explore Azure Virtual Desktop session host enrollment

### Scenario

Azure Virtual Desktop (AVD) provides multi-session Windows desktops for virtual desktop infrastructure (VDI) scenarios. You'll review how AVD session hosts can be enrolled in Intune for policy management.

> [!NOTE]
> AVD session host enrollment requires an Azure subscription and AVD deployment. This exercise is a **guided demonstration**.

### Task 1: Understand AVD session host enrollment (demonstration)

1. Understand the AVD architecture:
   - **Host pool:** Collection of identical session hosts (VMs)
   - **Session hosts:** Windows 11 or Windows 10 multi-session VMs
   - **Workspaces:** User-facing interface to access desktops and apps

1. Understand how session hosts are enrolled in Intune:
   - Session hosts are Microsoft Entra joined (or Hybrid joined)
   - Automatic MDM enrollment is enabled (same as physical devices in Lab 01)
   - Session hosts enroll in Intune during initial provisioning

1. Understand AVD-specific policy considerations:
   - **User-based policies:** Applied to the user session (e.g., OneDrive sync, app settings)
   - **Device-based policies:** Applied to the session host VM (e.g., BitLocker, firewall, antivirus)
   - **Multi-session optimizations:** Policies should account for multiple concurrent users (e.g., FSLogix profile containers)

**You now understand how AVD session hosts enroll in Intune and how policies are applied in multi-session environments.**

---

### Task 2: Review AVD session host in Intune (demonstration)

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **All devices**.

1. Understand that AVD session hosts appear in the device list with:
   - **Device name:** AVD-SessionHost-<number>
   - **OS:** Windows 11 Enterprise multi-session or Windows 10 Enterprise multi-session
   - **Managed by:** Intune

1. Understand that AVD session hosts receive Intune policies:
   - Configuration profiles (e.g., Start menu layout, Edge policies)
   - Compliance policies (e.g., antivirus, firewall)
   - Applications (e.g., Microsoft 365 Apps, LOB apps)

1. Understand AVD-specific considerations:
   - Do not apply BitLocker to session hosts (managed disks are encrypted at rest in Azure)
   - Use FSLogix for user profile management (not OneDrive Known Folder Move)
   - Apply Windows Update policies carefully (coordinate with AVD maintenance windows)

**You now understand how AVD session hosts are managed in Intune.**

---

**Previous:** [← Exercise 4: Explore Windows 365 Cloud PC provisioning](exercise-4.md) | **Next:** [Lab summary →](summary.md)

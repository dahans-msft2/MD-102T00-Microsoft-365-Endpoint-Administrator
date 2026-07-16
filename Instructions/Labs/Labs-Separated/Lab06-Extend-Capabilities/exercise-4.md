# Lab 06, Exercise 4: Explore Windows 365 Cloud PC provisioning

### Scenario

Windows 365 provides cloud-hosted Windows desktops (Cloud PCs) that users access via browser or Remote Desktop client. You'll review the provisioning process and understand how Cloud PCs integrate with Intune.

> [!NOTE]
> Windows 365 provisioning requires an Azure subscription and additional licensing. This exercise is a **guided demonstration** of the provisioning workflow.

### Task 1: Review Windows 365 provisioning policy (demonstration)

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Windows 365** → **Provisioning policies**.

   > [!NOTE]
   > If Windows 365 is not available in your tenant, review the following steps conceptually.

1. Understand the **Create provisioning policy** workflow:
   - **Basics:**
     - Policy name
     - Join type: Microsoft Entra join or Hybrid Microsoft Entra join
     - Network: Microsoft-hosted network or Azure network connection
   - **Image:**
     - Gallery image (e.g., Windows 11 Enterprise + Microsoft 365 Apps)
     - Custom image (uploaded to Azure Compute Gallery)
   - **Configuration:**
     - License type: Enterprise, Business, or Frontline
     - Region: Azure region for Cloud PC deployment
     - Enable single sign-on: Yes/No

1. Understand the **Assignment** workflow:
   - Assign provisioning policy to Microsoft Entra groups
   - Users in the group automatically receive a Cloud PC when policy is assigned
   - Cloud PC is provisioned in Azure (typically 15–30 minutes)

1. Understand the **User experience**:
   - User signs in to **https://windows365.microsoft.com**
   - Cloud PC appears in the user's dashboard
   - User can launch the Cloud PC via browser or Remote Desktop client
   - Cloud PC is managed by Intune (same policies as physical devices)

**You now understand how Windows 365 provisioning policies deploy cloud-hosted Windows desktops.**

---

### Task 2: Review Cloud PC management in Intune (demonstration)

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **All devices**.

1. Understand that Cloud PCs appear in the device list with:
   - **Device name:** CloudPC-<username>
   - **Managed by:** Intune
   - **Ownership:** Corporate
   - **OS:** Windows 11 Enterprise

1. Understand that Cloud PCs receive the same Intune policies as physical devices:
   - Configuration profiles
   - Compliance policies
   - Applications
   - Security baselines

1. Understand Cloud PC-specific actions:
   - **Restart:** Restarts the Cloud PC
   - **Resize:** Changes the Cloud PC SKU (vCPU, RAM)
   - **Restore:** Restores the Cloud PC from a backup snapshot
   - **Reprovision:** Wipes the Cloud PC and re-provisions from the image

**You now understand how Cloud PCs are managed in Intune like physical devices.**

---

**Previous:** [← Exercise 3: Use Advanced Analytics and Device Query](exercise-3.md) | **Next:** [→ Exercise 5: Explore Azure Virtual Desktop session host enrollment](exercise-5.md)

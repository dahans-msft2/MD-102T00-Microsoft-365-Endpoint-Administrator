# Lab 04, Exercise 4: Deploy Microsoft Tunnel Gateway

### Scenario

Microsoft Tunnel is a VPN gateway solution that provides secure access to on-premises and cloud resources for mobile devices. You'll deploy the Tunnel Gateway on an Ubuntu server (LX1), register it with Intune, and author the VPN profile mobile devices would consume.

> [!IMPORTANT]
> **Scope.** This exercise covers gateway deployment, Intune registration, and VPN profile authoring. The lab environment doesn't include a mobile device, so **live client VPN connectivity through the gateway is out of scope** — similar to how Lab 01 scopes out the live Autopilot OOBE. The lab is complete when the LX1 server appears as **Online** in **Tenant administration** → **Microsoft Tunnel Gateway** → **Servers** (Task 3), and the VPN profile is authored and assigned (Task 4).
>
> Microsoft Tunnel Gateway is included with **Intune Plan 1** (no Suite required). If LX1 isn't available in your lab environment, review the steps conceptually or skip to Exercise 5.

### Task 1: Prepare the LX1 server

1. Switch to **LX1** (Ubuntu 22.04 server).

1. Sign in with the provided credentials (typically `ubuntu` user with key-based or password auth).

1. Verify Docker is installed:

   ```bash
   docker --version
   ```

   If Docker is not installed, install it:

   ```bash
   sudo apt update
   sudo apt install docker.io -y
   sudo systemctl enable docker
   sudo systemctl start docker
   ```

1. Verify internet connectivity:

   ```bash
   ping -c 4 8.8.8.8
   ```

1. Verify the server has an internal IP address and hostname:

   ```bash
   ip addr show
   hostname -f
   ```

   Note the internal IP/hostname (e.g., `10.0.1.10` or `lx1.lab.local`). The gateway only needs **outbound** access to Microsoft Intune endpoints to register — no inbound ports, no public FQDN, and no publicly-trusted certificate are required for this lab.

**You have successfully prepared the LX1 server for Microsoft Tunnel installation.**

---

### Task 2: Download and install Microsoft Tunnel

1. On **LX1**, download the Microsoft Tunnel installation script:

   ```bash
   wget https://aka.ms/microsofttunneldownload -O mstunnel-setup
   chmod +x mstunnel-setup
   ```

1. Run the installation script:

   ```bash
   sudo ./mstunnel-setup
   ```

1. Follow the installation prompts:
   - Accept the license terms
   - Choose installation path: `/opt/microsoft/mstunnel` (default)
   - Configure TLS certificate:
     - Option 1: Provide an existing certificate and private key
     - Option 2: Generate a self-signed certificate (for lab purposes)

   For lab purposes, select **Option 2** to generate a self-signed certificate. No mobile client connects through the gateway in this lab, so a publicly-trusted certificate isn't required.

1. Wait for the installation to complete (typically 5–10 minutes).

1. Verify the Tunnel Gateway service is running:

   ```bash
   sudo systemctl status mstunnel
   ```

   The output should show **active (running)**.

**You have successfully installed Microsoft Tunnel Gateway on LX1.**

---

### Task 3: Register the Tunnel Gateway in Intune

1. On **CL1**, in the **Microsoft Intune admin center**, navigate to **Tenant administration** → **Microsoft Tunnel Gateway**.

1. Select the **Sites** tab.

1. Select **Create** to create a new Tunnel site.

1. On the **Create a site** page, enter:
   - **Name:** `Contoso HQ Tunnel`
   - **Description:** `Microsoft Tunnel Gateway for mobile device VPN access`
   - **Public address:** Enter the LX1 server's internal IP or hostname (e.g., `10.0.1.10` or `lx1.lab.local`). In production this would be the public FQDN mobile clients connect to; for this lab it's a required field with no client traffic behind it.

1. Select **Create**.

1. After the site is created, select **Servers** tab.

1. Select **Add** to register the LX1 server.

1. On **LX1**, generate a registration token:

   ```bash
   sudo mstunnel register
   ```

   The command will output a registration token (a long alphanumeric string).

1. On **CL1**, in the **Add server** dialog, paste the registration token.

1. Select **Add**.

1. Wait for the server to register and sync with Intune (typically 2–5 minutes).

1. Verify the server appears in the **Servers** list with status **Online**.

> [!TIP]
> **Online** is the verifiable success criterion for this exercise. It confirms outbound registration worked, the install completed, and Intune is talking to your gateway — everything the gateway-deployment skill is meant to teach.

**You have successfully registered the Microsoft Tunnel Gateway in Intune.**

---

### Task 4: Create a VPN profile for Microsoft Tunnel

> [!NOTE]
> You'll author the VPN profile end-to-end and assign it to a group — the same workflow you'd use in production. In this lab environment no mobile device is enrolled to consume it, so the profile is authored and assigned but **client connection through the tunnel is out of scope** (see the scope callout at the top of Exercise 4).

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Configuration profiles**.

1. Select **Create** → **New policy**.

1. In the **Create a profile** pane, configure:
   - **Platform:** iOS/iPadOS (or Android, depending on your test devices)
   - **Profile type:** Templates → VPN

1. Select **Create**.

1. On the **Basics** page, enter:
   - **Name:** `VPN - Microsoft Tunnel`
   - **Description:** `VPN profile for secure access via Microsoft Tunnel Gateway`

1. Select **Next**.

1. On the **Configuration settings** page, configure:
   - **Connection name:** `Contoso VPN`
   - **Connection type:** Microsoft Tunnel (Standalone client)
   - **Server address:** Enter the LX1 server's address (e.g., `lx1.lab.local` — same value used when registering the Tunnel site in Task 3)
   - **Per-app VPN:** Not configured (or configure specific apps if desired)
   - **Always-on VPN:** Enable (recommended for corporate-owned devices)

1. Select **Next**.

1. On the **Assignments** page, assign to a mobile device group (e.g., **All users** or a pilot group).

1. Select **Next** → **Create**.

**You have successfully created a VPN profile for Microsoft Tunnel.**

---

**Previous:** [← Exercise 3: Configure BitLocker encryption](exercise-3.md) | **Next:** [→ Exercise 5: Implement Microsoft Cloud PKI](exercise-5.md)

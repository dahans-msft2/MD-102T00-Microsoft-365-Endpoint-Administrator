# Lab 06, Exercise 3: Use Advanced Analytics and Device Query

### Scenario

**Advanced Analytics** (part of the Intune Suite) provides ML-powered insights into device performance, anomaly detection, and resource utilization. **Device Query** uses Kusto Query Language (KQL) to run ad-hoc queries against Windows device telemetry — either against a single device (live) or across many devices. This is the upper-intermediate replacement for "please run remote desktop and check" — a delegated admin can answer real support questions without ever touching a user's device.

The Intune Suite trial (activated in **Lab 01** prerequisites) includes Advanced Analytics, so this exercise is fully hands-on.

> [!IMPORTANT]
> **Device prerequisite for Device Query.** A device must be **enrolled in Endpoint Analytics** before it shows up in Device Query results. Endpoint Analytics enrollment is enabled tenant-wide via **Reports** → **Endpoint analytics** → **Settings**. If you completed **Lab 02 Exercise 5 Task 1** (Enable Endpoint analytics), your devices are already enrolled and ready.

> [!NOTE]
> **Empty results are normal on a fresh tenant.** Until at least one Windows device has actually checked in to Endpoint Analytics, every multi-device Device Query in Task 3 will return **0 items**. The Get started → Prerequisites pane on the Device Query page repeats this: *"For a device to appear in device queries, it must be enrolled in Endpoint Analytics."* If your SEA-DEV1/SEA-DEV2 haven't checked in yet, run a single-device query against the device blade (Task 2) instead — those run live and don't depend on the Endpoint Analytics catalog.

> [!NOTE]
> **Telemetry latency.** Advanced Analytics dashboards (anomaly detection, resource performance, battery health) need approximately **24 hours of device telemetry** to populate meaningfully. Device Query, by contrast, runs against the device's **live state** and returns results within seconds. If your SEA-DEV1/SEA-DEV2 devices were enrolled less than 24 hours ago, the dashboards in Task 1 may show "Insufficient data" — Tasks 2 and 3 (Device Query) will still work.

### Task 1: Review Advanced Analytics dashboards

1. In the **Microsoft Intune admin center**, navigate to **Reports** → **Endpoint analytics** → **Advanced analytics**.

1. Review the **Anomaly detection** dashboard:
   - **Device anomalies:** Devices exhibiting unusual behavior (high CPU, frequent crashes, app hangs)
   - **User anomalies:** Users experiencing degraded experience scores
   - **Application anomalies:** Apps with high crash rates or slow start times

   > [!NOTE]
   > Anomaly detection uses ML to identify outliers from each device's own historical baseline (not a fleet-wide threshold). On a new lab device with limited history you may see empty panels or a status banner; that's expected.

1. Review the **Resource performance** dashboard:
   - **CPU performance:** Devices with sustained high CPU utilization
   - **Memory performance:** Devices with memory pressure (page faults, working-set pressure)
   - **Disk performance:** Devices with slow disk I/O

1. Review the **Battery health** dashboard (if mobile devices are enrolled):
   - **Battery capacity degradation:** Devices with reduced battery health vs. designed capacity
   - **Charging behavior:** Frequent charging cycles

**You have successfully reviewed the Advanced Analytics dashboards.**

---

### Task 2: Run live Device Query on a single device

Single-device Device Query runs a KQL query against one Windows device's live state. It's the canonical replacement for opening a remote control session just to check a service, a registry value, or an installed app version.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Windows** → select **SEA-DEV1**.

1. Under the **Monitor** section, select **Device query**.

1. In the query editor, enter and run the following query to list the CPU information for SEA-DEV1:

   ```kusto
   Cpu
   | project ProcessorId, Model, Architecture, CpuStatus, CoreCount, LogicalProcessorCount, Manufacturer
   ```

1. Select **Run**. Results appear in the **Results** tab within a few seconds.

   > [!NOTE]
   > Single-device Device Query has a **15 queries / minute** rate limit per admin and a **2048-character** query input limit. The result set is capped at 128 KB.

1. Replace the query with this one to check BitLocker encryption status on SEA-DEV1's drives:

   ```kusto
   EncryptableVolume
   | project Device, DriveLetter, ProtectionStatus, ConversionStatus, EncryptionMethod
   | join LogicalDrive on Device
   ```

1. Select **Run**. Confirm SEA-DEV1's OS drive shows **PROTECTED** — this verifies the BitLocker policy from **Lab 04 Exercise 3** is actively encrypting the drive (rather than just "assigned" in the Intune portal).

1. Replace the query with this one to verify the device's OS version:

   ```kusto
   OsVersion
   | project Device, OsVersion, OsBuildNumber, OsArchitecture
   ```

1. Select **Run**. Confirm SEA-DEV1 is running the Windows 11 24H2 build you pinned via the Feature update profile in **Lab 02 Exercise 4**.

**You have successfully run live Device Query against a single device.**

---

### Task 3: Run multi-device Device Query and build a security group from results

Multi-device Device Query runs one KQL query across every Windows device in your scope and returns one row per device. The killer feature: you can **create a Microsoft Entra security group directly from a query's results**, which means you can dynamically target Intune policies and Conditional Access at exactly the devices your query found.

1. In the **Microsoft Intune admin center**, navigate to **Devices** → **Device query**.

   > [!NOTE]
   > This is the **multi-device** Device Query surface (Devices → Device query at the top of the **Manage devices** group is not present — it's a top-level item under **Devices**). It's distinct from the single-device Device Query you used in Task 2 (Devices → Windows → *device* → Monitor → Device query).

1. Expand the **example queries** section under **Getting started** on the left, and browse the pre-built samples. Microsoft maintains this list — it's the fastest way to learn the supported tables and operators.

1. Enter and run this query to find every Windows device that is **not** BitLocker-encrypted — the canonical "these devices need attention now" query:

   ```kusto
   EncryptableVolume
   | where ProtectionStatus != "PROTECTED"
   | join LogicalDrive on Device
   ```

1. Select **Run**. The Results tab returns one row per affected device.

1. With results on screen, select **Add all items to a group** from the top of the Results tab. In the dialog, name the new group `sg-Devices-Unencrypted` (description: *Devices identified by Device Query as not BitLocker-encrypted*). Select **Create group**.

   > [!NOTE]
   > **This is the upper-intermediate move.** Instead of building a dynamic device group based on a rough attribute (e.g., "deviceCategory eq 'Laptop'"), you can query the actual on-device state and turn the result into a real, addressable Microsoft Entra security group. Use it to target a remediation script, a stricter compliance policy, or a Conditional Access "block until compliant" enforcement.

1. Run a second query to find devices running an OS build older than your fleet target (Windows 11 24H2 — build number `26100`):

   ```kusto
   OsVersion
   | where OsBuildNumber < 26100
   | project Device, OsVersion, OsBuildNumber
   | order by OsBuildNumber asc
   ```

1. Select **Run**. This is your "hasn't taken the feature update yet" working list — useful for chasing devices that fall behind the Feature update profile you created in **Lab 02 Exercise 4**.

1. Run a third query to summarize the fleet by processor architecture (a quick "who has ARM64 devices" inventory):

   ```kusto
   Cpu
   | summarize DeviceCount = count() by Architecture
   ```

1. Select **Run**. The Results tab shows a summary row per architecture.

1. Select **Export** to save the result set as CSV — useful for handing a hardware inventory to procurement or for ticketing-system import.

   > [!NOTE]
   > Multi-device Device Query results respect **scope tags**. When Lee Gu (the **Pharmacy Helpdesk** delegated admin assigned in **Lab 05 Exercise 3**) runs these same queries, the results are automatically filtered to only the Pharmacy-tagged devices in her scope. Delegated admins can answer support questions about their own devices without ever seeing the rest of the tenant.

**You have successfully run multi-device Device Query and converted a query result into a Microsoft Entra security group.**

---

**Previous:** [← Exercise 2: Deploy Remote Help](exercise-2.md) | **Next:** [→ Exercise 4: Explore Windows 365 Cloud PC provisioning](exercise-4.md)

# 📊 ANTA Report <a id="anta-report"></a>

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Run Overview](#run-overview)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## 📋 Run Overview <a id="run-overview"></a>

| ⚙️ Run Metric | 📝 Details |
| :- | :- |
| **ANTA Version** | v1.7.0 |
| **Test Execution Start Time** | 2026-05-14 23:34:04.296+00:00 |
| **Test Execution End Time** | 2026-05-14 23:34:11.523+00:00 |
| **Total Duration** | 7 seconds |
| **Total Devices In Inventory** | 11 |
| **Devices Unreachable At Setup** | None |
| **Devices Filtered At Setup** | None |
| **Filters Applied** | None |

## 📉 Test Results Summary <a id="test-results-summary"></a>

### 🔢 Summary Totals <a id="summary-totals"></a>

| Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- |
| 5 | 2 | 0 | 1 | 2 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **Media-H2** | 3 | 1 | 0 | 0 | 2 | - | Connectivity |
| **Staff-H1** | 2 | 1 | 0 | 1 | 0 | - | Connectivity |

### 🗂️ Summary Totals Per Category <a id="summary-totals-per-category"></a>

| Test Category | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- | :- |
| **Connectivity** | 5 | 2 | 0 | 1 | 2 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Custom Field | Result | Messages |
| :- | :- | :- | :- | :- | :- | :- |
| Media-H2 | Connectivity | ICMP | ICMP reachability validation for: Media-H2 to Staff-H1 | - | ✅&nbsp;Success | - |
| Media-H2 | Connectivity | TCP | Validates active Layer 4 TCP transport path connectivity. | - | ❗&nbsp;Error | bash timeout 7 bash -c 'if [ "default" = "default" ]; then iperf -c 172.16.11.10 -p 5901  -t 2; else ip netns exec ns-default iperf -c 172.16.11.10 -p 5901  -t 2; fi' has failed: Command 'bash -c 'if [ "default" = "default" ]; then iperf -c 172.16.11.10 -p 5901 -t 2; else ip netns exec ns-default iperf -c 172.16.11.10 -p 5901 -t 2; fi'' timed out |
| Media-H2 | Connectivity | Telnet | Validates active cleartext Telnet application layer delivery. | - | ❗&nbsp;Error | bash timeout 7 bash -c 'if [ "default" = "default" ]; then iperf -c 172.16.11.10 -p 23  -t 2; else ip netns exec ns-default iperf -c 172.16.11.10 -p 23  -t 2; fi' has failed: Command 'bash -c 'if [ "default" = "default" ]; then iperf -c 172.16.11.10 -p 23 -t 2; else ip netns exec ns-default iperf -c 172.16.11.10 -p 23 -t 2; fi'' timed out |
| Staff-H1 | Connectivity | ICMP | ICMP reachability validation for: Staff-H1 to IOT-H3 | - | ❌&nbsp;Failure | Ping completely failed to target device: IOT-H3 |
| Staff-H1 | Connectivity | ICMP | ICMP reachability validation for: Staff-H1 to Media-H2 | - | ✅&nbsp;Success | - |

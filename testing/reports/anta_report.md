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
| **Test Execution Start Time** | 2026-05-14 07:12:07.100+00:00 |
| **Test Execution End Time** | 2026-05-14 07:12:07.344+00:00 |
| **Total Duration** | 244 milliseconds |
| **Total Devices In Inventory** | 11 |
| **Devices Unreachable At Setup** | None |
| **Devices Filtered At Setup** | None |
| **Filters Applied** | None |

## 📉 Test Results Summary <a id="test-results-summary"></a>

### 🔢 Summary Totals <a id="summary-totals"></a>

| Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- |
| 4 | 2 | 0 | 2 | 0 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **Media-H2** | 1 | 1 | 0 | 0 | 0 | - | - |
| **Staff-H1** | 3 | 1 | 0 | 2 | 0 | - | Connectivity |

### 🗂️ Summary Totals Per Category <a id="summary-totals-per-category"></a>

| Test Category | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- | :- |
| **Connectivity** | 4 | 2 | 0 | 2 | 0 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Custom Field | Result | Messages |
| :- | :- | :- | :- | :- | :- | :- |
| Media-H2 | Connectivity | ICMP | Test network reachability to one or many destination IP(s) via standard ICMP echo. | - | ✅&nbsp;Success | - |
| Staff-H1 | Connectivity | ICMP | Test network reachability to one or many destination IP(s) via standard ICMP echo. | - | ✅&nbsp;Success | - |
| Staff-H1 | Connectivity | Telnet | Validates active cleartext Telnet application layer delivery parameters. | - | ❌&nbsp;Failure | Transport block failure. Telnet Port 23 to 172.16.21.10 timed out or was dropped. |
| Staff-H1 | Connectivity | UDP | Validates active Layer 4 UDP transport path socket delivery parameters. | - | ❌&nbsp;Failure | Transport block failure. UDP Port 53 to 172.16.31.10 timed out or was dropped. |

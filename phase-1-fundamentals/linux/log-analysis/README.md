# Linux Authentication Log Analysis & Brute Force Detection - Lab 08 date:27-08

## Objective
Analyze Linux authentication logs (`/var/log/auth.log` / `journalctl`) to investigate failed login attempts, detect SSH brute-force attacks, and extract Indicators of Compromise (IoCs).

---

## Technical Concepts
- **Authentication Logs (`/var/log/auth.log` / `journalctl`)**: Centralized repositories recording user authentication events, `sudo` execution, and SSH connection attempts.
- **SSH Brute-Force Attack**: Automated login attempts targeting port 22/TCP using credential dictionaries.
- **Log Parsing**: Utilizing Linux text-processing pipelines (`grep`, `awk`, `sort`, `uniq`, `journalctl`) to isolate malicious IP sources and authentication failures.

---

## Analyst Commands & Execution Pipeline

### 1. Filter Failed Authentication Attempts via Journald
`sudo journalctl _COMM=su -n 10 --no-pager`

### 2. Search Authentication Failures in Auth Log
`sudo grep -i "authentication failure" /var/log/auth.log`

### 3. Extract & Count Attacker Source IPs (Top Offenders Pipeline)
`sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr`

---

## Security Analyst Value
Log analysis allows Blue Team analysts to correlate failed authentication spikes, identify brute-force patterns, extract malicious source IPs for firewall blocking, and confirm whether unauthorized access was obtained.

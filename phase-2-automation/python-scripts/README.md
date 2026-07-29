

# Python Authentication Log Parser - Lab 09


**Date:** July 28, 2026  
**Category:** Security Automation & Scripting / Blue Team  
**Language:** Python 3  

---

## 1. Objective
Automate system log inspection by developing a Python script (`log_parser.py`) to parse `/var/log/auth.log`, identify authentication failures, and extract security alert events.

---

## 2. Script Architecture & Logic
- **File I/O (`open`)**: Efficiently reads system log files line-by-line to optimize memory usage.
- **Pattern Matching (`.lower()`)**: Case-insensitive filtering for words like `failed` and `failure`.
- **Exception Handling (`try/except`)**: Prevents execution crashes by handling `PermissionError` and `FileNotFoundError`.

---

## 3. How to Run

```bash
# Grant execution permissions
chmod +x log_parser.py

# Execute with elevated privileges to read auth logs
sudo python3 log_parser.py

resume: in the age AI crtlC + ctrlV


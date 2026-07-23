
# Linux System Inspection - Lab 01

## Commands Executed:
- `pwd`: Prints the current working directory.
- `ls -la`: Lists all files, including hidden ones, with detailed permissions.
- `whoami`: Displays the current logged-in user.
- `uname -a`: Displays system info and Linux kernel version.
## File Permissions Lab

- `chmod u+x script.sh`: Grants execution (`x`) permissions to the file owner (`u`).

23/07 12:59
## Correlation Lab: Ports, Processes and Logs

- **Port Inspection (`ss -tulpn`)**: Identified active listening TCP/UDP ports and their associated PIDs.
- **Process Inspection (`ps aux | grep <PID>`)**: Correlated the process ID to identify the binary running on the system.
- **Log Inspection (`tail -f /var/log/auth.log` or `journalctl`)**: Monitored real-time authentication logs to inspect system activity.

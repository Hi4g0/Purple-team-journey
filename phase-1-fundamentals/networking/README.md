# Network Packet Capture - Lab 01 date:26/07/2026

## Objective
Capture and inspect live network traffic using `tcpdump`.

## Commands Executed:
- `ip a`: Identified active network interfaces on the local host.
- `sudo tcpdump -c 5 -i any icmp`: Captured ICMP (ping) packets to inspect network connectivity and packet flow in real-time.

## DNS Traffic Analysis - Lab 02

### Objective
Inspect DNS domain resolution queries and responses over UDP port 53.

### Commands Executed:
- `sudo tcpdump -c 4 -i any port 53`: Captured live DNS query and response packets filtering specifically on port 53.
- `nslookup github.com`: Queryed DNS servers to resolve the IP address of `github.com`.

## Firewall Management with UFW - Lab 03

#### im undertood those things

### Objective
Understand how local firewalls filter network traffic using specific port rules and actions (ALLOW/DENY).

### Concept Learned:
- `DENY IN`: Drops incoming traffic targeting a specific port from any host.
- `ALLOW IN`: Permits incoming traffic through a designated port for authorized connections.

### Commands Executed:
- `sudo ufw status numbered`: Displayed active firewall rules in an indexed table format.
- `sudo ufw deny 80/tcp`: Created a rule blocking incoming HTTP traffic on port 80.
- `sudo ufw allow 22/tcp`: Created a rule permitting incoming SSH management traffic on port 22.

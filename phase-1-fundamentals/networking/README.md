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

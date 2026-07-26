# Network Packet Capture - Lab 01 date:26/07/2026

## Objective
Capture and inspect live network traffic using `tcpdump`.

## Commands Executed:
- `ip a`: Identified active network interfaces on the local host.
- `sudo tcpdump -c 5 -i any icmp`: Captured ICMP (ping) packets to inspect network connectivity and packet flow in real-time.

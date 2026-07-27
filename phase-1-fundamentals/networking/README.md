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


## Network Path Inspection with Traceroute - Lab 04

### Objective
Analyze routing paths, network hops, and latencies from the local host to remote cloud infrastructure (GitHub/Microsoft Azure).

### Technical Analysis:
- **Local Gateway (Hop 1)**: Reached home router (`192.168.1.1`) under `0.5ms`.
- **ISP Infrastructure (Hops 2-5)**: Transited through Carrier-Grade NAT (CGNAT) and North Telecom backbone.
- **Enterprise Edge & Cloud Data Center (Hops 7-11)**: Entered Microsoft's global network backbone (`msn.net`) through São Paulo/Guarulhos (`sao30`/`gru30`) into the Campinas Data Center (`cpq02`/`cpq20`).
- **Firewall Dropped Packets (`* * *`)**: Internal data center security policies drop ICMP/TTL packets to prevent topology mapping.

### Commands Executed:
- `traceroute github.com`: Tracked the network path and round-trip times (RTT) across 30 maximum hops.

## Layer 2 Data Link Inspection (ARP Table) - Lab 05

### Objective
Inspect Address Resolution Protocol (ARP) cache mappings between Layer 3 IP addresses and Layer 2 Physical MAC addresses.

### Technical Concept:
- **ARP Protocol**: Resolves IP addresses into hardware MAC addresses within a local area network (LAN).
- **Security Relevance**: Monitoring ARP tables helps identify ARP Poisoning / Man-in-the-Middle (MITM) attacks where malicious hosts forge hardware MAC identities.

### Commands Executed:
- `ip neighbor`: Displayed the active neighbor table showing IP-to-MAC address bindings on the local interface.


## Packet Analysis & Display Filters with Wireshark - Lab 06 date:27/06/2026
### Objective
Understand display filter syntax in Wireshark for effective network traffic analysis during incident investigation.

### Key Display Filters Reference:
- `http`: Filters unencrypted web application traffic on TCP port 80.
- `dns`: Isolates Domain Name System queries and responses over UDP port 53.
- `ip.addr == X.X.X.X`: Shows all incoming and outgoing packets associated with a specific IP address.
- `ip.src == X.X.X.X && tcp.port == 80`: Combines logical operators to isolate HTTP traffic originating from a single host source.

### Security Analyst Context
Display filters allow SOC analysts to eliminate background network noise and isolate suspicious indicators of compromise (IoCs), such as unusual DNS queries or unauthorized connection attempts. 

# Mini-SOC Incident Response & Traffic Containment Report  date:27/07

**Incident ID:** INC-2026-0728  
**Date:** July 28, 2026  
**Severity Level:** Medium (Unencrypted Data Leak / Suspicious Egress Traffic)  
**Analyst:** Hiago (Blue Team / SOC Specialist)  

---

## 1. Executive Summary
On July 28, 2026, network monitoring detected unauthorized outbound HTTP traffic originating from a local host. The traffic transmitted unencrypted plaintext payloads on TCP port 80 to an external destination. A packet capture was initiated, revealing the target destination. The incident was successfully contained by enforcing strict outbound firewall filtering rules.

---

## 2. Technical Analysis & Indicators of Compromise (IoCs)
- **Source IP / Host:** Local Workstation (`192.168.x.x`)
- **Destination Protocol / Port:** TCP / Port 80 (HTTP)
- **Target Domain:** `neverssl.com`
- **Evidence File:** `incidente_traffic.pcap`
- **Root Cause:** Application transmitting cleartext sensitive payloads over an unencrypted transport layer.

---

## 3. Incident Response Workflow & Actions Taken

### Phase 1: Evidence Collection
Captured raw network packets directly from the interface using `tcpdump`:
`sudo tcpdump -i any port 80 -w incidente_traffic.pcap`

### Phase 2: Packet Inspection
Analyzed the `.pcap` file to inspect header flags, target IP bindings, and layer 7 payload structures:
`tcpdump -nn -r incidente_traffic.pcap`

### Phase 3: Containment & Hardening
Applied an outbound host-based firewall enforcement rule using `ufw` to prevent data exfiltration across TCP port 80:
`sudo ufw deny out 80/tcp`

---

## 4. Post-Incident Verification & Lessons Learned
- **Containment Verification:** Outbound requests targeting HTTP port 80 were blocked instantly by the kernel firewall filter (`ufw`), returning connection timeout errors on outbound connection attempts.
- **Recommendation:** Enforce mandatory TLS/SSL encryption across all internal services and restrict outbound TCP port 80 access by default.

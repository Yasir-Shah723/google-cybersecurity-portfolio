# 05 - Incident Handler's Journal: Detection, Analysis & Triage

## Overview
An operational log documenting security exercises and investigative workflows across the incident response lifecycle (NIST SP 800-61 Rev. 2). Tracks analytical observations, investigative workflows, and practical usage of defensive security tools.

## Logged Exercises & Tooling

### Entry #1: Healthcare Ransomware Incident Triage
- **Phase:** Detection & Analysis; Containment & Eradication.
- **Analysis:** Phishing vector analysis; containment via host isolation; evaluation of ransom refusal policies adhering to CISA/FBI guidance.

### Entry #2: Packet Analysis with Wireshark
- **Tool Used:** **Wireshark** (Graphical Network Protocol Analyzer)
- **Key Takeaways:** Inspected TCP 3-way handshakes, DNS queries, and cleartext protocols; applied display filters (`ip.addr`, `http`, `tcp.flags.syn`) to isolate anomalous traffic.

### Entry #3: Command-Line Traffic Sniffing with tcpdump
- **Tool Used:** **tcpdump** (CLI Network Protocol Analyzer)
- **Key Takeaways:** Built targeted Berkeley Packet Filter (BPF) commands (e.g., `tcpdump -i eth0 -nn -c 50 port 80 -w out.pcap`) for minimal-overhead triage on headless Linux servers.

### Entry #4: Indicator of Compromise (IoC) Triage with VirusTotal
- **Tool Used:** **VirusTotal** & Threat Feeds
- **Investigation:** Analyzed SHA-256 hash `54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b`; correlated multi-vendor detections; executed endpoint hash blacklisting in EDR.

## Deliverables
- Full Document: `Incident_Handlers_Journal_Complete.pdf`
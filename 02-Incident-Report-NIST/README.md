# 02 - Incident Report Analysis: DoS Attack Remediated

## Incident Scenario
A multimedia services company suffered an operational disruption lasting two hours due to a Denial of Service (DoS) attack. An external threat actor flooded the internal corporate network with ICMP packets (Ping Flood) through an unconfigured perimeter firewall, exhausting network capacity and halting critical client operations.

## Framework Applied: NIST CSF v1.1
- **Identify:** Isolated root cause to an unconfigured boundary firewall allowing unbounded ICMP echo requests.
- **Protect:** Implemented firewall rate-limiting on ICMP packets and segmented client staging environments from internal production networks.
- **Detect:** Configured Unicast Reverse Path Forwarding (uRPF) to inspect spoofed source IP addresses and deployed automated traffic monitoring software.
- **Respond:** Executed incident response procedures to block malicious streams, offlined non-essential services, and extracted packet logs for root-cause analysis.
- **Recover:** Restored customer-facing databases first, validated baseline network metrics, and re-enabled non-critical internal services.

## Technical Countermeasures Deployed
- **ICMP Rate Limiting:** Enforced threshold caps on echo requests per source IP.
- **Source IP Verification (uRPF):** Discarded forged/spoofed headers at the interface boundary.
- **Network-Based IDS/IPS:** Deployed signature-based filtering for abnormal ICMP payload characteristics.

## Deliverables
- Full Document: `Incident_Report_Analysis_DoS_NIST_CSF.pdf`
# 01 - Conduct a Security Audit: Botium Toys

## Overview
A comprehensive internal security audit conducted for **Botium Toys**, a retail and e-commerce business expanding into European markets. The evaluation benchmarks administrative, technical, and physical safeguards against global compliance standards.

## Frameworks Applied
- **NIST Cybersecurity Framework (CSF v1.1)**
- **Payment Card Industry Data Security Standard (PCI DSS)**
- **General Data Protection Regulation (GDPR)**
- **System and Organization Controls (SOC Type 1 & 2)**

## Key Findings
- **Defenses Active:** Working physical perimeter locks, functioning CCTV cameras, fire suppression systems, and network firewalls.
- **Critical Vulnerabilities:** Customer credit card details and EU citizen PII stored unencrypted and accessible to all employees.
- **Operational Gaps:** Absence of automated data backups, no documented Disaster Recovery Plan (DRP), and lack of an Intrusion Detection System (IDS).

## Remediation Roadmap
1. **Phase 1 (Days 1–30):** Implement Role-Based Access Control (RBAC), enforce AES-256 database encryption, and mandate TLS 1.3 across web touchpoints.
2. **Phase 2 (Days 30–60):** Deploy network IDS/IPS, configure an automated 3-2-1 backup strategy, and mandate enterprise Multi-Factor Authentication (MFA).
3. **Phase 3 (Days 60–90):** Establish an organizational 4-tier data classification scheme, draft a formal DRP with defined RTO/RPO metrics, and schedule legacy system patch cycles.

## Deliverables
- Full Document: `Botium_Toys_Security_Audit_Report.pdf`
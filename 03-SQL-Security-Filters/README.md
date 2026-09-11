# 03 - Apply Filters to SQL Queries: Security Log Triage

## Overview
This project illustrates practical database querying techniques used by cybersecurity analysts to triage security incidents from authentication logs and generate targeted employee machine lists for patch management.

## Environment & Tables
- **Database Engine:** MariaDB / MySQL (`organization` database)
- **Tables Queried:**
  - `log_in_attempts`: Tracks authentication telemetry (event ID, username, date, time, country, IP address, success status).
  - `employees`: Tracks workforce asset assignments (employee ID, device ID, username, department, office location).

## Executed Security Queries

### 1. After-Hours Failed Login Attempts
```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = FALSE;
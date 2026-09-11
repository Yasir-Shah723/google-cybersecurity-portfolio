# 06 - Update a File Through a Python Algorithm

## Overview
In regulated healthcare environments handling electronic personal health records (ePHI), access to restricted subnets must be restricted dynamically based on staff responsibilities. This project provides an automated Python algorithm that audits an active IP allow list file (`allow_list.txt`) and removes unauthorized addresses based on an updated revocation list (`remove_list`).

## Technical Workflow
1. **File Ingestion:** Utilizes Python `with open(import_file, "r") as file:` for resource-safe file stream management.
2. **Data Parsing:** Reads file content with `.read()` and converts whitespace-delimited IP entries into a mutable list using `.split()`.
3. **Iterative Revocation:** Cycles through each flagged address in `remove_list` using a `for` loop.
4. **Defensive Validation:** Applies conditional guard rails (`if element in ip_addresses:`) prior to invoking `.remove(element)` to prevent runtime `ValueError` crashes.
5. **Disk Commit:** Joins clean list elements with `\n`.join() and overwrites the active configuration using `with open(import_file, "w") as file:` and `.write()`.

## Python Implementation
```python
def update_file(import_file, remove_list):
    # 1. Read active allow list
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # 2. Convert to list
    ip_addresses = ip_addresses.split()

    # 3. Safely remove revoked addresses
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

    # 4. Reconstruct string and overwrite file
    ip_addresses = "\n".join(ip_addresses)
    with open(import_file, "w") as file:
        file.write(ip_addresses)
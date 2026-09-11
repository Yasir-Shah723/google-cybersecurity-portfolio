"""
File: algorithm.py
Author: Syed Yasir Shah
Description: Python algorithm to automate network access control by updating 
an IP address allow list ('allow_list.txt') and removing revoked IP addresses 
found in a designated removal list ('remove_list').
"""

def update_file(import_file, remove_list):
    """
    Reads an allow list file, removes specified IP addresses, and overwrites the file.

    Parameters:
        import_file (str): The path/name of the file containing active allowed IP addresses.
        remove_list (list): A list of IP addresses that should have access revoked.
    """
    # Step 1 & 2: Open the file in read mode and read contents into memory
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # Step 3: Convert the whitespace-delimited string into a list of IP addresses
    ip_addresses = ip_addresses.split()

    # Step 4 & 5: Iterate through remove_list and remove matching entries defensively
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

    # Step 6: Convert list back into a newline-separated string
    ip_addresses = "\n".join(ip_addresses)

    # Step 7: Overwrite the allow list file with the sanitized IP list
    with open(import_file, "w") as file:
        file.write(ip_addresses)

    print(f"[+] Successfully updated '{import_file}'. Revoked IPs removed.")


if __name__ == "__main__":
    # Target access control file
    target_file = "allow_list.txt"

    # List of employee IP addresses scheduled for access revocation
    revocation_list = [
        "192.168.1.15",
        "192.168.1.25",
        "192.168.1.40"
    ]

    print("[*] Initiating Network Access Control update...")
    update_file(target_file, revocation_list)

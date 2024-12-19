import os
import sys

def modify_hosts(domain, ip):
    hosts_path = "/etc/hosts"
    entry = f"{ip} {domain}\n"

    try:
        if os.geteuid() != 0:
            print("This script needs to be run as root.")
            sys.exit(1)

        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        for line in lines:
            if domain in line:
                print(f"The domain {domain} is already configured in /etc/hosts.")
                return

        with open(hosts_path, "a") as hosts_file:
            hosts_file.write(entry)

        print(f"The domain {domain} has been added to the /etc/hosts file with IP {ip}.")

    except Exception as e:
        print(f"Error modifying the /etc/hosts file: {e}")

if __name__ == "__main__":
    domain = "dev.codeleap.co.uk"
    ip = "127.0.0.1"

    modify_hosts(domain, ip)

import os

def modify_hosts_windows(domain, ip):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    entry = f"{ip} {domain}\n"

    try:
        if not os.access(hosts_path, os.W_OK):
            print("This script needs to be run as administrator.")
            return

        with open(hosts_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        for line in lines:
            if domain in line:
                print(f"The domain {domain} is already configured in the hosts file.")
                return

        with open(hosts_path, "a") as hosts_file:
            hosts_file.write(entry)

        print(f"The domain {domain} has been added to the hosts file with IP {ip}.")

    except Exception as e:
        print(f"Error modifying the hosts file: {e}")

if __name__ == "__main__":
    domain = "dev.codeleap.co.uk"
    ip = "127.0.0.1"

    modify_hosts_windows(domain, ip)

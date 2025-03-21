import requests

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device and login details
HOST = '10.10.20.48'
USER = 'developer'
PASS = 'C1sco12345'
TARGET_INTERFACE = "Loopback1"

def main():
    """Retrieve Interface details from the device via RESTCONF and check for a specific interface."""
    
    # RESTCONF URL to get interface details
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"

    # RESTCONF headers
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    # Perform GET request to retrieve interface details
    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
    interfaces_data = response.json()

    found = False
    for intf in interfaces_data["ietf-interfaces:interfaces"]["interface"]:
        if intf["name"] == TARGET_INTERFACE:
            found = True
            
            ipv4_addresses = intf["ietf-ip:ipv4"].get("address", [])
            ipv6_addresses = intf["ietf-ip:ipv6"].get("address", [])
            
            print(f"Interface: {intf['name']}")
            print(f"Description: {intf['description']}")
            print(f"Type: {intf['type']}")
            print(f"Enabled: {intf['enabled']}")
            
            if ipv4_addresses:
                for address in ipv4_addresses:
                    print(f"IPv4 Address: {address['ip']}")
                    print(f"IPv4 Netmask: {address['netmask']}")
            else:
                print(f"IPv4 Address: Not Configured")
                print(f"IPv4 Netmask: Not Configured")
            
            if ipv6_addresses:
                for address in ipv6_addresses:
                    print(f"IPv6 Address: {address['ip']}")
                    print(f"IPv6 Prefix: {address['prefix-length']}")
            else:
                print(f"IPv6 Address: Not Configured")
                print(f"IPv6 Prefix: Not Configured")
            
    if not found:
        print(f"Interface {TARGET_INTERFACE} not found on the device.")

if __name__ == '__main__':
    main()
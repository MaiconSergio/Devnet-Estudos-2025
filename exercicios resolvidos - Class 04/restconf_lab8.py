import requests

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device and login details
HOST = '10.10.20.48'
USER = 'developer'
PASS = 'C1sco12345'
TARGET_INTERFACE = "Loopback1"  # The specific interface we want to target

def main():
    """Retrieve specific interface details from the device using RESTCONF by targeting a precise URL."""
    
    # RESTCONF URL crafted to directly target the specified interface
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface={TARGET_INTERFACE}"

    # RESTCONF headers
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }

    # Perform GET request to retrieve the specific interface details
    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
    
    # Print the entire response, showcasing only the details of the targeted interface
    print(response.text)

if __name__ == '__main__':
    main()
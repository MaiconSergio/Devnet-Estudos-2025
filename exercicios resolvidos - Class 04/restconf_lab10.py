import requests

# Disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device details
HOST = '10.10.20.48'
USER = 'developer'
PASS = 'C1sco12345'


# Interface to update
TARGET_INTERFACE = "Loopback0"
DESCRIPTION = "Change by RESTCONF"
ENABLED = "true"

def main():
    # Constructing the payload
    payload = f'{{"ietf-interfaces:interface": {{"name": "{TARGET_INTERFACE}", "description": "{DESCRIPTION}", "type": "iana-if-type:softwareLoopback", "enabled": {str(ENABLED).lower()}}}}}'
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface={TARGET_INTERFACE}"
    
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'
    }

    # Using POST method
    response = requests.put(url, auth=(USER, PASS), headers=headers, verify=False, data=payload)
    
    # Check response
    if response.status_code == 204:
        print(f"Status Code: {response.status_code}")
        print("Success: Interface details updated.")
    else:
        print(f"Status Code: {response.status_code}")
        print("Error message returned:")
        print(response.text)

if __name__ == '__main__':
    main()
import requests

# Disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device details
HOST = '10.10.20.48'
USER = 'developer'
PASS = 'C1sco12345'

def main():
    """Retrieve Interface details from the device via RESTCONF."""
    
    # Construct the URL
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"
    
    # Headers for the GET request
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }
    
    # Make the GET request
    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
    
    # Print the returned JSON data
    print(type(response.text))
    print(response.text)

if __name__ == '__main__':
    main()
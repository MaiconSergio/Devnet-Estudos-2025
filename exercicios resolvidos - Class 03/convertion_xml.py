import xml.etree.ElementTree as ET
import json
import yaml

# Load XML data
tree = ET.parse('network_config.xml')
root = tree.getroot()

# Create a data structure to hold our parsed XML
network = {"routers": []}

for router in root.findall('router'):   
    router_data = {
        "id": router.find('id').text,
        "hostname": router.find('hostname').text,
        "interfaces": [
            {
                "name": iface.find('name').text,
                "ip_address": iface.find('ip_address').text,
                "subnet_mask": iface.find('subnet_mask').text
            }
            for iface in router.findall('interfaces/interface')
        ]
    }
    network['routers'].append(router_data)

# Convert dictionary data to JSON and save
with open('network_config.json', 'w') as json_file:
    json.dump(network, json_file, indent=4)

# Convert data to YAML and save
with open('network_config.yaml', 'w') as yaml_file:
    yaml.dump(network, yaml_file, default_flow_style=False)
# Lab: Converting XML to JSON and YAML with Python

## Introduction

In this lab, you will leverage Python's capabilities to transform data from XML format into both JSON and YAML. This is a common task when ensuring data interoperability among systems or preparing data for different types of data stores.

## Objective

- Convert XML data into JSON and YAML formats using Python.

## Lab Tasks

**Note**: Ensure you have the XML configuration file from the previous lab saved as `network_config.xml` in your working directory.

### 1. Converting XML Data to JSON

To begin, we'll convert our XML data into JSON format. This is a widespread format suitable for many applications, especially web-based apps.

**Python Code to Convert XML to JSON:**
```python
import xml.etree.ElementTree as ET
import json

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
```

### 2. Converting XML Data to YAML

Next, we'll encode our XML data into YAML, a human-readable format often used for configuration files.

**Note**: You'll need the `PyYAML` library. If you haven't already installed it, you can do so using pip: `pip install pyyaml`.

**Python Code to Convert XML to YAML:**
```python
import yaml

# Convert data to YAML and save
with open('network_config.yaml', 'w') as yaml_file:
    yaml.dump(network, yaml_file, default_flow_style=False)
```

## Conclusion

Congratulations! You've successfully transformed data from XML format to both JSON and YAML using Python. Such skills are vital in today's IT world, where data flexibility and interoperability are paramount. Continue to practice and experiment with various data formats to enhance your proficiency!
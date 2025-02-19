import xml.etree.ElementTree as ET

tree = ET.parse('network_config.xml')
root = tree.getroot()

for router in root.findall('router'):
    router_name = router.find('hostname').text
    for interface in router.find('interfaces').findall('interface'):
        iface_name = interface.find('name').text
        ip = interface.find('ip_address').text
        print(f"{router_name}, Interface {iface_name} has IP: {ip}")
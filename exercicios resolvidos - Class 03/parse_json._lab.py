import json


with open('network_config.json', 'r') as file:
    data = json.load(file)


for router in data['routers']:
    router_name = router['hostname']
    for interface in router['interfaces']:
        iface_name = interface['name']
        ip = interface['ip_address']
        subnet = interface['subnet_mask']
        print(f"{router_name}, Interface {iface_name} has IP: {ip} {subnet}")


import xmltodict

with open('network_config.xml', 'r') as file:
    data = xmltodict.parse(file.read())

for router in data['network']['router']:
    router_name = router['hostname']
    # A chave 'interfaces' contém um dicionário com a lista 'interface'
    for interface in router['interfaces']['interface']:
        iface_name = interface['name']
        ip = interface['ip_address']
        print(f"{router_name}, Interface {iface_name} has IP: {ip}")

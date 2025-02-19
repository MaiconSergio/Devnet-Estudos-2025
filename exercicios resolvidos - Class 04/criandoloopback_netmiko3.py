from netmiko import ConnectHandler

#new Loopback

loopback  = { 
'int_name': "Loopback01",
"description": "criando loopback",
"ip": "10.10.10.2",
"netmask": "255.255.255.0"
}

interface_config = [
    f"interface {loopback['int_name']}", 
    f"description {loopback['description']}",
    f"ip address {loopback['ip']} {loopback['netmask']}",
    "no shutdown"
]

device = {
    'device_type': 'cisco_xe',
    'ip': '10.10.20.48',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22,          # Default SSH port
    'secret': '',        # Optional, in case of enable password
    'verbose': False     # Optional, set to True for verbose logs
}

# Create a connection
connection = ConnectHandler(**device)

# Execute command and retrieve output

output = connection.send_config_set(interface_config)



# Close the connection
connection.disconnect()


# Print the output
print("A seguinte configuração foi aplicada: ")
print(output)

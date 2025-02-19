from netmiko import ConnectHandler


# Device details
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

output = connection.send_command('show ip int brief', use_textfsm=True)



# Close the connection
connection.disconnect()



# Print the output
target_interface = input("Digite a interface desejada: ")
interface_found = False
for entry in output:
    
    if entry['interface'] == target_interface:
        interface_found = True
        intf = entry['interface']
        ip = entry['ip_address']
        statu = entry['status']
        protocol = entry ["proto"]
        print (f"a interface name {intf} possui o ip {ip} e o status da interface é {statu} {protocol}")
        break

if not interface_found: 
    print(f"interface {target_interface} não existe")
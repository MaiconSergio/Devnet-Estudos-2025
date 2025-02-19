from netmiko import ConnectHandler
import sys

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

device2 = {
    'device_type': 'cisco_xe',
    'ip': '10.10.20.35',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22,          # Default SSH port
    'secret': '',        # Optional, in case of enable password
    'verbose': False     # Optional, set to True for verbose logs
}


# Create a connection
connection = ConnectHandler(**device)
connection2 = ConnectHandler(**device2)
# Execute command and retrieve output

output = connection.send_command('show run')
output2 = connection2.send_command('show run')


# Close the connection
connection.disconnect()
connection2.disconnect()

# Print the output
print(output)
print(output2)

with open('config_interface.txt', 'w') as file:
    sys.stdout = file

    print(f"show run dos seguintes dispositivos {output} \n \n \n \n {output2}")
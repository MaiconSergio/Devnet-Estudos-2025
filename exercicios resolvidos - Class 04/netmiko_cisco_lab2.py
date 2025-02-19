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



# Create a connection
connection = ConnectHandler(**device)

# Execute command and retrieve output

output = connection.send_command('show ip int brief', use_textfsm=True)



# Close the connection
connection.disconnect()


# Print the output
print(type(output))
#print(output)

for entry in output:
    int = entry['interface']
    ip = entry['ip_address']
    status = entry['status']

    print (f"a interface {int} possui o ip {ip} e o status da interface é {status}")
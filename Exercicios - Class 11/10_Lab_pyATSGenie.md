# Lab 10: Cisco's Genie

## Objective:

In this lab, you will learn how to set up and use Cisco Genie to interact and automate tasks on Cisco IOSXE devices.

### Prerequisites:

Have access to an IOSXE device, either reserved on DevNet or one of the "always-on" devices. Ensure you have a stable connection to the IOSXE device. If using a reserved device, you may need to use Cisco AnyConnect to establish a VPN connection. Instructions for this can be found in the DevNet sandbox.

## Steps

### 1. **Initial Check**:

Verify the connection to the IOSXE device and ensure all accesses are working correctly.

### 2. **Setting Up the Environment**:

Remember to check if you are in the Python virtual environment.
Install Genie and the required pyATS library using the following command:
```bash
pip install genie pyats.contrib
```

### 3. **Verifying the Installation**:

To ensure everything is set up correctly, you can test Genie using:
```bash
genie --help
```

### 4. **Creating the Testbed File**:

You'll need to create a testbed file for Genie. Follow the interactive prompts below:
```bash
genie create testbed interactive --output yaml/testbed.yml --encode-password
```

While running the command, you will see the following prompts:
```bash
Start creating Testbed yaml file ...
Do all of the devices have the same username? [y/n]
Do all of the devices have the same default password? [y/n]
Do all of the devices have the same enable password? [y/n]

Device hostname: [DEVICE]
   IP (ip, or ip:port): [IP]
   Username: [USERNAME]
Default Password (leave blank if you want to enter on demand): [PASSWORD]
Enable Password (leave blank if you want to enter on demand):
   Protocol (ssh, telnet, ...):
   OS (iosxr, iosxe, ios, nxos, linux, ...):
More devices to add ? [y/n]
Testbed file generated:
yaml/testbed.yml
```

### 5. **Testing Data Collection**:

Now, you can test data collection from the device using Genie:
```bash
genie parse "show version" --testbed-file yaml/testbed.yml --devices [DEVICE]
```

**Note**: The system may prompt for an enable password. If you're using DevNet, simply press the Enter key when prompted.

## Conclusion

Upon completing this lab, you will have a basic understanding of how to set up and use Cisco Genie to interact with Cisco IOSXE devices.
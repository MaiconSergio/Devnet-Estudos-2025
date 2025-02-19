# Lab 11: Diff Config

## Objective:

In this lab, you will learn how to compare configurations using Cisco Genie. You'll capture the configuration of a specific interface, modify its settings, capture the configuration again, and then compare the two configurations to see what changed.

## Steps

### 1. **Select an Interface**:

Start by selecting an interface on your IOS device that you'd like to monitor. This can be done either through SSH or the device's web interface (WebUI).

### 2. **Capture Initial Configuration**:

Once you've selected your interface, you can use the following Genie command to capture its configuration and save the output:

```bash
genie parse "show ip interface [INTERFACE_NAME]" --testbed-file yaml/testbed.yml --devices [DEVICE] --output [OUTPUT_FILE_1]
```
Replace `[INTERFACE_NAME]` with the name of your chosen interface (e.g., `loopback 109`) and `[OUTPUT_FILE_1]` with the desired name for your initial output file.

### 3. **Modify the Interface**:

Now, make some changes to the configuration of the interface you selected. This can be done either via SSH or through the WebUI.

### 4. **Capture the Modified Configuration**:

After making changes, capture the configuration of the interface again using Genie:

```bash
genie parse "show ip interface [INTERFACE_NAME]" --testbed-file yaml/testbed.yml --devices [DEVICE] --output [OUTPUT_FILE_2]
```
Make sure to replace `[INTERFACE_NAME]` as before and `[OUTPUT_FILE_2]` with the desired name for your modified output file.

### 5. **Compare the Configurations**:

With both configurations captured, you can use Genie to compare the two files and see what changed:

```bash
genie diff [OUTPUT_FILE_1] [OUTPUT_FILE_2]
```
Examine the differences displayed. If you can correctly identify the changes you made between the two captured configurations, then the comparison was successful.

## Conclusion

After completing this lab, you will have gained hands-on experience using Cisco Genie to capture and compare configurations, making it easier to identify and track changes in your network devices.


genie parse "show ip interface loop 109" --testbed-file yaml/testbed.yml --devices cat8000v --output interface-1
# Lab 08: Cisco's pyATS

## Objective:

In this lab, you'll set up and familiarize yourself with Cisco's pyATS, an automation and validation testing tool for networks.

**Note:** It's important to note that pyATS operates natively in Linux environments.

## Steps

### 1. **Environment Preparation**:
- Start by pulling the official pyATS image from Docker Hub:
```
docker pull ciscotestautomation/pyats
```

### 2. **Container Creation**:
- Create a container named `pyats_container`, connected to the host network, ensuring it can communicate with the network devices in your local environment:
```
docker run -it --name pyats_container --network host ciscotestautomation/pyats bash
```
After executing this command, you'll be logged into the container's bash shell.

### 3. **Accessing the pyATS Environment**:
- Activate the pyATS virtual environment using:
```
source bin/activate
```
- Verify that the pyATS tool is set up correctly by executing:
```
pyats --help
```
If everything is set up properly, you'll see the help message related to pyATS.

### 4. **Detaching and Re-attaching to the Container**:
Should you get detached from the container, reattach using the Docker exec command:
```
docker exec -it pyats_container bash
```

## Conclusion

In this lab, you've successfully set up Cisco's pyATS and have taken the initial steps to acquaint yourself with its functionalities.
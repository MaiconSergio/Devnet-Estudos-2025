# Lab 01: Building the Lab

## Objective

In this lab, our focus will be on creating and configuring two Docker Linux containers. Both containers will have an SSH server and will be on a custom Docker network named `my_network`. We'll also map the SSH ports of the containers to local ports 2221 and 2222.

## Note:
Elements described in this lab might already be created from previous labs and can be reused without any issues.

## Prerequisites:

Ensure Docker is installed on your machine.

## Steps:

### 1. **Building the Docker Image**:

- Start by creating a `Dockerfile` with the following content:

```Dockerfile
# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Update repositories and install OpenSSH server, ping utility, vim, and rsync 
RUN apt-get update && apt-get install -y openssh-server iputils-ping vim rsync

# Create an SSH user
RUN useradd -rm -d /home/hello -s /bin/bash -g root -G sudo -u 1000 hello

# Set the SSH user's password
RUN echo 'hello:password' | chpasswd

# Allow SSH access without a password for the hello user
RUN echo 'hello ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Allow SSH access
RUN mkdir /var/run/sshd

# Expose the SSH port
EXPOSE 22

# Start SSH server on container startup
CMD ["/usr/sbin/sshd", "-D"]
```

- In the directory where the `Dockerfile` is located, run the command to build the image:

```bash
docker build -t mypython_ssh .
```

### 2. **Setting up the Docker Network**:

- Create a Docker network named `my_network`:

```bash
docker network create my_network
```

### 3. **Launching the Containers**:

- Start the first container, named `controller`, mapping its SSH port to local port 2221:

```bash
docker run -d --name controller --network my_network -p 2221:22 mypython_ssh
```

- Start the second container, named `webserver`, mapping its SSH port to local port 2222 and its port 8080 to local port 8080:

```bash
docker run -d --name webserver --network my_network -p 2222:22 -p 8080:8080 mypython_ssh
```

### 4. **Verification**:

To ensure everything is working correctly, try to SSH into the containers using ports 2221 and 2222:

```bash
ssh hello@localhost -p 2221
```

and

```bash
ssh hello@localhost -p 2222
```

Use "password" as the password when prompted.

### 5. **Checking Inter-Container Connectivity**:

- To ensure the containers are communicating correctly with each other, SSH from the `controller` container to the `webserver` container:

```bash
# Access the 'controller' container
ssh hello@localhost -p 2221

# Once logged in, SSH to the 'webserver' from the 'controller'
ssh hello@webserver
```

Use "password" as the password when prompted.

### 6. **Ping Verification**:

To ensure network connectivity and ICMP responses are properly set up between the containers, use the `ping` command from the `controller` container to the `webserver`:

- First, access the `controller` container:

```bash
ssh hello@localhost -p 2221
```

- Once inside, execute the `ping` command with `-c 4` to send 4 ICMP echo requests:

```bash
ping -c 4 webserver
```

You should see replies from the `webserver` container, confirming that ICMP (ping) communication between the containers is functioning correctly.

## Conclusion:

In this lab, we successfully set up two Docker containers with SSH servers and verified their inter-communication. These containers are on a custom Docker network and have their SSH ports mapped to specific ports on our local machine.
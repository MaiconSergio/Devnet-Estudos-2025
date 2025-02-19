# Lab 05: Ansible Setup

In this lab, we will set up Ansible by creating a Docker image with Ansible installed and configuring a container to use Ansible.

## Steps

### 1. **Creating a Dockerfile**:

Create a Dockerfile with the following content and ensure that the other necessary files provided in previous labs are in the same folder:

```Dockerfile
# Use an official Ubuntu base image
FROM ubuntu:latest

# Install packages
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-add-repository --yes --update ppa:ansible/ansible && \
    apt-get install -y ansible openssh-server iputils-ping vim rsync

# Create an SSH user
RUN useradd -rm -d /home/hello -s /bin/bash -g root -G sudo -u 1000 hello

# Set the SSH user's password
RUN echo 'hello:password' | chpasswd

# Allow SSH access without a password for the hello user
RUN echo 'hello ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

# Allow SSH access
RUN mkdir /var/run/sshd

# Create the webserver file structure
WORKDIR /home/hello/my_hello_app
COPY hello_app.py .
COPY templates/index.html templates/

# Change ownership and permissions
RUN chown -R hello:root /home/hello/my_hello_app
RUN chmod -R 755 /home/hello/my_hello_app

# Expose the SSH port
EXPOSE 22

# Start SSH server on container startup
CMD ["/usr/sbin/sshd", "-D"]
```

### 2. **Build the Docker Image**:

Build a Docker image named `myansible` from the Dockerfile:

```bash
docker build -t myansible .
```

### 3. **Creating and Configuring the Ansible Container**:

Run the following command to create and configure a container from the `myansible` image. This will also map the SSH port to your local machine's port 2223 and connect the container to the `my_network` network:

```bash
docker run -d --name ansible-controller --hostname ansible-controller --network my_network -p 2223:22 myansible
```

This starts the Ansible container with the specified configurations. You can now connect to it using SSH locally on port 2223. Ensure that the `my_network` network is correctly set up so the container can communicate with other containers on the same network.

### 4. **Testing Ansible**:

While logged in via SSH to the Ansible container, you can test Ansible by running the following command to check the Ansible version:

```bash
ansible --version
```

This should display information about the installed Ansible version.

## Conclusion

In this lab, you have successfully set up an Ansible container using Docker. This setup enables you to deploy or maintain remote systems or devices using Ansible. You can now use Ansible playbooks and modules to manage configurations and automate tasks on your infrastructure.
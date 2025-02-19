# Lab 08: Deploying a Web Server with Ansible and Docker

## Objective:

The goal of this lab is to deploy a functional web server using only Ansible while leveraging Docker. By the end of the lab, you should have a running Flask web application inside a Docker container, all set up and configured using Ansible playbooks.

## Prerequisites:

- Ensure that both Ansible and Docker are installed on your Linux machine. This lab assumes a Linux-based environment for smoother interoperability between Ansible and Docker.

## Challenge Steps:

### 1. **Deploy a Docker Container**:

Begin by deploying a Docker container using the official `python:3.9-slim` image. This container will serve as our web server. You must expose ports 2222 for SSH and 8080 for the web application.

### 2. **Set Up the Environment**:

Inside the container:
- Install necessary packages: `openssh-server`, `iputils-ping`, `vim`, and `rsync`.
- Create a user named `hello`.

### 3. **Set Up SSH Access**:

Start the SSH server inside the container and ensure it can accept connections.
You can use this SSH access for subsequent Ansible tasks on the container.

### 4. **Configure the Web Application**:

Inside the container:
- Install Flask using `pip`.
- Deploy a Flask web application.
- Ensure the Flask application is running and can be accessed via port 8080.

### 5. **Testing**:

Once your playbook is complete, run it. After execution, access the Flask web application by visiting `http://localhost:8080` in a web browser. You should see the "Hello World!" message displayed.

### Tips:

- For the Docker-related tasks, you might find Ansible's `docker_container` and `docker_image` modules particularly useful.
- For in-container configurations, you can either use `docker exec` with the `command` module or SSH into the container and use Ansible's native modules.

## Conclusion

This lab emphasizes the power of Ansible in automating complex tasks. Deploying a web server involves several configuration steps, and using Ansible alongside Docker makes the process consistent and repeatable. Once you've set up the playbook, deploying another instance in the future becomes a trivial task.
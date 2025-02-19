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
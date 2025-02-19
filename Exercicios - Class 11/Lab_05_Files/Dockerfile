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
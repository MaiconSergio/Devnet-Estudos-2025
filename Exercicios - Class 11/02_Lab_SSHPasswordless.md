# Lab 02: Configuring Passwordless SSH Authentication Between Containers

## Objective

In this lab, we will learn how to configure passwordless SSH authentication between two Docker containers. This allows the containers to communicate without the need for password authentication.

## Steps:

### 1. **Generate SSH Key Pair on the controller Container**:

- Start by generating an SSH key pair (public and private keys) on the `controller` container. Use the following command:

```bash
ssh-keygen
```

- You can press Enter for all prompts to accept the default values.

### 2. **Copy the Public Key to the webserver Container**:

- Next, copy the public key to the `webserver` container. Use the following command to copy the public key to the `webserver` container:

```bash
ssh-copy-id hello@webserver
```

- Press Enter to accept the default file (`~/.ssh/id_rsa.pub`) when prompted.

### 3. **Test Passwordless SSH Connection**:

- Now that the public key is added to the `webserver` container's authorized keys, test the passwordless SSH connection.

- From the `controller` container, try SSHing into the `webserver` container:

```bash
ssh hello@webserver
```

- You should be able to log in without being prompted for a password.

## Conclusion

In this lab, we've successfully configured passwordless SSH authentication between two Docker containers. This eliminates the need for password authentication, simplifying the process of communication between containers. By following these steps, you can enhance the convenience and security of communication between containers within your Docker environment.
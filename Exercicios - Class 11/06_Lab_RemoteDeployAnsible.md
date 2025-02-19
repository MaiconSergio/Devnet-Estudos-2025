# Lab 06: Web Server Configuration with Ansible

In this lab, we will configure a web server and then automate this process using Ansible.

## Steps

### 1. **Running the Web Server**:

First, let's set up a web server manually. Run the following command to start the web server in a container:

```bash
docker run -d --name webserver --network my_network -p 2222:22 -p 8080:8080 mypython_ssh
```

This starts the `webserver` on port 8080 and sets up port redirection for SSH on port 2222 to allow SSH access.

**Note**: If you have already created the `webserver` container previously and want to use the same one, make sure to delete the files from `my_hello_app` and uninstall Flask before proceeding.

### 2. **Setting Up SSH Authentication**:

In this step, we'll configure SSH authentication between the `controller` and `webserver` containers.

1. **Generate SSH Key Pair**:
   - If not already done, generate an SSH key pair on the `controller` container:
     ```bash
     ssh-keygen
     ```

2. **Copy Public Key**:
   - Copy the public key (`id_rsa.pub`) to the `webserver` container:
     ```bash
     ssh-copy-id hello@webserver
     ```

3. **Test SSH Connection**:
   - Verify the SSH connection between the `controller` and `webserver` containers:
     ```bash
     ssh hello@webserver
     ```
     
   - You should now be able to SSH into the `webserver` container without entering a password.

### 3. **: Verify File Structure on Ansible Server**:

Ensure that our project directory on the Ansible server is organized as follows:

```plaintext
~/my_hello_app
│
├── hello_app.py
│
└── templates
    └── index.html
```

The files should be located in the home directory of the user 'hello' and have the same structure as mentioned above.

### 4. **Create Ansible Playbook**:

Now, let's create an Ansible playbook (e.g., `webserver_setup.yml`) with the following tasks:

```yaml
---
- name: Web Server Configuration
  hosts: webserver
  become: no
  tasks:
    - name: Check if Flask is installed
      command: "pip3 show flask"
      ignore_errors: yes
      register: flask_installed

    - name: Install Flask
      command: "pip3 install flask"
      when: flask_installed.rc != 0

    - name: Copy my_hello_app
      synchronize:
        src: /home/hello/my_hello_app/
        dest: /home/hello/my_hello_app/
      delegate_to: localhost
      register: file_changed

    - name: Check if Flask app is running
      shell: "pgrep -f hello_app.py"
      ignore_errors: yes
      register: flask_running

    - name: Stop the Flask application
      shell: "pkill -f hello_app.py"
      ignore_errors: yes
      when: file_changed.changed == true

    - name: Stop and Start Flask Application
      shell: "nohup python3 /home/hello/my_hello_app/hello_app.py > /dev/null 2>&1 &"
      when: file_changed.changed == true or flask_running.stdout_lines | length == 1
```

This Ansible playbook performs the following tasks:
- Checks if Flask is installed.
- Installs Flask if it's not installed.
- Copies the `my_hello_app` directory to the server if Flask is installed.
- Checks if the Flask app is running.
- Stops the Flask app if there are changes in the `my_hello_app` directory.
- Restarts the Flask application if there are changes or if it's not running.

You can use this playbook to automate the configuration of your web server.

### 5. **Running the Ansible Playbook**:

Execute the Ansible playbook with the following command:

```bash
ansible-playbook -i 'webserver,' webserver_setup.yml
```

This will run the playbook on the `webserver` host you created and automatically configure the web server based on the tasks defined in the playbook.

### 6. **Accessing the Web Page**:

To access the web page, open a web browser on your local machine and enter the following URL:

http://localhost:8080

Press Enter to access the web page. You should see the "Hello World!" message displayed.

## Conclusion

Automation with Ansible is a powerful and efficient way to manage and configure remote servers and services. In this lab, we demonstrated how to set up a web server and automate its configuration using Ansible. By defining tasks in Ansible playbooks, you can ensure consistent and reproducible server configurations, making it easier to manage and scale your infrastructure. As you continue to explore and utilize Ansible, you'll discover its versatility and value in automating and simplifying various aspects of system administration and infrastructure management.
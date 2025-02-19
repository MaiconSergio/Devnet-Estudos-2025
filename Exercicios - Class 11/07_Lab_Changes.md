# Lab 07: Restoring Web Server Configuration with Ansible

In this lab, we'll simulate various web server misconfiguration scenarios. Then, we'll use Ansible to restore the original setup and observe its behavior.

### Restoration using Ansible:

To restore settings after any induced failure:

- Run the Ansible playbook with the command:
  ```bash
  ansible-playbook -i 'webserver,' webserver_setup.yml
  ```

- After executing, access http://localhost:8080 and check if the configuration has been restored correctly.

## Test Suggestions:

Each of the following tests can be executed individually and then restored with Ansible, or you can combine multiple tests to see how Ansible handles simultaneous misconfigurations.

### 1. **Modify Files in Controller and Restore with Ansible**:

- Make changes to the `hello_app.py` or `index.html` file in the `controller` container.
- Run the Ansible playbook:
  ```bash
  ansible-playbook -i 'webserver,' webserver_setup.yml
  ```

- Visit http://localhost:8080 to observe the behavior.
- Revert the changes made to the `hello_app.py` or `index.html` in the `controller` container.
- Run the Ansible playbook again to observe the restoration.

### 2. **Stop the Flask App on Web Server**:

- Use the command to stop Flask:
  ```bash
  pkill -f hello_app.py
  ```

- Check the web server's status at http://localhost:8080.

### 3. **Remove Flask using pip on Web Server**:

- Uninstall Flask with:
  ```bash
  pip3 uninstall flask -y
  ```

- Try manually starting the `hello_app.py`.

### 4. **Remove Files on the Web Server**:

- Delete the `my_hello_app` directory:
  ```bash
  rm -rf /home/hello/my_hello_app/
  ```

## Conclusion

Ansible is a powerful tool that ensures rapid restoration of desired configurations on our servers, even after mishaps or misconfigurations. This lab underscored its ability to handle diverse scenarios and ensure service consistency and availability.
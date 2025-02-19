# Lab 04: Remote Web Server Deploy

In this lab, we will set up the `webserver` container and use a deployment script to manage the Flask application.

## Steps

### 1. **Preparing the webserver Container**:

Ensure that the `webserver` container is running and accessible via SSH. You can refer to the previous labs for instructions on setting up SSH access.

### 2. **Preparing the Project Structure**:

Make sure the project structure on the `controller` container is organized as follows:

```plaintext
~/my_hello_app
│
├── hello_app.py
│
└── templates
    └── index.html
```

### 3. **Deployment Script**:

You can use the provided deployment script to manage your Flask application remotely.
Create a new script file, e.g., `remote_deploy_webserver.sh`, on the `controller` container and add the following content:

```bash
#!/bin/bash

# Define a variable to keep the current log
current_log=""

# Define the function to add logs to the log file
log() {
    current_log="$current_log$(date +"%Y-%m-%d %H:%M:%S") - $1"$'\n'
}

# 'webserver' container variable
WEBSERVER="webserver"

# Ensure the log directory exists and start logging
mkdir -p ~/log
echo "-------------------" >> ~/log/deploy.log

# Check if Flask is installed on the 'webserver' and install if not
FLASK_INSTALLED=$(ssh $WEBSERVER 'pip3 show flask')
if [ -z "$FLASK_INSTALLED" ]; then
    ssh $WEBSERVER 'pip3 install flask'
    log "Flask was not installed on the $WEBSERVER and has been installed."
else
    log "Flask is already installed on the $WEBSERVER."
fi

# Check for differences and use rsync to update the remote 'webserver'
RSYNC_OUTPUT=$(rsync -avz --dry-run -e "ssh" ~/my_hello_app/ hello@$WEBSERVER:/home/hello/my_hello_app/ 2>&1)

if [[ $RSYNC_OUTPUT == *"hello_app.py"* || $RSYNC_OUTPUT == *"index.html"* ]]; then
    rsync -avz -e "ssh" ~/my_hello_app/ hello@$WEBSERVER:/home/hello/my_hello_app/
    log "Files were updated on the $WEBSERVER."

    # Starting or restarting the Flask application on the 'webserver'
    ssh $WEBSERVER 'pkill -f hello_app.py'
    ssh $WEBSERVER 'nohup python3 /home/hello/my_hello_app/hello_app.py > /dev/null 2>&1 &'
    log "Flask application started/restarted on the $WEBSERVER."

else
    # Check if Flask is running on the 'webserver'
    if ! ssh $WEBSERVER 'pgrep -f hello_app.py'; then
        # If Flask is not running, start it
        ssh $WEBSERVER 'nohup python3 /home/hello/my_hello_app/hello_app.py > /dev/null 2>&1 &'
        log "Flask application was not running and has been started on the $WEBSERVER."
    else
        log "No changes detected, and Flask is already running. Nothing was done."
    fi
fi

# Add the current log to the log file and clear it
echo -e "$current_log" >> ~/log/deploy.log
```

### 4. **Running the Deployment Script**

Make sure the deployment script (`remote_deploy_webserver.sh`) is executable:

```bash
chmod +x remote_deploy_webserver.sh
```

Now, you can execute the deployment script to update and manage the Flask application on the 'webserver' container:

```bash
./remote_deploy_webserver.sh
```

The script will handle updating files, installing Flask if needed, and starting/restarting the Flask application. It will also log its actions in the `deploy.log` file.

### 5. **Accessing the Web Page**:

Open a web browser on your local machine and enter the following URL in the address bar:

```
http://localhost:8080
```

Press Enter to access the web page. You should see the "Hello World!" message displayed.
You have successfully set up the `webserver` container and can remotely manage your Flask application using the provided deployment script.

## Conclusion

In this lab, you have learned how to set up a remote `webserver` container, and use a remote deployment script to manage your Flask application.
This setup enables you to deploy or maintain remote systems or devices.
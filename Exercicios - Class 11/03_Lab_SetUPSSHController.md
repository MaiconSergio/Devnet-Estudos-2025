# Lab 03: Setting Up the Controller Environment

## Objective

In this lab, you will prepare the Controller environment by configuring the `hello_app.py` and `index.html` files to be sent to the Webserver.

## Steps

### 1. **Project Structure**:

- Ensure our project directory is organized as follows:

```plaintext
~/my_hello_app
│
├── hello_app.py
│
└── templates
    └── index.html
```

**Description**:
- **hello_app.py**: Main Python script containing the Flask application.
- **templates**: Directory for HTML templates. Flask follows this convention to locate templates.

### 2. **Writing the Flask Application**:

In the `hello_app.py` file, use the following code:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

This Flask application renders the `index.html` template when accessed.

### 3. **Creating the HTML Template**:

Inside the `~/my_hello_app/templates` directory, create a file named `index.html` and paste the following HTML code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World Example</title>
    <style>
        body {
            background-color: black;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        h1 {
            font-family: "Courier New", monospace;
            font-size: 48px;
            color: #00FF00;
        }
    </style>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

### 4. **Verification**:

- Verify that the directory structure and files were created correctly using the `ls` commands:

```bash
ls ~/my_hello_app
ls ~/my_hello_app/templates
```

## Conclusion

In this lab, you prepared the Controller environment by creating the `hello_app.py` and `index.html` files that will be sent to the Webserver in the next lab. Ensure that the files are correctly organized before proceeding to the next step of the project.
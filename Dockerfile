# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY hello_app.py /app
COPY templates /app/templates

# Install Flask
RUN pip install flask

# Expose port 8080 to the outside
EXPOSE 8080

# Define environment variable (optional)
ENV NAME World

# Run the application upon container startup
CMD ["python", "hello_app.py"]
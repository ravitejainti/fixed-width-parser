# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all the files from the current directory to /app inside the container
COPY . .

# Run the parser script when the container starts
CMD ["python", "parser.py"]

# Use an official Ubuntu base image
FROM ubuntu:22.04

# Install Python and other dependencies
RUN apt-get update && apt-get install -y python3 python3-pip unzip curl fontconfig && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application code and requirements file
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Flask application
CMD ["gunicorn", "app.__main__:app", "--workers", "3", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
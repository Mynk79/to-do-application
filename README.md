# To-do Application (FastAPI)

This is the source code for the [CRUD API's](https://github.com/Mynk79/to-do-application). The course is meant for learning how to implement HTTP methods (POST, GET, PUT, PATCH, UPDATE) in the backend of the application.

## Table of Contents

1. [Getting-Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Project Setup](#project-setup)
4. [Running the Application](#running-the-application)


### Getting Started
Follow the instructions shown below to setup and run the project.

### Prerequisites
Ensure you have the following installed:
- Python >= 3.10

### Project Setup
1. Clone the project repository:
    ```bash
    git clone https://github.com/Mynk79/to-do-application.git
    ```

2. Navigate to the project directory
    ```bash
    cd to-do-application/
    ```

3. Create and activate a virtual environment (For Linux/Mac):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### Local Environment
Start the Application:
```bash
python3 main.py
```

or using:
```bash
python3 -m app
```

or using:
```bash
uvicorn app.__main__:app --host 0.0.0.0 --port 8000
```

### Production Environment
Start the application:
```bash
gunicorn -w 3 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app.__main__:app
```

Alternatively, you can start the application using **Docker** by:

```bash
docker build -t to-do-app .
docker run -p 8000:8000 to-do-app
```

### Postman API Collection

You can use the Postman API collection to test the API's by importing the collection into Postman.



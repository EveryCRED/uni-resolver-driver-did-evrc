# EveryCRED EVRC DID Method Driver

## 🛠 Skills
Python, Fast-API, Swagger Doc.

## Install + configure the project

### 1. Linux
```
# Create python virtual environment
python3 -m venv venv

# Activate the python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt

# Install the dependencies of Fast API
pip install "fastapi[all]"

# Upgrade pip version
python -m pip install --upgrade pip==22.1.2
```
### 2. Windows
```
# Create python virtual environment
conda create --name venv python=3.10.12

# Activate the python virtual environment
conda activate venv

# Install the requirements for the project into the virtual environment in the following sequence:
pip install -r requirements.txt

# Install the dependencies of Fast API
pip install "fastapi[all]"

# Upgrade pip version
python -m pip install --upgrade pip==22.1.2
```

## Run the server in development mode
Run the server
```
python asgi.py
```
Browse Swagger API Doc at: http://localhost:8080/docs
Browse  Redoc at: http://localhost:8080/redoc

## Release History

* 1.0
    * Work in progress
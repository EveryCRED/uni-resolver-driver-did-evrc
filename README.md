# EveryCRED EVRC DID Method Driver
EVERYCRED is an exceptionally adaptable platform for the issuance, viewing, and verification of credentials. Notably, this platform is structured around the fundamental concepts of DID (Decentralized Identifiers) and W3C Verifiable Credentials, embracing cutting-edge technology and gametics.

### Issuer DID

To represent organization as the issuer of credentials, we generates the following DID for each issuer:

- DID: `did:evrc:issuer:{Blockchain Network}:{Unique ID}`
- Description: This DID uniquely identifies issuers within the decentralized identity ecosystem.

### Holder DID

For each credential recipient, we assign a DID that represents them in our system. As an example, here's the holder's DID for Jane Doe:

- DID: `did:evrc:holder:{Unique ID}`
- Description: This DID is linked to Jane Doe and is used to associate her with the credentials issued by issuer.

Please replace these example DIDs and descriptions with your actual DIDs and relevant information as needed and resolve the did.

### Example DID's
- Issuer DID: did:evrc:issuer:ethereum:246d9b34-09e1-496e-ad5b-fb5ea889d96b
- Holder DID: did:evrc:holder:6c8ab8b9-daec-4e65-91de-5ac5019f69f2

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
# 3. Docker
```
# Create docker image
docker image build -t uni-resolver-driver-did-evrc .

# Create docker container
docker run -p 8145:8080 -d uni-resolver-driver-did-evrc
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
 
## Contact us
- Website-site: https://everycred.com/
- Organization Website: https://viitorcloud.com/

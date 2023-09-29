import json
import requests
from fastapi import HTTPException
from config import env_config
from fastapi_utils.inferring_router import InferringRouter

## Load API's
router = InferringRouter()

@router.get("/1.0/identifiers/{identifier}")
async def get_did(identifier: str):
    """
    This API responds to a dirver of evrc and request for /identifiers/{identifier}
    to get the information of evrc identifier.
    """ 
    # API route
    CRED_API_ROUTE = f'{env_config.EVERYCRED_API_ROUTE}/{identifier}'
    
    response = requests.get(CRED_API_ROUTE)
    identifier = json.loads(response.content.decode())

    if response.status_code == 400:
        return "Invalid Input"
    
    if response.status_code != 200:
        return "Invalid DID"
    
    if response.json()['status'] != 200:
        return response.json()['message']
    
    identifier_data = response.json().get('data')['did_data']

    return identifier_data
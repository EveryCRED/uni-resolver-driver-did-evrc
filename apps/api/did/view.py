import aiohttp
from fastapi import APIRouter
from config import env_config

## Load API's
router = APIRouter()

@router.get("/1.0/identifiers/{identifier}")
async def get_did(identifier: str):
    """
    This API responds to a request for /identifiers/{identifier}
    to get the information of evrc identifier.
    """
    CRED_API_ROUTE = f'{env_config.EVERYCRED_API_ROUTE}/{identifier}'

    error_response = {
        "@context": "https://w3id.org/did-resolution/v1",
        "didDocument": None,
        "didResolutionMetadata": {
            "error": "notFound",
            "errorMessage": "404 Not Found",
            "contentType": "application/did+ld+json"
        },
        "didDocumentMetadata": {}
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(CRED_API_ROUTE) as response:
            if response.status != 200:
                return error_response
            
            identifier_data = await response.json()

    return identifier_data
from fastapi import FastAPI 
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


##### CORS configuration #####
CORS_ALLOW_ORIGINS = ["*"]

CORS_ALLOW_METHODS = ["*"]

CORS_ALLOW_HEADERS = ["*"]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=CORS_ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=CORS_ALLOW_METHODS,
        allow_headers=CORS_ALLOW_HEADERS
    )
]
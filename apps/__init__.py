from config import cors
from fastapi import FastAPI
from apps.api.did.view import router


# Create app object and add routes
app = FastAPI(title="EveryCRED EVRC Driver", middleware=cors.middleware)

# # define router for different version
app.include_router(router)
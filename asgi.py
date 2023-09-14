import os
import uvicorn
from apps.__init__ import app

if __name__ == "__main__":
    uvicorn.run("asgi:app",
                host="127.0.0.1",
                port=8080,
                reload=False)
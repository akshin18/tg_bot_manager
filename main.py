import uvicorn
import os
import webbrowser
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(
    description="This is to test",
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/",StaticFiles(directory=static_dir, html=True),name="static")

def start_server():

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True,
    )

if __name__ == "__main__":
    start_server()
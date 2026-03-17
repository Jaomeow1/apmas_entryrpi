# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database import init_firebase
from routers import entrance, tickets, slots
import os

app = FastAPI(title="APMAS Parking API")

# CORS — เติม origins ที่อนุญาต
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "YOUR_GITHUB_PAGES_URL",   # e.g. https://yourname.github.io
        "YOUR_SERVER_URL",         # e.g. http://192.168.x.x
        "YOUR_SERVER_URL_PORT",    # e.g. http://192.168.x.x:8000
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1",
        "null"
    ],
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)

os.makedirs("static/images",  exist_ok=True)
os.makedirs("static/qrcodes", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"),        name="static")
app.mount("/images", StaticFiles(directory="static/images"), name="images")

app.include_router(entrance.router, prefix="/api")
app.include_router(tickets.router,  prefix="/api")
app.include_router(slots.router,    prefix="/api")

@app.on_event("startup")
def startup():
    init_firebase()
    from routers.tickets import start_slot_watcher
    start_slot_watcher()
    print("[Server] Ready")

@app.get("/")
def root():
    return {"status": "APMAS Parking Server running"}

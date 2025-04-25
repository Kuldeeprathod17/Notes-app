from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# Add GZip compression
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Include router
app.include_router(note)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

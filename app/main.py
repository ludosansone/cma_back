from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import course_routes, song_routes, instrument_routes, instructor_routes

app = FastAPI()

# Configuration CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(course_routes.router)
app.include_router(song_routes.router)
app.include_router(instrument_routes.router)
app.include_router(instructor_routes.router)

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API de Cover Academy"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.user import Base
from app.database import Base, engine
from app.schemas.user import UserCreate
from app.services.user_service import create_user

app = FastAPI()

# Crée les tables
Base.metadata.create_all(bind=engine)

@app.post("/auth/register")
def register(user: UserCreate):
    return create_user(user)

# Autoriser les origines spécifiques
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # ajoute ici ton futur domaine déployé si besoin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur CleanMySpace API 🧽"}

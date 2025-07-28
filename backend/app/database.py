# app/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Création de l'engine en mode async
engine = create_async_engine(
    DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"),
    echo=True
)

# Création du SessionLocal
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base pour les modèles ORM
Base = declarative_base()

# Dépendance pour FastAPI (à importer dans tes routes)
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

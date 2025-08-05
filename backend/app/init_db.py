from app.database import engine
from app.models.user import Base

# Crée toutes les tables définies via Base (inclut la table "users")
Base.metadata.create_all(bind=engine)

print("✅ Tables créées avec succès.")

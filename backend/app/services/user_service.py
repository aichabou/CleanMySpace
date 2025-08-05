from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user import UserCreate
from app.database import SessionLocal
from app.security import hash_password
from fastapi import HTTPException, status


def create_user(user: UserCreate):
    db: Session = SessionLocal()
    
    # Vérifier si l'email ou le username existe déjà
    existing_user = db.query(User).filter(
        (User.email == user.email) | (User.username == user.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ou nom d'utilisateur déjà utilisé."
        )

    # Hasher le mot de passe
    hashed_password = hash_password(user.password)

    # Créer l'utilisateur
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # ✅ Ne pas renvoyer le mot de passe
        return {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "created_at": new_user.created_at.isoformat()
        }

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la création de l'utilisateur."
        )
    finally:
        db.close()

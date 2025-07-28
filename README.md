# 🧽 CleanMySpace

CleanMySpace est une application web permettant aux individus, couples ou colocataires de **gérer les tâches ménagères**, suivre les responsabilités et organiser leur foyer de façon collaborative.


## ✨ Fonctionnalités clés (MVP)

- ✅ Création de compte utilisateur
- ✅ Création de foyer (optionnel si l’utilisateur veut rester seul)
- ✅ Ajout de membres dans un foyer
- ✅ Ajout, édition, suppression de tâches
- ✅ Attribution des tâches aux membres
- ✅ Statistiques simples de répartition des tâches
- ✅ Système de rappels

## 🧰 Stack technique

### Frontend
- React + Vite
- Tailwind CSS
- Zustand (state management)
- Axios (requêtes HTTP)

### Backend
- FastAPI (ASGI framework Python)
- Pydantic (validation)
- SQLAlchemy (ORM)
- PostgreSQL (base de données)
- Uvicorn (serveur de développement)

### DevOps & Outils
- Docker (containerisation)
- Docker Compose
- GitHub Actions (CI/CD)
- PostgreSQL via Docker
- pgAdmin pour l'administration BDD
- .env (gestion des secrets)

## ⚙️ Installation & lancement

### Prérequis

- Node.js (v18+)
- Python 3.9+
- Docker & Docker Compose
- PostgreSQL ou pgAdmin (local ou via Docker)

### Clonage

git clone https://github.com/aichabou/CleanMySpace.git
cd CleanMySpace


### Lancer le frontend

cd frontend
npm install
npm run dev

### Lancer le backend

cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


### 📦 Variables d’environnement
Copie le fichier .env.example dans le backend :
cp .env.example .env

### 📄 Licence
Projet personnel sous licence MIT.

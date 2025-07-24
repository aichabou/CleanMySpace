# 🧼 CleanMySpace

**CleanMySpace** est une application web destinée à aider les utilisateurs à organiser les tâches ménagères au sein d’un foyer (couple, colocataires ou en solo).  
Elle permet d’assigner, suivre et répartir les tâches de manière simple et collaborative.



## 🚀 Objectif du projet

- Créer un outil pour organiser les corvées à la maison
- Montrer mes compétences full-stack (frontend, backend, BDD, DevOps)
- Apprendre FastAPI, renforcer React, structurer un projet professionnel



## 🧰 Stack technique

| Partie        | Technologie utilisée        |
|---------------|-----------------------------|
| Frontend      | React + Vite + Tailwind CSS |
| Backend       | FastAPI + Pydantic + SQLAlchemy |
| Base de données | PostgreSQL               |
| Authentification | JWT (Token sécurisé)    |
| Conteneurisation | Docker + Docker Compose |
| Déploiement / DevOps | GitHub Actions (CI/CD à venir) |



## 📁 Structure du projet

```
cleanmyspace/
├── frontend/             # Interface utilisateur (React)
├── backend/              # API (FastAPI)
├── docker-compose.yml    # Orchestration des services
├── .env.example          # Fichier d'exemple d'environnement
└── README.md             # Documentation
```



## ▶️ Instructions de lancement rapide

1. **Cloner le projet**  
```bash
git clone https://github.com/votre-utilisateur/cleanmyspace.git
cd cleanmyspace
```

2. **Configurer les variables d’environnement**  
Créer un fichier `.env` dans le dossier `backend/` basé sur `.env.example`.

3. **Lancer le projet avec Docker**  
```bash
docker-compose up --build
```

- Frontend disponible sur : http://localhost:5173  
- Backend (API docs) sur : http://localhost:8000/docs



## 📄 Licence

Projet personnel sous licence MIT.

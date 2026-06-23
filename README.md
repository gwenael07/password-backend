# Password Generator - Backend API

Backend API développé avec Django et Django REST Framework pour la génération de mots de passe sécurisés et configurables. Ce projet fournit les points d'accès nécessaires au fonctionnement de l'application frontend.

## Technologies utilisées

* Python 
* Django 
* Django REST Framework
* django-cors-headers
* SQLite3 
* Déploiement : Render

## Fonctionnalités de l'API

* Génération de mots de passe basée sur des paramètres personnalisables (longueur, caractères spéciaux, chiffres, majuscules).
* Configuration CORS activée pour permettre les requêtes depuis le frontend Angular.
* Paramètres de sécurité configurés pour la production (DEBUG désactivé, gestion de la clé secrète via l'environnement).

## Installation et lancement en local

### 1. Clonage du dépôt
```bash
git clone [https://github.com/gwenael07/password-backend.git](https://github.com/gwenael07/password-backend.git)
cd password-backend

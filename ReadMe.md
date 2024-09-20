# User Management System avec Tkinter GUI

Bienvenue dans le **User Management System**! Ce projet fournit une interface graphique utilisateur (GUI) construite à l'aide de **Tkinter** qui permet aux utilisateurs de se connecter, et, si ils sont administrateurs, de gérer les utilisateurs (créer, modifier, supprimer) de manière simple et intuitive.

## Table des matières

- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Fonctionnalités

1. **Authentification utilisateur**: 
   - Users can log in with a username and password.
   - Admins are granted access to the full user management panel.

2. **Panneau d'administration**: 
   - Les administrateurs peuvent:
     - Créer de nouveaux utilisateurs.
     - Lister tous les utilisateurs.
     - Modifier l'email ou le mot de passe des utilisateurs.
     - Supprimer des utilisateurs.

3. **Sécurité du mot de passe**:
   - Les mots de passe sont hachés à l'aide de **bcrypt** pour garantir des pratiques de sécurité robustes.

4. **Persistance des données**:
   - Les données des utilisateurs sont stockées dans un fichier CSV (`users.csv`), garantissant une persistance des données entre les sessions.

5. **Interface Graphique Utilisateur**:
   - Le système utilise une **Interface Graphique Utilisateur** (GUI) avec **Tkinter** pour une interface utilisateur conviviale.

---

## Technologies

- **Python 3.x**
- **Tkinter** (for GUI)
- **Pandas** (for CSV data management)
- **Bcrypt** (for password hashing)
- **Pytest** (for testing)

---

## Installation

1. Cloner le dépôt sur votre machine locale:

```bash
git clone https://github.com/yourusername/user-management-system.git
cd user-management-system
```

2. Créer un environnement virtuel:

```bash
python -m venv venv
source venv/bin/activate
```

3. Installer les dépendances:

```bash
pip install -r requirements.txt
```

---

## Utilisation

Pour lancer l'interface graphique Tkinter, exécutez le fichier main.py:

```bash
python main.py
```

---

### Connexion:
- Entrez votre nom d'utilisateur et votre mot de passe pour vous connecter. Si aucun administrateur existe, le système vous demandera de créer un utilisateur.

### Fonctionnalités d'administration:
- Si vous vous connectez en tant qu'administrateur, vous aurez accès à:
  - Créer de nouveaux utilisateurs.
  - Voir la liste de tous les utilisateurs.
  - Modifier ou supprimer des utilisateurs.

### Actions du panneau d'administration:
- Créer un utilisateur: Remplissez les champs "Nom d'utilisateur", "Email" et "Mot de passe", puis cliquez sur "Créer utilisateur".
- Modifier un utilisateur: Fournissez le nom d'utilisateur de l'utilisateur que vous souhaitez modifier, puis entrez le nouvel email et/ou mot de passe.
- Supprimer un utilisateur: Entrez le nom d'utilisateur de l'utilisateur que vous souhaitez supprimer, puis cliquez sur "Supprimer utilisateur".
- Après avoir effectué une action, les champs de saisie seront automatiquement réinitialisés.

---

## Test

Pour exécuter les tests unitaires, utilisez la commande suivante:

```bash
pytest tests/test_user_management.py
```

---

## Contribution

Nous encourageons les contributions à ce projet! Si vous avez des idées ou des suggestions, veuillez ouvrir une issue ou soumettre une pull request.

---

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Mathieu Soussignan - 2024 - Simplon.co



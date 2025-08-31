# Recipe Manager

Recipe Manager is a full-stack web application built with **Django** (backend) and **TypeScript/JavaScript** (frontend) that allows users to manage recipes, including creating, editing, deleting, searching, and viewing ingredients. The app supports pagination, dynamic ingredient management, and multi-language support.

---

## Features

- **User Authentication**: Register, login, and logout.
- **Recipe Management**:
  - Add, edit, and delete recipes.
  - Upload a photo for each recipe.
  - Manage multiple ingredients per recipe dynamically.
- **Ingredient Management**:
  - Add ingredient details: amount, unit, and name.
  - Dynamic interface for adding/removing ingredients.
- **Recipe Listing**:
  - Paginated recipe list.
  - View recipe details including ingredients and image.
- **Search Functionality**:
  - Search recipes by name or ingredients.
  - Dynamic results with pagination.
- **Internationalization**:
  - Switch languages via a dropdown.
  - Session-based language updates.
- **Responsive Design**:
  - Works well on desktop, tablet, and mobile.
- **REST-like API**:
  - Supports delete operations and paginated recipe listing for dynamic frontend updates.

---

## Technologies

- **Backend**: Django 4.x, Python 3.12
- **Frontend**: TypeScript, JavaScript, Bootstrap 5
- **Database**: SQLite (default, can be replaced with any Django-supported DB)
- **Other**: JSON-based API endpoints, i18n support

---

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/philipp-meier/recipe-manager.git
   cd recipe-manager
2. Create a virtual environment and activate it

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


3. Install dependencies

pip install -r requirements.txt


4. Apply migrations

python manage.py migrate


5. Create a superuser (optional)

python manage.py createsuperuser


6. Run the development server

python manage.py runserver


7. Open the app in your browser

http://127.0.0.1:8000/



Usage

Register/Login to access recipe features.

Navigate to Recipes to view all recipes.

Click Add Recipe to create a new recipe.

Click a recipe to edit or view details.

Use the search bar to find recipes by name or ingredients.

Change language using the dropdown menu.

Navigate pages using pagination controls.

Project Structure
recipe-manager/
├── recipes/
│   ├── templates/
│   │   ├── layout.html
│   │   ├── recipe.html
│   │   └── recipelist.html
│   ├── static/
│   │   ├── recipes/
│   │   │   ├── recipeList.js
│   │   │   ├── ingredientsControl.js
│   │   │   └── styles.css
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── helper.py
│   └── urls.py
├── config/
│   ├── settings.py
│   └── urls.py
└── manage.py

Contributing

Fork the repository.

Create a new branch.

Make your changes.

Submit a pull request.
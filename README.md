# learningDjango

1. Create virtual environment -> uv venv
2. Activate venv -> .venv/Scripts/Activate.ps1
3. Install Django -> (uv add django) or (uv pip install Django)
4. Create Django Project -> django-admin startproject "projectname"
5. Run Django App -> python manage.py runserver <port_number>(optional)


Root Level -> manage.py
App Level
Inside Level
Project Level= chaiaurdjango/chaiaurjango

db.sqlite3  -> default database for Django.
settings.py -> manage configurations (project level)
urls.py     -> manages all routings
views.py    -> manages all controllers (contains business logic)
models.py   -> contains database models

flow: url->route->views 


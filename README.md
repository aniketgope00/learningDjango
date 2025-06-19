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

Templates and Errors:
(a) Create views.py
(b) Define functions in views.py
(c) Go to urls and add paths as path("<name>", views.<def_name>, name = <name>)
(d) Create templates and static directory in root folder
(e) Include 'templates' in DIRS:list in settings.py
(f) Templating Enging -> {%load static%}, {%static "style.css"%}
(g) Include static Path as STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] in settings.py
(h) Use render(request, <template_name>)


# learningDjango

1. Create virtual environment -> uv venv
2. Activate venv -> .venv/Scripts/Activate.ps1
3. Install Django -> (uv add django) or (uv pip install Django)
4. Create Django Project -> django-admin startproject "projectname"
5. Run Django App -> python manage.py runserver <port_number>(optional)


Root Level -> chaiaurdjango/manage.py
App Level
Project Level = chaiaurdjango/chaiaurjango

db.sqlite3  -> default database for Django.
settings.py -> manage configurations (project level)
urls.py     -> manages all routings
views.py    -> manages all controllers (contains business logic)
models.py   -> contains database models

flow: url->route->views 

Templates and Errors: <br>
(a) Create views.py <br>
(b) Define functions in views.py <br>
(c) Go to urls and add paths as path("<name>", views.<def_name>, name = <name>) <br>
(d) Create templates and static directory in root folder <br>
(e) Include 'templates' in DIRS:list in settings.py <br>
(f) Templating Enging -> {%load static%}, {%static "style.css"%} <br>
(g) Include static Path as STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] in settings.py <br>
(h) Use render(request, <template_name>) <br>

Jinja2:<br>
(a) Create new app: python manage.py startapp chai <br>
(b) Go to base app's settings.py -> add <app_name> to INSTALLED_APPS <br>
(c) Creating Templates inside app: templates/<app_name>/files (no need to configure settings.py in this case) <br>
(d) Once functions are created in views.py, copy urls.py from base app -> create urls.py in current app and paste contents <br>
(e) Pass control from project's urls.py to app's urls.py: import include -> path(<app_name>/, include(<app_name>.urls)) [DO this in base app's urls.py]<br>
(f) 



# Django Go Path 

```shell
django-admin startproject dj_project
```

```shell
dj_project/
├── manage.py
├── dj_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├─ settings.py
│   ├─ urls.py
│   ├── wsgi.py 
```

```shell
python3 manage.py startapp first_app
```

```shell
dj_project/
├── manage.py
├── dj_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├─ settings.py
│   ├─ urls.py
│   ├── wsgi.py
├── first_app/
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

Run django server with cmd
```shell
python3 manage.py runserver
```

Migrations to create migrations for those changes
```shell
python3 manage.py makemigrations
```

Migrate Run python manage.py migrate to apply those changes to the database. 
```shell
python3 manage.py migrate
```

Create a superuser for panel auth
```shell
python3 manage.py createsuperuser
```

```shell
python manage.py shell
```

## The main project directory

The main project directory in Django encapsulates the essence of your application. It’s the nucleus from which all functionalities radiate, shaping the entirety of your web venture. Within this directory reside several pivotal files, each bearing its significance in orchestrating the symphony of your development journey:

<br/><b>manage.py</b><br/>
This small but mighty script serves as the gateway to various Django management commands. It’s the tool through which you initiate the development server, create applications, run migrations, and more. manage.py is the conductor's baton, guiding your project's activities.
<br/><b>dj_project/settings.py:</b><br/>
As the name suggests, this file houses the settings that configure your Django project. From database configurations to middleware lists, this is where you define how your application functions. It’s akin to the blueprint that shapes the structure of your project’s behavior.
<br/><b>dj_project/urls.py</b><br/>
The URL dispatcher — encoded within urls.py—maps URLs to views. This file determines which view is displayed when a specific URL is accessed. It's like a roadmap that navigates users through the intricacies of your application's pages.
<br/><b>my_project/wsgi.py</b><br/>
Short for Web Server Gateway Interface, wsgi.py serves as the entry point for your application when deployed on a production server. It's the bridge connecting your application to the web server, enabling it to handle incoming requests.
<br/><b>my_project/asgi.py</b><br/>
Similar to wsgi.py, asgi.py is the entry point for asynchronous web servers. It stands for Asynchronous Server Gateway Interface and facilitates the handling of asynchronous HTTP requests.
<br/><b>my_project/__init__.py</b><br/>
This seemingly unassuming file holds the magic that transforms a directory into a Python package. It’s essential for organizing and importing modules across your project

# Directory Hierarchy

```shell
dj_project/
├── manage.py
├── dj_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├─ settings.py
│   ├─ urls.py
│   ├── wsgi.py
├── app1/
├── app2/
  ...
├── static/
├── media/
├── templates/
```
<br/>
<b>dj_project</b>:The root directory of your project.
<br/>
<b>project_name/project_name</b>: This inner directory holds core project settings and configuration.
<br/>
<b>app1, app2:</b> These are the individual apps you create within the project.
<br/>
<b>static:</b> Houses static files like CSS, JavaScript, and images.
<br/>
<b>media:</b> Stores user-uploaded files.
<br/>
<b>templates:</b> Contains HTML templates.
<br/>

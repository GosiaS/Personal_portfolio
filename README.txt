This page is heavily based on the tutorial from this page: https://realpython.com/get-started-with-django-1/#why-you-should-learn-django
I changed little in the core code, and I kept using Bootstrap as per tutorial - I focused on django core code, not the page layout
I added "my" page to the web, which is "store". It's not from any tutorial, but I was heavily inspired by uncle Google.

Commands to make it work on local environement:
    $ source venv/bin/activate
    (venv) $ python manage.py runserver
    open http://localhost:8000/projects/ in browser to navigate through the page

*you need to have django installed
    (venv) $ pip install Django

Commands that are good to know:
    $ django-admin startproject nazwa_projektu
    $ python manage.py startapp blog
        *new apps need to be added to INSTALLED_APPS in settings.py
    to migrate the data:
        $ python manage.py makemigrations projects
        $ python manage.py migrate projects
    to create instances of projects(or any data):
        $ python manage.py shell
        >>> from projects.models import Project
        example instance:
            >>> p1 = Project(
            ...     title='My First Project',
            ...     description='A web development project.',
            ...     technology='Django',
            ...     image='img/project1.png'
            ... )
            >>> p1.save()
    to enable adding instances for admin user within browser, not terminal
        $ python manage.py createsuperuser
        create username & password
        Navigate to localhost:8000/admin

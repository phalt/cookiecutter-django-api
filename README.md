# cookiecutter-django-api

This provides a cookiecutter template for a Django API project.

Featuring:

- Django 1.8
- Django REST Framework 3.1

## Installation:

1. Install [cookicutter](https://cookiecutter.rtfd.org).

2. Use cookiecutter to make a copy:

```
$ cookiecutter https://github.com/phalt/cookiecutter-django-api.git
project_name (default is 'project_name'):
```

3. Set things up:

```
cd project_name
make install
```

4. Write your models in resources/models.

5. Generate and setup your models:

```
make build
```

6. Run the server!

```
make serve
```

From here, you can work on the project, create a git repository and push your changes to GitHub. The project is set up to work with Heroku automatically, see [Heroku's guide on creating Django projects](https://devcenter.heroku.com/articles/getting-started-with-django) to get your started.

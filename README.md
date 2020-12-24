# Django-uWSGI-NGINX-MySQL(Docker-Compose)


## Dependence

* [Python](https://www.python.org/) 3.7
* [Django](https://www.djangoproject.com/) 2.2
* [MySQL](https://www.mysql.com/) 8

## Get Started

```
$ docker-compose up --build
```

### Front-End

- HTML 저장 위치
```
app/service_tastemeasure
├── templates
    └── service_tastemeasure
        └── <here.html>
```

- CSS/JS/IMG 저장 위치
```
app/staic
├── service_tastemeasure
    ├── css
    ├── img
    └── js
```

### Development

- Main site : http://localhost

- Admin page : http://localhost/admin

### Commands
create a django app
```
$ docker exec python ./manage.py startapp {app_label}
```

create models from existing database
```
$ docker exec python ./manage.py inspectdb > {path/to/models.py}
```

execute migration
```
$ docker exec python ./manage.py migrate
```

create a migration file
```
$ docker exec python ./manage.py makemigrations
```

create dump fixture files
```
$ docker exec python ./manage.py dumpdata {app_label.model} --indent 2 > {path/to/fuxture.json}
```

load data from fixture files
```
$ docker exec python ./manage.py loaddata --verbosity 2 > {path/to/fuxture.json}
```

create an admin account
```
$ docker exec -it python ./manage.py createsuperuser
```

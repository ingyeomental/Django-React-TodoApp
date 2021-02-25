# Simple TODO APP
> Django-uWSGI-NGINX-MySQL(Docker-Compose) 활용

## Directory Tree

```
.
├── app                         # Django App
│   ├── config
│   ├── service_tastemeasure
│   ├── static
│   └── todo                    # TODO API 개발
├── docker                      # Dockerfile 및 각 Config 파일
│   ├── mysql                   
│   ├── nginx
│   └── python
└── frontend                    # React TODO APP
    ├── node_modules
    ├── public
    └── src
```


## Dependence

* [Python](https://www.python.org/) 3.7
* [Django](https://www.djangoproject.com/) 2.2
* [MySQL](https://www.mysql.com/) 8


## Get Started

### Step 1. Create or Start Django + Web + MySQL Container 
```
$ docker-compose up --build
```

### Step 2. Start React App in Python Container
```
$ cd /var/www/frontend && npm start
```

### Step 3. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.


## Development

- Main site : http://localhost:3000
- Api page : http://localhost/api
    - Todo App api : http://localhost/api/todos


## Reference

- https://github.com/yoshitakameguro/docker-django-uwsgi-nginx-mysql
- https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react

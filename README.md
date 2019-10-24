## Django-vue-stories

Inspired from https://mxh-mini-apps.github.io/mxh-cp-stories/.

<!-- 攻め（せめ）seme 受け（うけ）uke -->

## Features

- Django restframwork

- taggit

- debug_toolbar

- Vue CLI3 & Vue.js integration

- axios, element-ui

- Heroku


## Setup

setup a `virtualenv` if needed

```
mkdir env
virtualenv dj
source dj/bin/activate
cd yourproject
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:

```
python manage.py createsuperuser
```

Run:

```
python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000/).

## Vue

```
npm install -g @vue/cli
```

```
cd vuefront
# install dependencies
npm install
```

Project setup
```
npm install
```

Compiles and hot-reloads for development
```
npm run serve
```

Compiles and minifies for production
```
npm run build
```
Run your tests
```
npm run test
```

Lints and fixes files
```
npm run lint
```

Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/)

License
----

MIT

## REFERENCES

- .browserslistrc ==> https://github.com/browserslist/browserslist#custom-usage-data

- https://cli.vuejs.org/config/#typescript

- Inspiration from: https://github.com/gtalarico/django-vue-template


## Django-vue-stories

Inspired from https://mxh-mini-apps.github.io/mxh-cp-stories/.

![github](media/user/2019/github.png): https://github.com/mxh-mini-apps/mxh-cp-stories / https://github.com/mxh-mini-apps/mxh-cp-stories/blob/master/src/assets/story.json

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

```sh
mkdir env
virtualenv dj
source dj/bin/activate
cd yourproject
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:

```sh
python manage.py createsuperuser
admin/adminlemon
```

Run:

```sh
python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000/).

## Vue

```sh
npm install -g @vue/cli
```

```sh
cd vuefront
```

Project setup
```sh
# install dependencies
npm install
```

Compiles and hot-reloads for development
```sh
npm run serve
```

Compiles and minifies for production
```sh
npm run build
```
Run your tests
```sh
npm run test
```

Lints and fixes files
```sh
npm run lint
```

Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/)

License
----

MIT
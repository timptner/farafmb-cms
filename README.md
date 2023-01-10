# FaRaFMB

This repository contains the source code for www.farafmb.de.

The website is build with [Django](https://www.djangoproject.com/) and [Wagtail](https://wagtail.org/).

For style this project includes a customized build of [Bulma](https://bulma.io/). 

## Installation

Create a python virtual environment.

```shell
python3 -m venv venv
```

Activate it.

```shell
source venv/bin/activate
```

Install all required dependencies.

```shell
pip install -r requirements.txt
```

## Development

To start a development webserver:

```shell
python manage.py runserver
```

If you make changes to the stylesheet you must re-generate the customized bulma build.
Therefor sass-cli needs to be available.

```shell
brew install sass/sass/sass
```

Ensure to have a current build of bulma under `farafmb/static/bulma/bulma.sass`.
Re-Generate a custom bulma build.

```shell
sass --no-source-map farafmb/static/sass/farafmb.scss:farafmb/static/css/farafmb.css
```

This will generate a fresh stylesheet under `farafmb/static/css/farafmb.css`.

## Author

Aiven Timptner

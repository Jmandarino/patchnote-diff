## Requirements
- Postgres (10.0 or higher)
- Python 3

## Installation
- Install python 3
- Install Postgres

### Create Postgres Database (windows)
- `psql -U postgres`
- `CREATE ROLE patchnotes WITH LOGIN PASSWORD 'secure_password';`
- `ALTER ROLE patchnotes CREATEDB;`
- `CREATE DATABASE patchnotes;`
- `GRANT ALL PRIVILEGES ON DATABASE patchnotes TO patchnotes;`


### Create Super User
- `./manage.py migrate`
- `./manage.py createsuperuser`

## Running the Server (and Migrations)
- `./manage.py migrate`
- `./manage.py runserver`

# Postgresql & PgAdmin powered by compose


## Requirements:
* docker >= 17.12.0+
* docker-compose

## Quick Start
* Clone or download this repository
* Go inside of directory,  `cd compose-postgres`
* Run this command `docker-compose up -d`


## Environments
This Compose file contains the following environment variables:

* `POSTGRES_USER` the default value is **admin**
* `POSTGRES_PASSWORD` the default value is **admin**
* `PGADMIN_PORT` the default value is **5050**
* `PGADMIN_DEFAULT_EMAIL` the default value is **admin**
* `PGADMIN_DEFAULT_PASSWORD` the default value is **admin**

## Access to postgres: 
* `localhost:5432`
* **Username:** admin (as a default)
* **Password:** admin (as a default)

## Access to PgAdmin: 
* **URL:** `http://localhost:5050`
* **Username:** admin@mail.jp (as a default)
* **Password:** admin (as a default)

## Add a new server in PgAdmin:
* **Host name/address** `postgres`
* **Port** `5432`
* **Username** as `POSTGRES_USER`, by default: `admin`
* **Password** as `POSTGRES_PASSWORD`, by default `admin`
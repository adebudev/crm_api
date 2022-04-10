# CRM Api Project

Manual Setup
============

To begin development, you will need:

* [Docker](https://docs.docker.com/install/#supported-platforms)
* [Docker Compose](https://docs.docker.com/compose/install/)

Starting the Application
========================

We'll use docker-compose to orchestrate the Docker containers that make up the application.  First, however, we need to build
the Docker image that will be our application server.

To do that, execute (in the main directory):

`docker build . -t crm_api`

Once that command has completed, we may start the application:

`docker-compose up`

Local Setup (Optional)
======================

To begin local development, you will need:

* [pyenv](https://realpython.com/intro-to-pyenv/)

**Steps for python installation**

1. `$ pyenv install 3.9.6`
2. `$ pyenv virtualenv 3.6.9 <environment_name>`
3. `$ pyenv activate <environment_name>`

To deactivate virtual env\
`$ pyenv deactivate`


Alembic
=======

To run migration in alembic take into account the followings commands

1. Enter the container:
    * `docker-compose exec api bash`
2. Create revision
    * `alembic revision -m "version ticket - this migrations add a new table to the md schema"`
2. Stamp revision
    * `alembic stamp <down-revision>`
3. Upgrade revision
    * `alembic upgrade +1`
4. If you desire to upgrade all revisions
    * `alembic upgrade head`

* Note: To downgrade revision, please stamp to the revision you want and check with:
    * `alembic downgrade -1`

If you want to check more about alembic please read the docs: [Alembic](https://alembic.sqlalchemy.org/en/latest/)

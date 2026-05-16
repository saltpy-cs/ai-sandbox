# Technology Architecture

## Decisions
- Python and FastAPI will be used for API services
- PostgreSQL and SQLAlchemy will be used for relational databases
- Typescript and React will be used for UI
- Docker will be used to run API services and relational databases
- Docker Compose will be used to run a development environment locally
- Nginx will be used as a webserver
- There will be an private network called 'prv' which all services communicate across
- There will be a public network called 'pub' which will only allow traffic to the webserver
- All secrets, for example the database password, should be stored in a .env file
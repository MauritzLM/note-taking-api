# Frontend Mentor - Note Taking App API

This is an API for my note taking app, using [fastapi](https://fastapi.tiangolo.com/).
Hosted on [railway](railway.app) with a postgresql db.

## Notes
- Initially I struggled to understand how to connect to the db using SQLModel I decided to use SQLAlchemy directly instead.
- First time using docker in a project, wanted to initially use secrets with docker compose but railway does note support docker compose so settled for env variables.
- Followed the fastapi docs to setup authentication.
- Had to learn about doing db migrations using alembic, I'm still unsure how to do migrations in production.
- Things to add: Password reset, google authentication.

## Helpful links
- [Youtube video](https://www.youtube.com/watch?v=398DuQbQJq0&list=LL&index=17). This video helped to setup my db connection and do some basic queries.




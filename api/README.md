This FastAPI app runs on Python 3.10.x

All services are currently running on a docker compose cluster which has some implications with the development experience on the api backend.

###  `poetry install --with handlers`

to create a poetry-managed virtualenv on your host machine. This is recommended so you don't have to `docker exec` a shell inside the fastapi container every time you want to issue, say, `alembic` commands.

### Install [direnv](https://direnv.net/docs/installation.html)

first to load the necessary environment variables prior to running the commands below. Don't forget to [hook](https://direnv.net/docs/hook.html) it to your shell.

#### `direnv allow`
inside the `api` directory aftewrwards to load the variables from `.envrc`

## Database migrations

Right now, the postgis database is being populated with a few datasets via alembic migration. We are planning to decouple this eventually as standalone scripts, but for now you will need the [Nigeria schools and population](https://github.com/avsolatorio/worldex/files/12481827/nigeria-schools-and-population-density.zip) and Critical Habitat (download link to follow or ask any of the repo maintainers) datasets.

You will need to download them into the `/tmp/datasets/` directory of your host machine. Additionally, you will have to unzip the Nigeria datasets. You can leave the Critical Habitat zipfile as is.

### `just migrate-db`
from `/api` to apply the database migrations. If you need to troubleshoot or would like a more fine-grained control, you can run

#### `docker compose exec -it api /bin/bash`
to run a shell instance on the api service. Afterwards, you can issue your commands such as

#### `alembic upgrade head`
which is exactly what `just migrate-db` does.

## Populating the database

You can populate the database with a few datasets stored in an aws bucket. From the `api` directory run

```
just run-script index_nigeria_pop_density
```

Or alternatively, run the actual command

```
poetry run python -m scripts.index_nigeria_pop_density
```

See the `api/scripts` directory for the rest you can run.

# API development

The api codebase currently hot reloads, so any changes you make should reflect immediately. However, the dependencies are baked in on the docker image. And so...

## Using poetry

You will still use the `poetry` command on your host machine to add/remove dependencies, but the docker image (and container) only interacts with the `poetry.lock` and `pyproject.toml`. Which means you'll have to rebuild the image when dependencies are added using

### `docker compose up api --build`

This is admittedly added toil when compared to ui where the `node_modules` can be bind-mounted and thus `yarn add` commands can be issued from the host.

Unfortunately, the same cannot be done for the poetry-managed `virtualenv`. You will encounter ownership/permission issues if you try to run `poetry` commands from the host for a bind-mounted virtualenv. So we're not doing it unless we find a workaround.


## Load DB dump

This is useful for loading an sql dump to a postgresql instance. The dump is located at `/opt/datasets.sql` and can be loaded with the following commands:

```bash
# Install postgis deps
sudo apt-get install postgis postgresql-15-postgis-3

# Create the database
createdb public.datasets -U postgres

# Install postgis extension
psql -d public.datasets -c "CREATE EXTENSION IF NOT EXISTS postgis;" -U postgres

# Load the dump
psql -d public.datasets -f /opt/datasets.sql -U postgres
```

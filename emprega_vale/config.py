import os
from importlib import import_module

from dynaconf import Dynaconf
from fastapi import FastAPI

BASE_PATH = os.path.dirname(__file__)

ABSOLUTE_PATH = os.path.abspath(os.path.join(BASE_PATH, '..'))

settings = Dynaconf(
    warn_dynaconf_global_settings=True,
    environments=True,
    lowercase_read=False,
    load_dotenv=True,
    default_settings_paths=[os.path.join(ABSOLUTE_PATH, 'settings.toml')],
)

SQLALCHEMY_DATABASE_URI = (
    f'postgresql+psycopg2://'
    f'{settings.DB_USER}:'
    f'{settings.DB_PASS}@'
    f'{settings.DB_HOST}:'
    f'{settings.DB_PORT}/'
    f'{settings.DB_NAME}'
)


def load_routes(app: FastAPI):
    for route in settings.ROUTES:
        module_name, factory = route.split(':')
        ext = import_module(module_name)
        getattr(ext, factory)(app)

import os

from dynaconf import Dynaconf

BASE_PATH = os.path.dirname(__file__)

ABSOLUTE_PATH = os.path.abspath(os.path.join(BASE_PATH, '..'))

settings = Dynaconf(warn_dynaconf_global_settings=True,
                    environments=True,
                    lowercase_read=False,
                    load_dotenv=True,
                    default_settings_paths=[os.path.join(ABSOLUTE_PATH, 'settings.toml')])

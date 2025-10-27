from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy import pool
from alembic import context
from os import path
from src.components.database_clients.models.database_models import *

BASE_DIR = path.abspath(path.join(path.dirname(path.abspath(__file__)), "../../../../storage/.databases"))
URL = f"sqlite:///{BASE_DIR}/production.db"
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = database.metadata

def run_migrations_offline() -> None:
    url = URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = create_engine(URL, poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

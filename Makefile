SHELL := /bin/bash
CURRENT_PATH := $(shell pwd)

.PHONY: all make_migration migrate

make_migration:
	PYTHONPATH=$(CURRENT_PATH) alembic revision --autogenerate

migrate:
	PYTHONPATH=$(CURRENT_PATH) alembic upgrade head
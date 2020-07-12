SHELL := /bin/bash
CURRENT_PATH := $(shell pwd)

.PHONY: all migration migrate

migration:
	PYTHONPATH=$(CURRENT_PATH) alembic revision --autogenerate

migrate:
	PYTHONPATH=$(CURRENT_PATH) alembic upgrade head
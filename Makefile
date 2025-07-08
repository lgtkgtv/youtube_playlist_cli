.PHONY: init sync run clean

ACCOUNT ?= your@email.com
SCRIPT = ./run.sh

init:
	uv init

sync:
	uv sync

run:
	uv run $(SCRIPT) --account=$(ACCOUNT)

download-all:
	uv run $(SCRIPT) --account=$(ACCOUNT) --download-all

list-users:
	uv run $(SCRIPT) --list-users

clean:
	rm -rf .venv tokens/ data/ uv.lock

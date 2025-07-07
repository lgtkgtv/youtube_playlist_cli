#!/bin/bash

# ------------------------------------------------------------------------------
# Entry point script for the ytcli tool.
#
# This script launches the main CLI logic via Python module mode.
# It assumes the virtual environment is already activated OR that it's used
# via `uv run ./run.sh` for dependency-managed execution.
#
# All CLI arguments passed to this script are forwarded to the Python CLI.
#
# Example Usage:
#
# export YTCLI_CLIENT_SECRET=secrets/client_secret.json
#
# uv run ./run.sh --email="you@gmail.com"
#
# With Markdown table and export
# uv run ./run.sh --email="you@gmail.com" --markdown --export-md=playlists.md
#
# Filtered and sorted
# uv run ./run.sh --email="you@gmail.com" --filter=music --sort-by-count
#
# ------------------------------------------------------------------------------

python3 -m ytcli.cli "$@"


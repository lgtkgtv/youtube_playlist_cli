import argparse
import yaml

def load_config():
    default_config_file = "config.yaml"

    parser = argparse.ArgumentParser(description="YouTube Playlist CLI")

    parser.add_argument("--extended", action="store_true")
    parser.add_argument("--markdown", action="store_true")
    parser.add_argument("--no-truncate", action="store_true")
    parser.add_argument("--group-by-privacy", action="store_true")
    parser.add_argument("--sort-by-count", action="store_true")
    parser.add_argument("--filter", type=str, default=None)
    parser.add_argument("--export-md", type=str, default=None)
    parser.add_argument("--export-json", type=str, default=None)
    parser.add_argument("--export-csv", type=str, default=None)
    parser.add_argument("--config", type=str, default=default_config_file)
    parser.add_argument("--email", type=str, required=False, default=None)

    # Milestone 2: Playlist clone support
    parser.add_argument("--clone-playlist", type=str, help="Playlist ID to clone", default=None)
    parser.add_argument("--new-title", type=str, help="Title of new cloned playlist", default=None)
    parser.add_argument("--remove-original", action="store_true", help="Delete the original playlist after cloning")

    # Parse initial CLI args to check if --config is specified
    args, remaining_argv = parser.parse_known_args()

    config = {}
    if args.config:
        with open(args.config, 'r') as f:
            config = yaml.safe_load(f) or {}

    # Merge config values into CLI args
    for key, value in config.items():
        if hasattr(args, key):
            setattr(args, key, value)

    # Final parse to apply merged args, allow CLI to override YAML
    parser.set_defaults(**vars(args))
    return parser.parse_args(remaining_argv)


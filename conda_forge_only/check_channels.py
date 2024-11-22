import sys
import yaml


def validate_channels(file_path):
    """Validates that the channels list in the given file only contains 'conda-forge'."""
    with open(file_path, 'r') as file:
        try:
            content = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"YAML parsing error in {file_path}: {exc}")
            return False

    if not isinstance(content, dict) or "channels" not in content:
        print(f"No 'channels' key found in {file_path}.")
        return False

    channels = content["channels"]
    if not isinstance(channels, list):
        print(f"'channels' in {file_path} is not a list.")
        return False

    invalid_channels = [channel for channel in channels if channel != "conda-forge"]
    if invalid_channels:
        print(
            f"Invalid channels found in {file_path}: {', '.join(invalid_channels)}. "
            f"Only 'conda-forge' is allowed."
        )
        return False

    return True


def main():
    """Entry point for the pre-commit hook."""
    files = sys.argv[1:]
    all_valid = True

    for file_path in files:
        if not validate_channels(file_path):
            all_valid = False

    sys.exit(0 if all_valid else 1)

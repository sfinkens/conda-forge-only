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

    # Check that the "channels" key exists and is a list
    is_conda_env = "name" in content and "dependencies" in content
    if is_conda_env:
        if "channels" not in content:
            print(f"No 'channels' key found in {file_path}.")
            return False

        channels = content["channels"]
        if not isinstance(channels, list):
            print(f"'channels' in {file_path} is not a list.")
            return False

        # Validate that only "conda-forge" is present
        if set(channels) != {"conda-forge"}:
            print(
                f"Invalid channels found in {file_path}: {', '.join(channels)}. "
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


if __name__ == "__main__":
    main()
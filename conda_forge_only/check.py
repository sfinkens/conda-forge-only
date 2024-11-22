import yaml


class ValidationError(Exception):
    def __init__(self, filename, error_message):
        self.filename = filename
        self.error_message = error_message

    def __str__(self):
        return f"{self.filename}: {self.error_message}"


def check_file(file_path):
    """Validates that the channels list in the given file only contains 'conda-forge'."""
    content = _read_yaml(file_path)
    is_conda_env = _is_conda_env(content)
    if is_conda_env:
        channels = _get_channels(file_path, content)
        _check_conda_forge_only(file_path, channels)


def _read_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            content = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            raise ValidationError(file_path, f"YAML parsing error: {exc}")
    return content


def _is_conda_env(content):
    return "name" in content and "dependencies" in content


def _get_channels(file_path, content):
    try:
        channels = content["channels"]
    except KeyError:
        raise ValidationError(file_path, "No 'channels' key")
    if not isinstance(channels, list):
        raise ValidationError(file_path, f"'channels' is not a list")
    return channels


def _check_conda_forge_only(file_path, channels):
    if set(channels) != {"conda-forge"}:
        raise ValidationError(
            file_path,
            f"Invalid channels found: {channels}. "
            f"Only 'conda-forge' is allowed."
        )


def check_files(files):
    checks_passed = []
    for file_path in files:
        try:
            check_file(file_path)
            checks_passed.append(True)
        except ValidationError as err:
            checks_passed.append(False)
            print(err)
        except Exception as err:
            print(f"{file_path}: Unexpected error: {err}")
            checks_passed.append(False)
    return checks_passed

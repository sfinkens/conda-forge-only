import pytest
from conda_forge_only.check_channels import validate_channels, ValidationError
from contextlib import nullcontext as does_not_raise


def create_yaml_file(tmp_path, content):
    """Helper function to create a temporary YAML file."""
    file_path = tmp_path / "test.yaml"
    file_path.write_text(content)
    return file_path


def test_not_a_conda_env(tmp_path):
    content = """
    foo: bar
    """
    file_path = create_yaml_file(tmp_path, content)
    with does_not_raise():
        validate_channels(file_path)


def test_valid_env(tmp_path):
    content = """
    name: myenv
    dependencies:
      - foo
    channels:
      - conda-forge
    """
    file_path = create_yaml_file(tmp_path, content)
    with does_not_raise():
        validate_channels(file_path)


def test_invalid_env_with_extra_channels(tmp_path):
    content = """
    name: myenv
    dependencies:
      - foo
    channels:
      - defaults
      - conda-forge
    """
    file_path = create_yaml_file(tmp_path, content)
    with pytest.raises(ValidationError):
        validate_channels(file_path)


def test_invalid_env_no_channels_key(tmp_path):
    content = """
    name: myenv
    dependencies:
      - foo
    """
    file_path = create_yaml_file(tmp_path, content)
    with pytest.raises(ValidationError):
        validate_channels(file_path)


def test_invalid_env_channels_not_a_list(tmp_path):
    content = """
    name: myenv
    dependencies:
      - foo
    channels: conda-forge
    """
    file_path = create_yaml_file(tmp_path, content)
    with pytest.raises(ValidationError):
        validate_channels(file_path)

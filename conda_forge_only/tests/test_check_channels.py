import pytest
from conda_forge_only.check_channels import validate_channels


def create_yaml_file(tmp_path, content):
    """Helper function to create a temporary YAML file."""
    file_path = tmp_path / "test.yaml"
    file_path.write_text(content)
    return file_path


def test_valid_yaml(tmp_path):
    content = """
    channels:
      - conda-forge
    """
    file_path = create_yaml_file(tmp_path, content)
    assert validate_channels(file_path) is True


def test_invalid_yaml_with_extra_channels(tmp_path):
    content = """
    channels:
      - defaults
      - conda-forge
    """
    file_path = create_yaml_file(tmp_path, content)
    assert validate_channels(file_path) is False


def test_invalid_yaml_no_channels_key(tmp_path):
    content = """
    dependencies:
      - numpy
    """
    file_path = create_yaml_file(tmp_path, content)
    assert validate_channels(file_path) is False


def test_invalid_yaml_channels_not_a_list(tmp_path):
    content = """
    channels: conda-forge
    """
    file_path = create_yaml_file(tmp_path, content)
    assert validate_channels(file_path) is False

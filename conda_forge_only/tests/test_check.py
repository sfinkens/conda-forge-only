import pytest
from conda_forge_only.check import check_file, check_files, ValidationError
from contextlib import nullcontext as does_not_raise
from click.testing import CliRunner
from conda_forge_only.cli import cli

def create_yaml_file(tmp_path, content, filename="test.yaml"):
    """Helper function to create a temporary YAML file."""
    file_path = tmp_path / filename
    file_path.write_text(content)
    return file_path


@pytest.fixture
def invalid_yaml(tmp_path):
    content = """
    |:
    """
    file_path = create_yaml_file(tmp_path, content, "invalid_yaml.yaml")
    return file_path


@pytest.fixture
def not_a_conda_env(tmp_path):
    content = """
    foo: bar
    """
    file_path = create_yaml_file(tmp_path, content, "not_a_conda_env.yaml")
    return file_path


@pytest.fixture
def valid_env(tmp_path):
    content = """
    name: myenv
    dependencies:
      - foo
    channels:
      - conda-forge
    """
    file_path = create_yaml_file(tmp_path, content, "valid_env.yaml")
    return file_path


@pytest.fixture
def invalid_env_with_extra_channels(tmp_path):
    content = """
    name: myenv
    dependencies:
      - foo
    channels:
      - defaults
      - conda-forge
    """
    file_path = create_yaml_file(tmp_path, content)
    return file_path


def test_not_a_conda_env(not_a_conda_env):
    with does_not_raise():
        check_file(not_a_conda_env)


def test_valid_env(valid_env):
    with does_not_raise():
        check_file(valid_env)


def test_invalid_env_with_extra_channels(invalid_env_with_extra_channels):
    with pytest.raises(ValidationError):
        check_file(invalid_env_with_extra_channels)


def test_invalid_env_no_channels_key(tmp_path):
    content = """
    name: myenv
    dependencies:
      - foo
    """
    file_path = create_yaml_file(tmp_path, content)
    with pytest.raises(ValidationError):
        check_file(file_path)


def test_invalid_env_channels_not_a_list(tmp_path):
    content = """
    name: myenv
    dependencies:
      - foo
    channels: conda-forge
    """
    file_path = create_yaml_file(tmp_path, content)
    with pytest.raises(ValidationError):
        check_file(file_path)


def test_multiple_files_pass(not_a_conda_env, valid_env):
    checks_passed = check_files([not_a_conda_env, valid_env])
    assert all(checks_passed)

def test_multiple_files_fail(valid_env, invalid_env_with_extra_channels, invalid_yaml):
    checks_passed = check_files([valid_env, invalid_env_with_extra_channels, invalid_yaml, "/foo.yaml"])
    assert not all(checks_passed)


def test_cli_pass(valid_env):
    args = [str(valid_env)]
    runner = CliRunner()
    res = runner.invoke(cli, args, catch_exceptions=False)
    assert res.exit_code == 0


def test_cli_fail(invalid_env_with_extra_channels):
    args = [str(invalid_env_with_extra_channels)]
    runner = CliRunner()
    res = runner.invoke(cli, args, catch_exceptions=False)
    assert res.exit_code == 1

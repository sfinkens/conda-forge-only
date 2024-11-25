# conda-forge-only

.. image:: https://github.com/sfinkens/conda-forge-only/workflows/CI/badge.svg?branch=main
    :target: https://github.com/sfinkens/conda-forge-only/actions?query=workflow%3A%22CI%22

.. image:: https://coveralls.io/repos/github/sfinkens/conda-forge-only/badge.svg?branch=main
    :target: https://coveralls.io/github/sfinkens/conda-forge-only?branch=main


A pre-commit hook to check that conda environment files use conda-forge only.

## Usage

Add the following lines to your project's `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/sfinkens/conda-forge-only
  rev: v0.1.0
  hooks:
    - id: conda-forge-only
```

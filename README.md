# conda-forge-only

[![CI](https://github.com/sfinkens/conda-forge-only/actions/workflows/ci.yaml/badge.svg)](https://github.com/sfinkens/conda-forge-only/actions?query=workflow%3A%22CI%22)
[![codecov](https://codecov.io/gh/sfinkens/conda-forge-only/graph/badge.svg?token=5MMOU081WQ)](https://codecov.io/gh/sfinkens/conda-forge-only)


A pre-commit hook to check that conda environment files use conda-forge only.

## Usage

Add the following lines to your project's `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/sfinkens/conda-forge-only
  rev: v0.1.0
  hooks:
    - id: conda-forge-only
```

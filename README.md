# conda-forge-only

[![CI](https://github.com/sfinkens/conda-forge-only/workflows/CI/badge.svg)](https://github.com/sfinkens/conda-forge-only/actions/workflows/ci.yml)
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

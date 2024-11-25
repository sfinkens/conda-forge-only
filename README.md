# conda-forge-only

A pre-commit hook to check that conda environment files use conda-forge only.

## Usage

Add the following lines to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/sfinkens/conda-forge-only
  rev: v0.1.0
  hooks:
    - id: conda-forge-only
```

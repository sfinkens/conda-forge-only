# conda-forge-only

A pre-commit hook to enforce that YAML channel lists contain only `conda-forge`.

## Usage

Add to your `.pre-commit-config.yaml`:

```yaml   
- repo: https://github.com/your-username/conda-forge-only
  rev: v0.1.0  # Use the latest version tag
  hooks:
    - id: conda-forge-only
```

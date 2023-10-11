# Default pre-commit config

In a repository that requires [pre-commit](https://pre-commit.com), simply add
a file called `.pre-commit-config.yaml` with the following code.

```yaml
repos:
  - repo: https://github.com/UCL-MIRSG/.github
    rev: ""
    hooks:
      - id: mirsg-hooks
```

Then run `pre-commit install; pre-commit autoupdate`.

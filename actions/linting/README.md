# linting

This action can be used in the following manner.

```yaml
jobs:
  linting:
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/linting@v0.1.0
        with:
          pre-commit-config: ./.pre-commit-config.yaml
```

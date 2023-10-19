# add-to-project

This action can be used in the following manner.

```yaml
jobs:
  add-issue-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/add-to-project@v0.1.0
        with:
          app-id: ${{ secrets.APP_ID }}
          app-pem: ${{ secrets.APP_PEM }}
```

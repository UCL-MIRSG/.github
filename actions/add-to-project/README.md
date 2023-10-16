# add-to-project

This action can be used in the following manner.

```yaml
jobs:
  add-issue-to-project:
    name: Add Issues to Board
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/add-to-project@v0.1.0
        with:
          app_id: ${{ secrets.APP_ID }}
          app_pem: ${{ secrets.APP_PEM }}
```

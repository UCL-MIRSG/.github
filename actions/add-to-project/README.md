# add-to-project

This action can be used in the following manner:

```yaml
jobs:
  add-issue-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/add-to-project@vx.y.z
        with:
          app-id: ${{ secrets.APP_ID }}
          app-pem: ${{ secrets.APP_PEM }}
```

where `x.y.z` is the `major.minor.patch` version of the action.

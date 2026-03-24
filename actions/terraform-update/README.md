# terraform-update

This action can be used in the following manner:

```yaml
jobs:
  terraform-update:
    runs-on: ubuntu-slim
    steps:
      - uses: UCL-MIRSG/.github/actions/terraform-update@vx
        with:
          app-id: ${{ vars.APP_ID }}
          app-pem: ${{ secrets.APP_PEM }}
```

where `x` is the `major` version of the action.

# terraform-lock-update

This action can be used in the following manner:

```yaml
jobs:
  terraform-lock-update:
    permissions:
      contents: write
    runs-on: ubuntu-slim
    steps:
      - uses: UCL-MIRSG/.github/actions/terraform-lock-update@vx
        env:
          APP_PEM: ${{ secrets.TERRAFORM_LOCK_UPDATE_APP_PRIVATE_KEY }}
        with:
          app-id: ${{ vars.TERRAFORM_LOCK_UPDATE_APP_ID }}
          app-pem: ${{ env.APP_PEM }}
```

where `x` is the `major` version of the action.

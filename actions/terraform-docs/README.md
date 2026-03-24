# terraform-docs

This action can be used in the following manner:

```yaml
jobs:
  terraform-docs:
    runs-on: ubuntu-slim
    steps:
      - uses: UCL-MIRSG/.github/actions/terraform-docs@vx
        with:
          app-id: ${{ vars.TERRAFORM_DOCS_APP_ID }}
          app-pem: ${{ secrets.TERRAFORM_DOCS_APP_PRIVATE_KEY }}
          working-dir: ./provision
```

where `x` is the `major` version of the action.

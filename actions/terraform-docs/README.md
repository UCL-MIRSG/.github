# terraform-docs

This action can be used in the following manner:

```yaml
jobs:
  terraform-docs:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/terraform-docs@vx
        env:
          APP_PEM:  ${{ secrets.TERRAFORM_DOCS_APP_PRIVATE_KEY }}
        with:
          app-id: ${{ vars.TERRAFORM_DOCS_APP_ID }}
          app-pem: ${{ env.APP_PEM }}
          working-dir: ./provision
```

where `x` is the `major` version of the action. Alternatively, the action can be
used as:

```yaml
jobs:
  terraform-docs:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/terraform-docs@vx
        env:
          APP_PEM:  ${{ secrets.TERRAFORM_DOCS_APP_PRIVATE_KEY }}
        with:
          app-id: ${{ vars.TERRAFORM_DOCS_APP_ID }}
          app-pem: ${{ env.APP_PEM }}
          find-dir: .
```

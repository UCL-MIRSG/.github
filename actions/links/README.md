# links

This action can be used in the following manner:

```yaml
jobs:
  links:
    permissions:
      contents: read
    runs-on: ubuntu-slim
    timeout-minutes: 2
    steps:
      - uses: UCL-MIRSG/.github/actions/links@vx
        env:
          APP_PEM: ${{ secrets.LINKS_PRIVATE_KEY }}
        with:
          app-id: ${{ vars.LINKS_APP_ID }}
          app-pem: ${{ env.APP_PEM }}
```

where `x` is the `major` version of the action. If custom link checking is
required, one can add custom inputs through `lychee-args`, i.e.:

```yaml
jobs:
  links:
    permissions:
      contents: read
    runs-on: ubuntu-slim
    steps:
      - uses: UCL-MIRSG/.github/actions/links@vx
        env:
          APP_PEM: ${{ secrets.LINKS_PRIVATE_KEY }}
        with:
          app-id: ${{ vars.LINKS_APP_ID }}
          app-pem: ${{ env.APP_PEM }}
          lychee-args: --no-progress --verbose .
```

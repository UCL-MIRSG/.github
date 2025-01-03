# links

This action can be used in the following manner:

```yaml
jobs:
  links:
    runs-on: ubuntu-latest
    timeout-minutes: 2
    steps:
      - uses: UCL-MIRSG/.github/actions/links@vx
        with:
          app-id: ${{ secrets.LINK_APP_ID }}
          app-pem: ${{ secrets.LINK_APP_PEM }}
```

where `x` is the `major` version of the action. If custom link checking is
required, one can add custom inputs through `lychee-args`, i.e.:

```yaml
jobs:
  linting:
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/linting@vx
        with:
          app-id: ${{ secrets.LINK_APP_ID }}
          app-pem: ${{ secrets.LINK_APP_PEM }}
          lychee-args: --debug --no-progress --verbose .
```

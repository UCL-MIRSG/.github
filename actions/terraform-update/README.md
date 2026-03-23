# Terraform Update

This action can be used in the following manner:

```yaml
jobs:
  linting:
    runs-on: ubuntu-slim
    steps:
      - uses: UCL-MIRSG/.github/actions/terraform-update@vx
```

where `x` is the `major` version of the action.

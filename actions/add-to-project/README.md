# add-to-project

This action can be used in the following manner to add issues to the
[default MIRSG project board](https://github.com/orgs/UCL-MIRSG/projects/3):

```yaml
jobs:
  add-issue-to-project:
    permissions: {}
    runs-on: ubuntu-slim
    steps:
      - uses: UCL-MIRSG/.github/actions/add-to-project@vx
        with:
          app-id: ${{ secrets.APP_ID }} # zizmor: ignore[secrets-outside-env]
          app-pem: ${{ secrets.APP_PEM }} # zizmor: ignore[secrets-outside-env]
```

where `x` is the `major` version of the action. If a different project board is
to be targeted, then the `project-url` input can be used and the above modified
to:

```yaml
jobs:
  add-issue-to-project:
    permissions: {}
    runs-on: ubuntu-slim
    steps:
      - uses: UCL-MIRSG/.github/actions/add-to-project@vx
        with:
          app-id: ${{ secrets.APP_ID }} # zizmor: ignore[secrets-outside-env]
          app-pem: ${{ secrets.APP_PEM }} # zizmor: ignore[secrets-outside-env]
          project-url: project_board_url
```

where `project_board_url` is the full URL of the project board to which the
repository's issues should be added.

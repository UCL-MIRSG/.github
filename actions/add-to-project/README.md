# add-to-project

This action can be used in the following manner to add issues to the [default
MIRSG project board](https://github.com/orgs/UCL-MIRSG/projects/3):

```yaml
jobs:
  add-issue-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/add-to-project@vx
        with:
          app-id: ${{ secrets.APP_ID }}
          app-pem: ${{ secrets.APP_PEM }}
```

where `x` is the `major` version of the action. If a different project board is
to be targeted, then the `project-url` input can be used and the above modified
to:

```yaml
jobs:
  add-issue-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/add-to-project@vx
        with:
          app-id: ${{ secrets.APP_ID }}
          app-pem: ${{ secrets.APP_PEM }}
          project-url: project_board_url
```

where `project_board_url` is the full URL of the project board to which the
repository's issues should be added.

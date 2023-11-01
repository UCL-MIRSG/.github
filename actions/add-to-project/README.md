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
          project-url: project_board_url # optional: defaults to https://github.com/orgs/UCL-MIRSG/projects/3
```

where `x.y.z` is the `major.minor.patch` version of the action.
where `project_board_url` is the url of the project board to add the issue to.

# Molecule Test

This action can be used in the following manner:

```yaml
jobs:
  molecule:
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/molecule-test@vx
```

where `x` is the `major` version of the action you would like to use.

The above workflow will run the `default` scenario for your role. If you would
like to specify a different scenario, you can do so with the `scenario` input:

```yaml
jobs:
  molecule:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: true
      matrix:
        molecule_scenario:
          - centos7
          - rocky8
    steps:
      - uses: UCL-MIRSG/.github/actions/molecule-test@vx
        with:
          scenario: ${{ matrix.molecule_scenario }}
```

If you are testing an Ansible Collection, Molecule requires your repository to
be in a specific path - `ansible_collections/<namespace>/<collection name>`.
Another requirement is that your Molecule configuration is not at the top-level
of the repository - you should put it in e.g. a `tests/` directory.

To use this action to test your Collection, you will need to specify a
`checkout_path` and `tests/path`:

```yaml
jobs:
  molecule:
    runs-on: ubuntu-latest
    steps:
      - uses: UCL-MIRSG/.github/actions/molecule-test@vx
        with:
          checkout_path: ansible_collections/my_namespace/my_collection
          tests_path: ansible_collections/my_namespace/my_collection/tests
```

Note, the `tests_path` is relative to the `$GITHUB_WORKSPACE` path, not to the
`checkout_path`.

If one requires a specific version of Ansible, then use the `ansible_version`
argument, i.e. `ansible_version: 10.0.0`.

By default, the action will default to `molecule test`, if running a specific
command is required, then use the `molecule_command` argument, i.e.
`molecule_command: converge`.

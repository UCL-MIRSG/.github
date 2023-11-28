# Molecule Test

This action can be used in the following manner:

```yaml
jobs:
  molecule:
    runs-on: ubuntu-latest
    steps:
      - name: Run `molecule test`
        uses: UCL-MIRSG/.github/actions/molecule-test@vx.y.z
```

where `x.y.z` is the `major.minor.patch` version of the action you would like to use.

The above workflow will run the `default` scenario for your role. If you would like to
specify a different scenario, you can do so with the `scenario` input:

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
      - name: Run `molecule test`
        uses: UCL-MIRSG/.github/actions/molecule-test@vx.y.z
        with:
          scenario: ${{ matrix.molecule_scenario }}
```

If you are testing an Ansible Collection, Molecule requires your repository to be in a specific
path - `ansible_collections/<namespace>/<collection name>`. You can set the checkout path
using the `checkout_path` input:

```yaml
jobs:
  molecule:
    runs-on: ubuntu-latest
    steps:
      - name: Run `molecule test`
        uses: UCL-MIRSG/.github/actions/molecule-test@vx.y.z
        with:
          checkout_path: ansible_collections/my_namespace/my_collection
```

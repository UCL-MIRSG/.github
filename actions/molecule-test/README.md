# Molecule Test

This action can be used in the following manner:

```yaml
jobs:
  molecule:
    runs-on: ubuntu-latest
    steps:
      - name: Run `molecule test`
        uses: UCL-MIRSG/.github/actions/molecule-test@v.0.1.0
```

This will run the `default` scenario for your role. If you would like to specify a different
scenario, you can specify this with the `scenario` input:

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
        uses: UCL-MIRSG/.github/actions/molecule-test@v0.21.0
        with:
          scenario: ${{ matrix.molecule_scenario }}
```

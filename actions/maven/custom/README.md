# Custom Maven Command

Generic Maven action, allowing one to simply run a Maven command. It will be
executed into a docker image, with Java 11 and Maven.

To build a Java app

```yaml
jobs:
  maven:
    permissions:
      contents: read
    runs-on: ubuntu-latest
    steps:
      - name: Build and Test
        uses: UCL-MIRSG/.github/actions/maven/custom@vx
        with:
          maven-args: clean install
```

where `x` is the `major` version of the action.

To set up a private Maven repository:

```yaml
jobs:
  maven:
    permissions:
      contents: read
    runs-on: ubuntu-latest
    steps:
      - name: Build and Test
        uses: UCL-MIRSG/.github/actions/maven/custom@vx
        with:
          maven-args: clean install
          maven-repo-server-id: YOUR_SERVER
          maven-repo-server-password: YOUR_BUILD_BOT_PASSWORD
          maven-repo-server-username: YOUR_BUILD_BOT_USER
```

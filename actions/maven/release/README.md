# Maven Release

Allows one to release a Java application by a bot. Very handy if one needs to
automate the release for each commit.

<!-- prettier-ignore -->
> [!NOTE]
> The release will allow one to set up a GPG key.

```yaml
jobs:
  release:
    permissions:
      contents: read
    runs-on: ubuntu-latest
    steps:
      - name: Release
        uses: UCL-MIRSG/.github/actions/maven/release@vx
        env:
          ACCESS_TOKEN: ${{ secrets.GITHUB_ACCESS_TOKEN }}
          GPG_KEY_ID: ${{ secrets.GITHUB_GPG_KEY_ID }}
          GPG_KEY: ${{ secrets.GITHUB_GPG_KEY }}
          MAVEN_REPO_SERVER_ID: ${{ secrets.MVN_REPO_PRIVATE_REPO_USER }}
          MAVEN_REPO_SERVER_PASSWORD: ${{ secrets.MVN_REPO_PRIVATE_REPO_PASSWORD }}
          MAVEN_REPO_SERVER_USERNAME: ${{ secrets.MVN_REPO_PRIVATE_REPO_USER }}
        with:
          access-token: ${{ env.ACCESS_TOKEN }}
          git-release-bot-email: release-bot@example.com
          git-release-bot-name: release-bot
          gpg-enabled: true
          gpg-key-id: ${{ env.GPG_KEY_ID }}
          gpg-key: ${{ env.GPG_KEY }}
          maven-args:
            -Dmaven.javadoc.skip=true -DskipTests -DskipITs -Ddockerfile.skip
            -DdockerCompose.skip
          maven-repo-server-id: ${{ env.MAVEN_REPO_SERVER_ID }}
          maven-repo-server-password: ${{ env.MAVEN_REPO_SERVER_PASSWORD }}
          maven-repo-server-username: ${{ env.MAVEN_REPO_SERVER_USERNAME }}
          release-branch-name: main
```

where `x` is the `major` version of the action.

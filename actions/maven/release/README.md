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
        with:
          access-token: ${{ secrets.GITHUB_ACCESS_TOKEN }} # zizmor: ignore[secrets-outside-env]
          git-release-bot-email: release-bot@example.com
          git-release-bot-name: release-bot
          gpg-enabled: true
          gpg-key-id: ${{ secrets.GITHUB_GPG_KEY_ID }} # zizmor: ignore[secrets-outside-env]
          gpg-key: ${{ secrets.GITHUB_GPG_KEY }} # zizmor: ignore[secrets-outside-env]
          maven-args:
            -Dmaven.javadoc.skip=true -DskipTests -DskipITs -Ddockerfile.skip
            -DdockerCompose.skip
          maven-repo-server-id: f${{ secrets.MVN_REPO_PRIVATE_REPO_USER }} # zizmor: ignore[secrets-outside-env]
          maven-repo-server-password:
            # prettier-ignore-start
            ${{ secrets.MVN_REPO_PRIVATE_REPO_PASSWORD }} # zizmor: ignore[secrets-outside-env]
            # prettier-ignore-end
          maven-repo-server-username: ${{ secrets.MVN_REPO_PRIVATE_REPO_USER }} # zizmor: ignore[secrets-outside-env]
          release-branch-name: main
```

where `x` is the `major` version of the action.

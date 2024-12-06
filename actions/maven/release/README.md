# Maven Release

Allows one to release a Java application by a bot. Very handy if one needs to
automate the release for each commit.

<!-- prettier-ignore -->
> [!NOTE]
> The release will allow one to set up a GPG key.

```yaml
- name: Release
  uses: UCL-MIRSG/.github/actions/maven/release@vx
  with:
    access-token: ${{ secrets.GITHUB_ACCESS_TOKEN }}
    git-release-bot-email: release-bot@example.com
    git-release-bot-name: release-bot
    gpg-enabled: true
    gpg-key-id: ${{ secrets.GITHUB_GPG_KEY_ID }}
    gpg-key: ${{ secrets.GITHUB_GPG_KEY }}
    maven-args:
      -Dmaven.javadoc.skip=true -DskipTests -DskipITs -Ddockerfile.skip
      -DdockerCompose.skip
    maven-repo-server-id: f${{ secrets.MVN_REPO_PRIVATE_REPO_USER }}
    maven-repo-server-password: ${{ secrets.MVN_REPO_PRIVATE_REPO_PASSWORD }}
    maven-repo-server-username: ${{ secrets.MVN_REPO_PRIVATE_REPO_USER }}
    release-branch-name: main
```

where `x` is the `major` version of the action.

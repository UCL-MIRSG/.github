# Maven release

```yaml
- name: Release
  uses: qcastel/github-actions-maven/actions/release@master
  with:
    release-branch-name: "master"
    gpg-enabled: "true"
    gpg-key-id: ${{ secrets.GITHUB_GPG_KEY_ID }}
    gpg-key: ${{ secrets.GITHUB_GPG_KEY }}
    maven-repo-server-id: f${{ secrets.MVN_REPO_PRIVATE_REPO_USER }}
    maven-repo-server-username: ${{ secrets.MVN_REPO_PRIVATE_REPO_USER }}
    maven-repo-server-password: ${{ secrets.MVN_REPO_PRIVATE_REPO_PASSWORD }}
    maven-args:
      "-Dmaven.javadoc.skip=true -DskipTests -DskipITs -Ddockerfile.skip
      -DdockerCompose.skip"
    git-release-bot-name: "release-bot"
    git-release-bot-email: "release-bot@example.com"
    access-token: ${{ secrets.GITHUB_ACCESS_TOKEN }}
```

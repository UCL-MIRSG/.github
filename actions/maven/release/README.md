# Maven release

```yaml
- name: Release
  uses: qcastel/github-actions-maven/actions/release@master
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
    release-branch-name: master
```

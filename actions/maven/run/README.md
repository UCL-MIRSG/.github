# Custom maven command

To build your java app

```yaml
- name: Build and Test
  uses: qcastel/github-actions-maven/actions/maven@master
  with:
    maven-args: clean install
```

If you need to setup a private maven repository:

```yaml
- name: Build and Test
  uses: qcastel/github-actions-maven/actions/maven@master
  with:
    maven-args: clean install
    maven-repo-server-id: YOUR_SERVER
    maven-repo-server-password: YOUR_BUILD_BOT_PASSWORD
    maven-repo-server-username: YOUR_BUILD_BOT_USER
```

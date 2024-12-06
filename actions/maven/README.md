# github-actions-maven

The GitHub Action for Maven wraps the Maven CLI to enable Maven commands to be
run. This can be used to run every Maven Command.

This repo contains two github actions around maven:

- maven-action: generic maven action, allowing you to simply run a maven
  command. It will be executed into a docker image, with Java 11 and maven.
- release: allowing you to release your java applications by a bot. Very handy
  if you want to automatise the release for each of your commits.

Note: The release will allow you to setup a GPG key.

## License

The Dockerfile and associated scripts and documentation in this project are
released under the MIT License.

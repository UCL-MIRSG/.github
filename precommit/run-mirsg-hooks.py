#!/usr/bin/env python
import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))


def main():
    cfg = os.path.join(HERE, "mirsg-hooks.yaml")
    cmd = ["pre-commit", "run", "--config", cfg, "--files"] + sys.argv[1:]
    os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    exit(main())

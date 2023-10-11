#!/usr/bin/env python
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve()


def main() -> None:
    cfg = HERE.parent / ".pre-commit-config.yaml"
    cmd = ["pre-commit", "run", "--config", f"{cfg}", "--files"] + sys.argv[1:]
    subprocess.run(cmd)


if __name__ == "__main__":
    main()

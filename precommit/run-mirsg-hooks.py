#!/usr/bin/env python
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve()


def main() -> int:
    cfg = HERE.parent / "mirsg-hooks.yaml"
    cmd = ["pre-commit", "run", "--config", f"{cfg}", "--files"] + sys.argv[1:]
    result = subprocess.run(cmd)
    return result.returncode


if __name__ == "__main__":
    exit(main())

#!/usr/bin/env python
import pathlib
import subprocess
import sys
import shlex

HERE = pathlib.Path(__file__).resolve()


def main() -> int:
    cfg = HERE.parent / "mirsg-hooks.yaml"
    result = subprocess.run(
        shlex.run(f"pre-commit run --config {cfg} --files {sys.argv[1:]}"),
        check=True,
    )
    return result.returncode


if __name__ == "__main__":
    exit(main())

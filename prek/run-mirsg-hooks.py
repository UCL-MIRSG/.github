#!/usr/bin/env python
import pathlib
import subprocess

HERE = pathlib.Path(__file__).resolve()


def main() -> int:
    cmd = [
        "prek",
        "run",
        "--config",
        str(HERE.parent / "mirsg-hooks.yaml"),
        "--all-files",
    ]
    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    exit(main())

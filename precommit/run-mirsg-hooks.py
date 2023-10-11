#!/usr/bin/env python
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve()


def main(run_once: int = 0) -> None:
    if not run_once:
        cfg = HERE.parent / ".pre-commit-config.yaml"
        cmd = ["pre-commit", "run", "--config", f"{cfg}", "--files"] + sys.argv[1:]
        subprocess.run(cmd)
        run_once += 1


if __name__ == "__main__":
    main()

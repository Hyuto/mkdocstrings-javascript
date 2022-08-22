import os
import contextlib
import shutil
import subprocess

from mkdocstrings.loggers import get_logger

main_dir = os.path.dirname(__file__)
logger = get_logger(__name__)


def _check_installed() -> bool:
    return os.path.exists(os.path.join(main_dir, "node_modules"))


def setup(pm: str) -> None:
    supported_pm = ["npm", "yarn"]
    assert pm in supported_pm, f"{pm} package manager is not supported. {supported_pm}"
    if _check_installed():
        print("Installed!")
        return
    logger.info(f"Installing javascript dependencies using {pm}")
    subprocess.run([pm, "install"], cwd=main_dir)


def clean() -> None:
    if not _check_installed():
        print("Not installed yet!")
        return
    logger.info(f"Uninstalling javascript dependencies and cleaning unused file.")
    shutil.rmtree(os.path.join(main_dir, "node_modules"))

    for lockfile in ["package-lock.json", "yarn.lock"]:
        with contextlib.suppress(FileNotFoundError):
            os.remove(os.path.join(main_dir, lockfile))

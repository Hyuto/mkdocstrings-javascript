import json
import os
import subprocess

main_dir = os.path.dirname(__file__)


def get_doclet():
    jsdoc_executable = os.path.join("node_modules", ".bin", "jsdoc")
    results = subprocess.run(
        [jsdoc_executable, "-X", os.path.join("..", "..", "tests", "lib")],
        cwd=main_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return json.loads(results.stdout)


class Parser:
    default_config = {}

    def __init__(self, **kwargs) -> None:
        self.default_config = {**self.default_config, **kwargs}

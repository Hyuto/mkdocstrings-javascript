import os
from typing import Any, Mapping, Optional, Sequence

from .handler import JSHandler

main_dir = os.path.dirname(__file__)
jsdoc_path = os.path.join(main_dir, "node_modules", ".bin", "jsdoc")
if not os.path.exists(jsdoc_path):
    raise ModuleNotFoundError(
        "jsdoc not found! Please run command "
        + "python -m mkdocstrings_handlers.javascript setup "
        + "to install javascript dependencies."
    )


def get_handler(
    theme: str,
    custom_templates: Optional[str] = None,
    crystal_docs_flags: Sequence[str] = (),
    source_locations: Mapping[str, str] = {},
    **config: Any
) -> JSHandler:

    return JSHandler()

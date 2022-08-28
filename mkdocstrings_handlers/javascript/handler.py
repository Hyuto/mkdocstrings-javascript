from typing import Any, Dict
from mkdocstrings.handlers.base import BaseHandler


class JSHandler(BaseHandler):
    domain: str = "js"
    fallback_theme = "material"

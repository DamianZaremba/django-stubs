# Stubs for django.template.loaders.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.template.base import Origin, Template
from django.template.engine import Engine
from typing import List, Optional
class Loader:
    engine: Any = ...
    def __init__(self, engine: Engine) -> None: ...
    def get_template(self, template_name: str, skip: Optional[List[Origin]] = ...) -> Template: ...
    def get_template_sources(self, template_name: Any) -> None: ...
    def reset(self) -> None: ...
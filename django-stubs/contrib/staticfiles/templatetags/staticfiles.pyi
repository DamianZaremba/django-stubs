# Stubs for django.contrib.staticfiles.templatetags.staticfiles (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from django.template.base import Parser, Token
from django.templatetags.static import StaticNode
register: Any

def static(path: Any): ...
def do_static(parser: Parser, token: Token) -> StaticNode: ...
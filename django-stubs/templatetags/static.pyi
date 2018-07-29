# Stubs for django.templatetags.static (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django import template
from typing import Any, Optional

from django.template.base import FilterExpression, Parser, Token
from django.template.context import Context
register: Any

class PrefixNode(template.Node):
    def __repr__(self): ...
    varname: Any = ...
    name: Any = ...
    def __init__(self, varname: None = ..., name: str = ...) -> None: ...
    @classmethod
    def handle_token(cls, parser: Parser, token: Token, name: str) -> PrefixNode: ...
    @classmethod
    def handle_simple(cls, name: str) -> str: ...
    def render(self, context: Context) -> str: ...

def get_static_prefix(parser: Parser, token: Token) -> PrefixNode: ...
def get_media_prefix(parser: Parser, token: Token) -> PrefixNode: ...

class StaticNode(template.Node):
    path: Any = ...
    varname: Any = ...
    def __init__(self, varname: Optional[str] = ..., path: FilterExpression = ...) -> None: ...
    def url(self, context: Context) -> str: ...
    def render(self, context: Context) -> str: ...
    @classmethod
    def handle_simple(cls, path: str) -> str: ...
    @classmethod
    def handle_token(cls, parser: Parser, token: Token) -> StaticNode: ...

def do_static(parser: Parser, token: Token) -> StaticNode: ...
def static(path: str) -> str: ...
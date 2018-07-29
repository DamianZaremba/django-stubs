# Stubs for django.templatetags.i18n (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.template import Node
from typing import Any, Optional

from django.template.base import FilterExpression, NodeList, Parser, Token
from django.template.context import Context, RequestContext
from django.utils.safestring import SafeText
from typing import Any, Dict, List, Optional, Tuple, Union
register: Any

class GetAvailableLanguagesNode(Node):
    variable: Any = ...
    def __init__(self, variable: str) -> None: ...
    def render(self, context: Context) -> str: ...

class GetLanguageInfoNode(Node):
    lang_code: Any = ...
    variable: Any = ...
    def __init__(self, lang_code: FilterExpression, variable: str) -> None: ...
    def render(self, context: Context) -> str: ...

class GetLanguageInfoListNode(Node):
    languages: Any = ...
    variable: Any = ...
    def __init__(self, languages: FilterExpression, variable: str) -> None: ...
    def get_language_info(self, language: Any): ...
    def render(self, context: Context) -> str: ...

class GetCurrentLanguageNode(Node):
    variable: Any = ...
    def __init__(self, variable: str) -> None: ...
    def render(self, context: RequestContext) -> str: ...

class GetCurrentLanguageBidiNode(Node):
    variable: Any = ...
    def __init__(self, variable: str) -> None: ...
    def render(self, context: RequestContext) -> str: ...

class TranslateNode(Node):
    noop: Any = ...
    asvar: Any = ...
    message_context: Any = ...
    filter_expression: Any = ...
    def __init__(self, filter_expression: FilterExpression, noop: bool, asvar: Optional[str] = ..., message_context: Optional[FilterExpression] = ...) -> None: ...
    def render(self, context: Context) -> str: ...

class BlockTranslateNode(Node):
    extra_context: Any = ...
    singular: Any = ...
    plural: Any = ...
    countervar: Any = ...
    counter: Any = ...
    message_context: Any = ...
    trimmed: Any = ...
    asvar: Any = ...
    def __init__(self, extra_context: Dict[str, FilterExpression], singular: List[Token], plural: List[Token] = ..., countervar: Optional[str] = ..., counter: Optional[FilterExpression] = ..., message_context: Optional[FilterExpression] = ..., trimmed: bool = ..., asvar: Optional[str] = ...) -> None: ...
    def render_token_list(self, tokens: List[Token]) -> Union[Tuple[str, List[str]], Tuple[str, List[Any]]]: ...
    def render(self, context: Context, nested: bool = ...) -> str: ...

class LanguageNode(Node):
    nodelist: Any = ...
    language: Any = ...
    def __init__(self, nodelist: NodeList, language: FilterExpression) -> None: ...
    def render(self, context: Context) -> SafeText: ...

def do_get_available_languages(parser: Parser, token: Token) -> GetAvailableLanguagesNode: ...
def do_get_language_info(parser: Parser, token: Token) -> GetLanguageInfoNode: ...
def do_get_language_info_list(parser: Parser, token: Token) -> GetLanguageInfoListNode: ...
def language_name(lang_code: str) -> str: ...
def language_name_translated(lang_code: str) -> str: ...
def language_name_local(lang_code: str) -> str: ...
def language_bidi(lang_code: str) -> bool: ...
def do_get_current_language(parser: Parser, token: Token) -> GetCurrentLanguageNode: ...
def do_get_current_language_bidi(parser: Parser, token: Token) -> GetCurrentLanguageBidiNode: ...
def do_translate(parser: Parser, token: Token) -> TranslateNode: ...
def do_block_translate(parser: Parser, token: Token) -> BlockTranslateNode: ...
def language(parser: Parser, token: Token) -> LanguageNode: ...
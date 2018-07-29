# Stubs for django.utils.encoding (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from datetime import date
from django.db.models.base import Model
from typing import Any, Optional, Union
class DjangoUnicodeDecodeError(UnicodeDecodeError):
    obj: Any = ...
    def __init__(self, obj: bytes, *args: Any) -> None: ...
    def __str__(self) -> str: ...

python_2_unicode_compatible: Any

def smart_text(s: Union[Model, int, str], encoding: str = ..., strings_only: bool = ..., errors: str = ...) -> str: ...

_PROTECTED_TYPES: Any

def is_protected_type(obj: Any) -> bool: ...
def force_text(s: Any, encoding: str = ..., strings_only: bool = ..., errors: str = ...) -> Optional[str]: ...
def smart_bytes(s: Any, encoding: str = ..., strings_only: bool = ..., errors: str = ...): ...
def force_bytes(s: Any, encoding: str = ..., strings_only: bool = ..., errors: str = ...) -> Union[date, bytes]: ...
smart_str = smart_text
force_str = force_text

def iri_to_uri(iri: Optional[str]) -> Optional[str]: ...

_ascii_ranges: Any
_hextobyte: Any
_hexdig: str

def uri_to_iri(uri: Optional[str]) -> Optional[str]: ...
def escape_uri_path(path: str) -> str: ...
def repercent_broken_unicode(path: bytes) -> bytes: ...
def filepath_to_uri(path: Optional[str]) -> Optional[str]: ...
def get_system_encoding() -> str: ...

DEFAULT_LOCALE_ENCODING: Any
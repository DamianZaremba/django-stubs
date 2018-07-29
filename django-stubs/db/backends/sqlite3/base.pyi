# Stubs for django.db.backends.sqlite3.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor
from django.db.backends.base.base import BaseDatabaseWrapper
from sqlite3 import dbapi2 as Database
from typing import Any, Optional

from datetime import datetime
from sqlite3 import Connection
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
def decoder(conv_func: Callable) -> Callable: ...

class DatabaseWrapper(BaseDatabaseWrapper):
    vendor: str = ...
    display_name: str = ...
    data_types: Any = ...
    data_types_suffix: Any = ...
    operators: Any = ...
    pattern_esc: str = ...
    pattern_ops: Any = ...
    Database: Any = ...
    SchemaEditorClass: Any = ...
    client_class: Any = ...
    creation_class: Any = ...
    features_class: Any = ...
    introspection_class: Any = ...
    ops_class: Any = ...
    def get_connection_params(self) -> Dict[str, Union[int, str]]: ...
    def get_new_connection(self, conn_params: Dict[str, Union[int, str]]) -> Connection: ...
    def init_connection_state(self) -> None: ...
    def create_cursor(self, name: None = ...) -> SQLiteCursorWrapper: ...
    def close(self) -> None: ...
    def _savepoint_allowed(self) -> bool: ...
    def _set_autocommit(self, autocommit: bool) -> None: ...
    def disable_constraint_checking(self) -> bool: ...
    def enable_constraint_checking(self) -> None: ...
    def check_constraints(self, table_names: List[str] = ...) -> None: ...
    def is_usable(self) -> bool: ...
    def _start_transaction_under_autocommit(self) -> None: ...
    def is_in_memory_db(self) -> bool: ...

FORMAT_QMARK_REGEX: Any

class SQLiteCursorWrapper(Database.Cursor):
    def execute(self, query: str, params: Any = ...) -> SQLiteCursorWrapper: ...
    def executemany(self, query: str, param_list: Union[List[Tuple[int, int]], List[Tuple[int]]]) -> SQLiteCursorWrapper: ...
    def convert_query(self, query: str) -> str: ...

def _sqlite_date_extract(lookup_type: str, dt: str) -> int: ...
def _sqlite_date_trunc(lookup_type: str, dt: str) -> str: ...
def _sqlite_time_trunc(lookup_type: str, dt: str) -> str: ...
def _sqlite_datetime_parse(dt: str, tzname: Optional[str]) -> datetime: ...
def _sqlite_datetime_cast_date(dt: str, tzname: Optional[str]) -> str: ...
def _sqlite_datetime_cast_time(dt: str, tzname: Optional[str]) -> str: ...
def _sqlite_datetime_extract(lookup_type: str, dt: str, tzname: Optional[str]) -> int: ...
def _sqlite_datetime_trunc(lookup_type: str, dt: str, tzname: Optional[str]) -> str: ...
def _sqlite_time_extract(lookup_type: str, dt: str) -> int: ...
def _sqlite_format_dtdelta(conn: str, lhs: Union[str, int], rhs: Union[str, int]) -> str: ...
def _sqlite_time_diff(lhs: Any, rhs: Any): ...
def _sqlite_timestamp_diff(lhs: str, rhs: str) -> int: ...
def _sqlite_regexp(re_pattern: str, re_string: Optional[str]) -> bool: ...
def _sqlite_lpad(text: str, length: int, fill_text: str) -> str: ...
def _sqlite_rpad(text: str, length: int, fill_text: str) -> str: ...
def _sqlite_power(x: Any, y: Any): ...
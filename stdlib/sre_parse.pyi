import sys
from sre_constants import *
from sre_constants import _NamedIntConstant as _NIC, error as _Error
from typing import Any, Iterable, Match, Optional, Pattern as _Pattern, overload

SPECIAL_CHARS: str
REPEAT_CHARS: str
DIGITS: frozenset[str]
OCTDIGITS: frozenset[str]
HEXDIGITS: frozenset[str]
ASCIILETTERS: frozenset[str]
WHITESPACE: frozenset[str]
ESCAPES: dict[str, tuple[_NIC, int]]
CATEGORIES: dict[str, tuple[_NIC, _NIC] | tuple[_NIC, list[tuple[_NIC, _NIC]]]]
FLAGS: dict[str, int]
if sys.version_info >= (3, 7):
    TYPE_FLAGS: int
GLOBAL_FLAGS: int

class Verbose(Exception): ...

class _State:
    flags: int
    groupdict: dict[str, int]
    groupwidths: list[int | None]
    lookbehindgroups: int | None
    def __init__(self) -> None: ...
    @property
    def groups(self) -> int: ...
    def opengroup(self, name: str | None = ...) -> int: ...
    def closegroup(self, gid: int, p: SubPattern) -> None: ...
    def checkgroup(self, gid: int) -> bool: ...
    def checklookbehindgroup(self, gid: int, source: Tokenizer) -> None: ...

if sys.version_info >= (3, 8):
    State = _State
else:
    Pattern = _State

_OpSubpatternType = tuple[Optional[int], int, int, SubPattern]
_OpGroupRefExistsType = tuple[int, SubPattern, SubPattern]
_OpInType = list[tuple[_NIC, int]]
_OpBranchType = tuple[None, list[SubPattern]]
_AvType = _OpInType | _OpBranchType | Iterable[SubPattern] | _OpGroupRefExistsType | _OpSubpatternType
_CodeType = tuple[_NIC, _AvType]

class SubPattern:
    data: list[_CodeType]
    width: int | None

    if sys.version_info >= (3, 8):
        state: State
        def __init__(self, state: State, data: list[_CodeType] | None = ...) -> None: ...
    else:
        pattern: Pattern
        def __init__(self, pattern: Pattern, data: list[_CodeType] | None = ...) -> None: ...

    def dump(self, level: int = ...) -> None: ...
    def __len__(self) -> int: ...
    def __delitem__(self, index: int | slice) -> None: ...
    def __getitem__(self, index: int | slice) -> SubPattern | _CodeType: ...
    def __setitem__(self, index: int | slice, code: _CodeType) -> None: ...
    def insert(self, index: int, code: _CodeType) -> None: ...
    def append(self, code: _CodeType) -> None: ...
    def getwidth(self) -> int: ...

class Tokenizer:
    istext: bool
    string: Any
    decoded_string: str
    index: int
    next: str | None
    def __init__(self, string: Any) -> None: ...
    def match(self, char: str) -> bool: ...
    def get(self) -> str | None: ...
    def getwhile(self, n: int, charset: Iterable[str]) -> str: ...
    if sys.version_info >= (3, 8):
        def getuntil(self, terminator: str, name: str) -> str: ...
    else:
        def getuntil(self, terminator: str) -> str: ...

    @property
    def pos(self) -> int: ...
    def tell(self) -> int: ...
    def seek(self, index: int) -> None: ...
    def error(self, msg: str, offset: int = ...) -> _Error: ...

def fix_flags(src: str | bytes, flags: int) -> int: ...

_TemplateType = tuple[list[tuple[int, int]], list[Optional[str]]]
_TemplateByteType = tuple[list[tuple[int, int]], list[Optional[bytes]]]
if sys.version_info >= (3, 8):
    def parse(str: str, flags: int = ..., state: State | None = ...) -> SubPattern: ...
    @overload
    def parse_template(source: str, state: _Pattern[Any]) -> _TemplateType: ...
    @overload
    def parse_template(source: bytes, state: _Pattern[Any]) -> _TemplateByteType: ...

else:
    def parse(str: str, flags: int = ..., pattern: Pattern | None = ...) -> SubPattern: ...
    @overload
    def parse_template(source: str, pattern: _Pattern[Any]) -> _TemplateType: ...
    @overload
    def parse_template(source: bytes, pattern: _Pattern[Any]) -> _TemplateByteType: ...

def expand_template(template: _TemplateType, match: Match[Any]) -> str: ...

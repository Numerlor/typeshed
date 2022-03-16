from _typeshed import SupportsLessThanT
from typing import Sequence, Text, overload
from typing_extensions import Literal

# All overloads can return empty string. Ideally, Literal[""] would be a valid
# Iterable[T], so that Union[List[T], Literal[""]] could be used as a return
# type. But because this only works when T is str, we need Sequence[T] instead.
@overload
def commonprefix(m: Sequence[str]) -> str | Literal[""]: ...  # type: ignore
@overload
def commonprefix(m: Sequence[Text]) -> Text: ...  # type: ignore
@overload
def commonprefix(m: Sequence[list[SupportsLessThanT]]) -> Sequence[SupportsLessThanT]: ...
@overload
def commonprefix(m: Sequence[tuple[SupportsLessThanT, ...]]) -> Sequence[SupportsLessThanT]: ...
def exists(path: Text) -> bool: ...
def getsize(filename: Text) -> int: ...
def isfile(path: Text) -> bool: ...
def isdir(s: Text) -> bool: ...

# These return float if os.stat_float_times() == True,
# but int is a subclass of float.
def getatime(filename: Text) -> float: ...
def getmtime(filename: Text) -> float: ...
def getctime(filename: Text) -> float: ...

# COMPLETE

from os import PathLike
from typing import (IO, Any, Callable, ContextManager, Dict, Generator,
                    Generic, ItemsView, Iterable, Iterator, KeysView, List,
                    Literal, Mapping, Optional, Sequence, Tuple, Type, TypeVar,
                    Union, ValuesView, overload)

from _typeshed import AnyPath, SupportsWrite
from matplotlib._typing import ArrayLike, ndarray
from matplotlib.artist import Artist

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_KT_co = TypeVar("_KT_co", covariant=True)  # Key type covariant containers.
_VT_co = TypeVar("_VT_co", covariant=True)  # Value type covariant containers.

class CallbackRegistry:
    def __init__(self, exception_handler: Optional[Callable[[Exception], Any]] = ...) -> None: ...

    def connect(self, signal: Any, func: Callable[..., Any]) -> int: ...
    def disconnect(self, cid: int) -> None: ...
    def process(self, s: Any, *args: Any, **kwargs: Any) -> None: ...


class Grouper:
    def __init__(self, init: Iterable[Any] = ...) -> None: ...
    
    def clean(self) -> None: ...
    def get_siblings(self, a: Any) -> List[Any]: ...
    def join(self, a: Any, *args: Any) -> None: ...
    def joined(self, a: Any, b: Any) -> bool: ...
    def remove(self, a: Any) -> None: ...

    def __contains__(self, item: Any) -> bool: ...
    def __iter__(self) -> Iterator[Any]: ...

class IgnoredKeyboardWarning(UserWarning): ...

class Stack:
    def __init__(self, default: Optional[Any] = ...) -> None: ...

    def back(self) -> Stack: ...
    def bubble(self, o: Any) -> Any: ...
    def clear(self) -> None: ...
    def empty(self) -> bool: ...
    def forward(self) -> Any: ...
    def home(self) -> Any: ...
    def push(self, o: Any) -> Any: ...
    def remove(self, o: Any) -> None: ...  

def boxplot_stats(
    x: ArrayLike,
    whis: Union[float, Tuple[float, float]] = ...,
    bootstrap: Optional[int] = ...,
    labels: Optional[ArrayLike] = ...,
    autorange: bool = ...
) -> List[Dict[str, Any]]: ...

def contiguous_regions(mask: ArrayLike) -> List[Tuple[int, int]]: ...

def delete_masked_points(*args: Any) -> Sequence[Any]: ...

def file_requires_unicode(x: SupportsWrite[Any]) -> bool: ...

def flatten(seq: Iterable[Any], scalarp: Callable[[Any], Any] = ...) -> Generator[Any, Any, Any]: ...

def get_sample_data(fname: AnyPath, asfileobj: bool = ..., *, np_load: bool = ...) -> Any: ... # TODO: split into overloads

def index_of(y: Union[float, ArrayLike]) -> Tuple[ndarray, ndarray]: ...

def is_math_text(s: object) -> bool: ...

def is_scalar_or_string(val: object) -> bool: ...

def is_writable_file_like(val: object) -> bool: ...

ls_mapper: Dict[str, str]
ls_mapper_r: Dict[str, str]

class maxdict(Dict[_KT, _VT]):
    def __init__(self, maxsize: int) -> None: ...

def normalize_kwargs(
    kw: Optional[Mapping[str, Any]],
    alias_mapping: Optional[Union[Mapping[str, Iterable[Any]], Type[Artist]]] = ...,
    require: Sequence[str] = ...,
    forbidden: Sequence[str] = ...,
    allowed: Optional[ Sequence[str]] = ...
) -> Dict[str, Any]: ...  # TODO: mappings between what and what?

def open_file_cm(path_or_file: Union[str, PathLike[Any], IO[Any]], mode: str = ..., encoding: Optional[str] = ...) -> ContextManager[IO[Any]]: ...

def print_cycles(objects: Iterable[Any], outstream: SupportsWrite[str] = ..., show_progress: bool = ...) -> None: ...

def pts_to_midstep(x: ArrayLike, *args: ArrayLike) -> ndarray: ...

def pts_to_poststep(x: ArrayLike, *args: ArrayLike) -> ndarray: ...

def pts_to_prestep(x: ArrayLike, *args: ArrayLike) -> ndarray: ...

def report_memory(i: int = ...) -> int: ...

def safe_first_element(obj: Union[Iterable[_T], Iterator[_T]]) -> _T: ...

def safe_masked_invalid(x: ArrayLike, copy: bool = ...) -> ndarray: ...

@overload
def sanitize_sequence(data: ItemsView[_KT_co, _VT_co]) -> List[Tuple[_KT_co, _VT_co]]: ...
@overload
def sanitize_sequence(data: KeysView[_KT_co]) -> List[_KT_co]: ...
@overload
def sanitize_sequence(data: ValuesView[_VT_co]) -> List[_VT_co]: ...
@overload
def sanitize_sequence(data: _T) -> _T: ...

_type = type
class silent_list(list[_T], Generic[_T]):
    type: _type
    def __init__(self, type: _type, seq: Optional[Iterable[_T]] = ...) -> None: ...

def simple_linear_interpolation(a: ndarray, steps: int) -> ndarray: ...

def strip_math(s: str) -> str: ...

@overload
def to_filehandle(fname: Union[str, PathLike[Any], IO[Any]], flag: str = ..., return_opened: Literal[False] = ..., encoding: Optional[str] = ...) -> IO[Any]: ...
@overload
def to_filehandle(fname: Union[str, PathLike[Any], IO[Any]], flag: str = ..., return_opened: Literal[True] = ..., encoding: Optional[str] = ...) -> Tuple[IO[Any], bool]: ...

def violin_stats(X: ArrayLike, method: Callable[[Any, ndarray], Any], points: int = ..., quantiles: Optional[ArrayLike] = ...) -> List[Dict[str, Any]]: ...

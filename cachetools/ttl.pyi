from typing import Callable, Iterator, Optional, TypeVar

from .cache import Cache

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class TTLCache(Cache[_KT, _VT]):
    """LRU Cache implementation with per-item time-to-live (TTL) value."""

    def __init__(
        self, maxsize: int, ttl: int, timer: Callable[[], float] = ..., getsizeof: Optional[Callable[[_VT], int]] = ...
    ) -> None:
        ...

    def __getitem__(self, key: _KT, cache_getitem: Callable[[_KT], _VT] = ...) -> _VT:
        ...

    def __setitem__(self, key: _KT, value: _VT, cache_setitem: Callable[[_KT, _VT], None] = ...) -> None:
        ...

    def __delitem__(self, key: _KT, cache_delitem: Callable[[_KT], None] = ...) -> None:
        ...

    def __iter__(self) -> Iterator[_KT]:
        ...

    def __len__(self) -> int:
        ...

    @property
    def currsize(self) -> int:
        """The current size of the cache."""
        ...

    @property
    def timer(self) -> Callable[[], float]:
        """ The timer function used by the cache. """
        ...

    @property
    def ttl(self) -> int:
        """ The time-to-live value of the cache's items. """
        ...

    def expire(self, time: Callable[[], float] = ...) -> None:
        """ Remove expired items from the cache. """
        ...


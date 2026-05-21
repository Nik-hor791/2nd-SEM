from typing import TypeVar, Generic, List, Callable, Any, Optional

# Определяем тип-параметр T
T = TypeVar('T')


class TypedCollection(Generic[T]):

    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError(f"Item {item} not found in collection")

    def get_all(self) -> List[T]:
        return self._items.copy()

    def sort_by(self, key_func: Callable[[T], Any]) -> 'TypedCollection[T]':
        self._items.sort(key=key_func)
        return self

    def filter_by(self, predicate: Callable[[T], bool]) -> 'TypedCollection[T]':
        self._items = [item for item in self._items if predicate(item)]
        return self

    def apply(self, func: Callable[[T], Any]) -> 'TypedCollection[T]':
        for item in self._items:
            func(item)
        return self

    def map(self, transform: Callable[[T], Any]) -> List[Any]:
        return list(map(transform, self._items))

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __contains__(self, item: T) -> bool:
        return item in self._items

    def __str__(self) -> str:
        if not self._items:
            return "TypedCollection (empty)"

        result = f"TypedCollection<{type(self._items[0]).__name__}> ({len(self._items)} items):\n"
        for i, item in enumerate(self._items, 1):
            result += f"  {i}. {item}\n"
        return result

    def find_first(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def find_all(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

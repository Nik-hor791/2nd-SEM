# Лабораторная работа №6 - Generics и typing

## Цель работы
- Освоить систему аннотаций типов в Python (typing)
- Научиться создавать обобщённые (generic) классы с помощью TypeVar и Generic
- Понять концепцию структурной типизации через typing.Protocol

## Иерархия классов
    Bus (базовый класс с аннотациями)
    ├── ElectricBus (с аннотациями)
    └── DieselBus (с аннотациями)


## Аннотации типов в классах

### Базовый класс Bus

```python
class Bus:
    def __init__(self, number: str, capacity: int, route: str, year: int) -> None:
        self._number: str = number
        self._capacity: int = capacity
        self._route: str = route
        self._year: int = year
    
    @property
    def number(self) -> str:
        return self._number
    
    def can_take_passengers(self, passengers: int) -> bool:
        return passengers <= self._capacity

```

### Generic-коллекция (container.py)

```python

from typing import TypeVar, Generic, List, Callable

T = TypeVar('T')

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get_all(self) -> list[T]:
        return self._items.copy()
    
    def sort_by(self, key_func: Callable[[T], any]) -> 'TypedCollection[T]':
        self._items.sort(key=key_func)
        return self
    
    def filter_by(self, predicate: Callable[[T], bool]) -> 'TypedCollection[T]':
        self._items = [item for item in self._items if predicate(item)]
        return self
    
    def __len__(self) -> int:
        return len(self._items)

```

### Demo.py
![alt text](<../../images/lab06/Снимок экрана (49).png>)
![alt text](<../../images/lab06/Снимок экрана (50).png>)
![alt text](<../../images/lab06/Снимок экрана (51).png>)
![alt text](<../../images/lab06/Снимок экрана (52).png>)
![alt text](<../../images/lab06/Снимок экрана (53).png>)
![alt text](<../../images/lab06/Снимок экрана (54).png>)
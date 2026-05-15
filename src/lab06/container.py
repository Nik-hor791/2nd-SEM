from typing import TypeVar, Generic, List, Callable, Any, Optional

# Определяем тип-параметр T
T = TypeVar('T')


class TypedCollection(Generic[T]):
    """
    Типизированная коллекция объектов с поддержкой функций высшего порядка

    Generic-класс, который может хранить элементы только одного типа T.
    Повторяет интерфейс коллекции из ЛР-2, но с аннотациями типов.
    """

    def __init__(self) -> None:
        """Создает пустую коллекцию"""
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """
        Добавляет элемент в коллекцию

        Args:
            item: Элемент типа T
        """
        self._items.append(item)

    def remove(self, item: T) -> None:
        """
        Удаляет элемент из коллекции

        Args:
            item: Элемент типа T для удаления

        Raises:
            ValueError: Если элемент не найден
        """
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError(f"Item {item} not found in collection")

    def get_all(self) -> List[T]:
        """
        Возвращает копию списка элементов

        Returns:
            Список всех элементов типа T
        """
        return self._items.copy()

    def sort_by(self, key_func: Callable[[T], Any]) -> 'TypedCollection[T]':
        """
        Сортирует коллекцию по заданной функции-ключу

        Args:
            key_func: Функция, извлекающая значение для сравнения

        Returns:
            Self для цепочек вызовов
        """
        self._items.sort(key=key_func)
        return self

    def filter_by(self, predicate: Callable[[T], bool]) -> 'TypedCollection[T]':
        """
        Фильтрует коллекцию по заданному предикату

        Args:
            predicate: Функция, возвращающая True для элементов, которые нужно оставить

        Returns:
            Self для цепочек вызовов
        """
        self._items = [item for item in self._items if predicate(item)]
        return self

    def apply(self, func: Callable[[T], Any]) -> 'TypedCollection[T]':
        """
        Применяет функцию к каждому элементу коллекции

        Args:
            func: Функция для применения к каждому элементу

        Returns:
            Self для цепочек вызовов
        """
        for item in self._items:
            func(item)
        return self

    def map(self, transform: Callable[[T], Any]) -> List[Any]:
        """
        Преобразует коллекцию в список результатов применения функции

        Args:
            transform: Функция преобразования

        Returns:
            Список результатов преобразования
        """
        return list(map(transform, self._items))

    def __len__(self) -> int:
        """Возвращает количество элементов в коллекции"""
        return len(self._items)

    def __getitem__(self, index: int) -> T:
        """
        Доступ к элементу по индексу

        Args:
            index: Индекс элемента

        Returns:
            Элемент по индексу
        """
        return self._items[index]

    def __contains__(self, item: T) -> bool:
        """
        Проверяет, содержится ли элемент в коллекции

        Args:
            item: Элемент для проверки

        Returns:
            True если элемент есть в коллекции
        """
        return item in self._items

    def __str__(self) -> str:
        """Строковое представление коллекции"""
        if not self._items:
            return "TypedCollection (empty)"

        result = f"TypedCollection<{type(self._items[0]).__name__}> ({len(self._items)} items):\n"
        for i, item in enumerate(self._items, 1):
            result += f"  {i}. {item}\n"
        return result

    def find_first(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """
        Находит первый элемент, удовлетворяющий предикату

        Args:
            predicate: Функция проверки условия

        Returns:
            Первый подходящий элемент или None
        """
        for item in self._items:
            if predicate(item):
                return item
        return None

    def find_all(self, predicate: Callable[[T], bool]) -> List[T]:
        """
        Находит все элементы, удовлетворяющие предикату

        Args:
            predicate: Функция проверки условия

        Returns:
            Список подходящих элементов
        """
        return [item for item in self._items if predicate(item)]

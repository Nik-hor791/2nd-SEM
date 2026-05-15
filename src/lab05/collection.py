from typing import List, Callable, Any
from base import Bus

class BusFleet:
    """Коллекция автобусов с поддержкой функций высшего порядка"""

    def __init__(self):
        self._buses: List[Bus] = []

    def add(self, bus: Bus) -> None:
        """Добавляет автобус в коллекцию"""
        self._buses.append(bus)

    def remove(self, bus: Bus) -> None:
        """Удаляет автобус из коллекции"""
        if bus in self._buses:
            self._buses.remove(bus)

    def get_all(self) -> List[Bus]:
        """Возвращает копию списка автобусов"""
        return self._buses.copy()

    def sort_by(self, key_func: Callable[[Bus], Any]) -> 'BusFleet':
        """
        Сортирует коллекцию по заданной функции-ключу
        key_func: функция, извлекающая значение для сравнения
        """
        self._buses.sort(key=key_func)
        return self  # возвращаем self для цепочек

    def filter_by(self, predicate: Callable[[Bus], bool]) -> 'BusFleet':
        """
        Фильтрует коллекцию по заданному предикату
        predicate: функция, возвращающая True для элементов, которые нужно оставить
        """
        self._buses = [bus for bus in self._buses if predicate(bus)]
        return self

    def apply(self, func: Callable[[Bus], Any]) -> 'BusFleet':
        """
        Применяет функцию к каждому элементу коллекции
        func: функция для применения к каждому автобусу
        """
        for bus in self._buses:
            func(bus)
        return self

    def map(self, transform: Callable[[Bus], Any]) -> List[Any]:
        """
        Преобразует коллекцию в список результатов применения функции
        transform: функция преобразования
        """
        return list(map(transform, self._buses))

    def __len__(self) -> int:
        return len(self._buses)

    def __getitem__(self, index: int) -> Bus:
        return self._buses[index]

    def __str__(self) -> str:
        if not self._buses:
            return "Empty fleet"
        result = f"BusFleet ({len(self._buses)} buses):\n"
        for i, bus in enumerate(self._buses, 1):
            result += f"  {i}. {bus}\n"
        return result
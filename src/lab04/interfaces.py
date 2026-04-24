from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс для объектов, которые можно вывести на печать"""

    @abstractmethod
    def to_string(self) -> str:
        """Возвращает строковое представление объекта"""
        pass

    @abstractmethod
    def get_short_info(self) -> str:
        """Возвращает краткую информацию об объекте"""
        pass


class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать"""

    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнивает текущий объект с другим
        Возвращает:
        - отрицательное число, если self < other
        - 0, если self == other
        - положительное число, если self > other
        """
        pass


class Chargeable(ABC):
    """Интерфейс для объектов, которые можно заряжать"""

    @abstractmethod
    def charge(self, hours: float) -> str:
        """Заряжает устройство в течение указанного количества часов"""
        pass

    @abstractmethod
    def get_battery_percentage(self) -> int:
        """Возвращает текущий уровень заряда батареи (0-100)"""
        pass


class Refuelable(ABC):
    """Интерфейс для объектов, которые можно заправлять"""

    @abstractmethod
    def refuel(self, liters: float) -> str:
        """Заправляет топливом в указанном количестве литров"""
        pass

    @abstractmethod
    def get_fuel_level(self) -> int:
        """Возвращает текущий уровень топлива (0-100)"""
        pass
"""
Стратегии сортировки, фильтрации и преобразования для BusFleet
"""

from typing import Callable
from base import Bus
from models import ElectricBus, DieselBus


# ==================== СТРАТЕГИИ СОРТИРОВКИ ====================

def by_number(bus: Bus) -> str:
    """Стратегия сортировки по номеру автобуса"""
    return bus.number


def by_capacity(bus: Bus) -> int:
    """Стратегия сортировки по вместимости"""
    return bus.capacity


def by_year(bus: Bus) -> int:
    """Стратегия сортировки по году выпуска"""
    return bus.year


def by_route(bus: Bus) -> str:
    """Стратегия сортировки по маршруту"""
    return bus.route


def by_battery_capacity(bus: Bus) -> float:
    """
    Стратегия сортировки по емкости батареи (только для ElectricBus)
    Для других автобусов возвращает 0
    """
    if isinstance(bus, ElectricBus):
        return bus.battery_capacity
    return 0


def by_fuel_efficiency(bus: Bus) -> float:
    """
    Стратегия сортировки по расходу топлива (меньше - лучше)
    Для дизельных автобусов возвращает расход, для остальных - большое число
    """
    if isinstance(bus, DieselBus):
        return bus.fuel_consumption
    return float('inf')


def by_combined(bus: Bus) -> tuple:
    """
    Стратегия сортировки по нескольким атрибутам: (год, вместимость, номер)
    """
    return (bus.year, bus.capacity, bus.number)


# ==================== ФУНКЦИИ-ФИЛЬТРЫ ====================

def is_electric(bus: Bus) -> bool:
    """Фильтр: только электрические автобусы"""
    return isinstance(bus, ElectricBus)


def is_diesel(bus: Bus) -> bool:
    """Фильтр: только дизельные автобусы"""
    return isinstance(bus, DieselBus)


def is_modern(bus: Bus) -> bool:
    """Фильтр: автобусы новее 2020 года"""
    return bus.year > 2020


def has_high_capacity(bus: Bus) -> bool:
    """Фильтр: автобусы с вместимостью больше 45 человек"""
    return bus.capacity > 45


def by_min_year(min_year: int) -> Callable[[Bus], bool]:
    """
    ФАБРИКА ФУНКЦИЙ: создает фильтр для автобусов не старше указанного года
    """

    def filter_fn(bus: Bus) -> bool:
        return bus.year >= min_year

    return filter_fn


def by_max_capacity(max_capacity: int) -> Callable[[Bus], bool]:
    """
    ФАБРИКА ФУНКЦИЙ: создает фильтр для автобусов с вместимостью не больше указанной
    """

    def filter_fn(bus: Bus) -> bool:
        return bus.capacity <= max_capacity

    return filter_fn


def by_route_contains(substring: str) -> Callable[[Bus], bool]:
    """
    ФАБРИКА ФУНКЦИЙ: создает фильтр для автобусов, в маршруте которых есть подстрока
    """

    def filter_fn(bus: Bus) -> bool:
        return substring.lower() in bus.route.lower()

    return filter_fn


# ==================== ФУНКЦИИ ПРЕОБРАЗОВАНИЯ ДЛЯ MAP ====================

def to_short_string(bus: Bus) -> str:
    """Преобразует автобус в короткую строку"""
    return f"{bus.number} ({bus.route})"


def to_dict(bus: Bus) -> dict:
    """Преобразует автобус в словарь"""
    result = {
        'number': bus.number,
        'capacity': bus.capacity,
        'route': bus.route,
        'year': bus.year
    }

    if isinstance(bus, ElectricBus):
        result['type'] = 'electric'
        result['battery'] = bus.battery_capacity
    elif isinstance(bus, DieselBus):
        result['type'] = 'diesel'
        result['consumption'] = bus.fuel_consumption
    else:
        result['type'] = 'regular'

    return result


def to_number(bus: Bus) -> str:
    """Извлекает номер автобуса"""
    return bus.number


def to_year(bus: Bus) -> int:
    """Извлекает год выпуска"""
    return bus.year


# ==================== ФУНКЦИИ ПРИМЕНЕНИЯ ====================

def print_info(bus: Bus) -> None:
    """Выводит информацию об автобусе"""
    print(f"  -> {bus}")


def add_years(years: int) -> Callable[[Bus], None]:
    """
    ФАБРИКА ФУНКЦИЙ: создает функцию для добавления лет к году выпуска
    """

    def apply_fn(bus: Bus) -> None:
        # В реальном коде нужно создать новый объект, но для демонстрации:
        bus._year += years

    return apply_fn


def apply_discount_to_capacity(discount: float) -> Callable[[Bus], None]:
    """
    ФАБРИКА ФУНКЦИЙ: создает функцию для "уменьшения" вместимости
    (демонстрация применения к объектам)
    """

    def apply_fn(bus: Bus) -> None:
        bus._capacity = int(bus._capacity * (1 - discount))

    return apply_fn
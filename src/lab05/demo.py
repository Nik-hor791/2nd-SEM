"""
Демонстрация лабораторной работы №5 - Функции как аргументы (Задание на 4)
"""

from base import Bus
from models import ElectricBus, DieselBus
from collection import BusFleet
from strategies import *


def print_separator(title: str):
    """Вспомогательная функция для вывода разделителей"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def print_list(items, title: str = ""):
    """Вспомогательная функция для вывода списка"""
    if title:
        print(f"\n{title}:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")


def main():
    # ==================== СОЗДАНИЕ КОЛЛЕКЦИИ ====================
    print_separator("1. СОЗДАНИЕ КОЛЛЕКЦИИ АВТОБУСОВ")

    fleet = BusFleet()

    # Добавляем разные типы автобусов (минимум 5)
    fleet.add(ElectricBus("E001", 40, "Route A", 2023, 300, 2.5))
    fleet.add(ElectricBus("E002", 35, "Route B", 2021, 250, 2.0))
    fleet.add(DieselBus("D001", 50, "Route C", 2022, 200, 25))
    fleet.add(DieselBus("D002", 55, "Route D", 2020, 220, 28))
    fleet.add(Bus("B001", 30, "Route E", 2019))
    fleet.add(ElectricBus("E003", 45, "Route F", 2024, 350, 3.0))

    print(f"Создана коллекция из {len(fleet)} автобусов:")
    print(fleet)

    # ==================== СОРТИРОВКА СТРАТЕГИЯМИ ====================
    print_separator("2. СОРТИРОВКА РАЗНЫМИ СТРАТЕГИЯМИ")

    # Стратегия 1: по номеру
    fleet_copy = BusFleet()
    for bus in fleet.get_all():
        fleet_copy.add(bus)

    print("\n2.1 Сортировка по НОМЕРУ (by_number):")
    fleet_copy.sort_by(by_number)
    for bus in fleet_copy.get_all():
        print(f"   {bus.number} - {bus.route}")

    # Стратегия 2: по вместимости
    fleet_copy = BusFleet()
    for bus in fleet.get_all():
        fleet_copy.add(bus)

    print("\n2.2 Сортировка по ВМЕСТИМОСТИ (by_capacity):")
    fleet_copy.sort_by(by_capacity)
    for bus in fleet_copy.get_all():
        print(f"   {bus.capacity} мест - {bus.number}")

    # Стратегия 3: по году выпуска
    fleet_copy = BusFleet()
    for bus in fleet.get_all():
        fleet_copy.add(bus)

    print("\n2.3 Сортировка по ГОДУ (by_year):")
    fleet_copy.sort_by(by_year)
    for bus in fleet_copy.get_all():
        print(f"   {bus.year} год - {bus.number}")

    # Стратегия 4: комбинированная
    fleet_copy = BusFleet()
    for bus in fleet.get_all():
        fleet_copy.add(bus)

    print("\n2.4 Сортировка по КОМБИНАЦИИ (by_combined - год, вместимость, номер):")
    fleet_copy.sort_by(by_combined)
    for bus in fleet_copy.get_all():
        print(f"   {bus.year} год, {bus.capacity} мест, номер {bus.number}")

    # ==================== ФИЛЬТРАЦИЯ ====================
    print_separator("3. ФИЛЬТРАЦИЯ РАЗНЫМИ ФИЛЬТРАМИ")

    # Фильтр 1: только электрические
    electric_fleet = BusFleet()
    for bus in fleet.get_all():
        if is_electric(bus):
            electric_fleet.add(bus)

    print("\n3.1 Фильтр 'Только электрические автобусы':")
    print(electric_fleet)

    # Фильтр 2: современные автобусы
    modern_fleet = BusFleet()
    for bus in fleet.get_all():
        if is_modern(bus):
            modern_fleet.add(bus)

    print("\n3.2 Фильтр 'Современные автобусы (после 2020 года)':")
    print(modern_fleet)

    # Фильтр 3: высокая вместимость
    print("\n3.3 Фильтр 'Высокая вместимость (>45 мест)':")
    high_cap = [bus for bus in fleet.get_all() if has_high_capacity(bus)]
    for bus in high_cap:
        print(f"   {bus.number}: {bus.capacity} мест")

    # ==================== ПРИМЕНЕНИЕ MAP() ====================
    print_separator("4. ПРЕОБРАЗОВАНИЕ КОЛЛЕКЦИИ ЧЕРЕЗ map()")

    # Преобразование 1: в строки
    strings = list(map(to_short_string, fleet.get_all()))
    print("\n4.1 Преобразование в короткие строки:")
    for s in strings:
        print(f"   {s}")

    # Преобразование 2: в словари
    dicts = list(map(to_dict, fleet.get_all()))
    print("\n4.2 Преобразование в словари (первые 3):")
    for i, d in enumerate(dicts[:3], 1):
        print(f"   {i}. {d}")

    # Преобразование 3: извлечение номеров
    numbers = list(map(to_number, fleet.get_all()))
    print(f"\n4.3 Извлечение номеров: {numbers}")

    # Преобразование 4: извлечение годов с лямбдой
    years = list(map(lambda bus: bus.year, fleet.get_all()))
    print(f"\n4.4 Извлечение годов (через лямбду): {years}")

    # ==================== ФАБРИКИ ФУНКЦИЙ ====================
    print_separator("5. ФАБРИКИ ФУНКЦИЙ")

    # Фабрика 1: фильтр по году
    print("\n5.1 Фильтр 'Автобусы после 2022 года' (фабрика by_min_year(2022)):")
    filter_2022 = by_min_year(2022)
    recent_buses = [bus for bus in fleet.get_all() if filter_2022(bus)]
    for bus in recent_buses:
        print(f"   {bus.number} - {bus.year} год")

    # Фабрика 2: фильтр по вместимости
    print("\n5.2 Фильтр 'Не более 40 мест' (фабрика by_max_capacity(40)):")
    filter_cap40 = by_max_capacity(40)
    small_buses = [bus for bus in fleet.get_all() if filter_cap40(bus)]
    for bus in small_buses:
        print(f"   {bus.number} - {bus.capacity} мест")

    # Фабрика 3: фильтр по маршруту
    print("\n5.3 Фильтр 'Маршрут содержит Route' (фабрика by_route_contains('Route')):")
    filter_route = by_route_contains("Route")
    route_buses = [bus for bus in fleet.get_all() if filter_route(bus)]
    for bus in route_buses:
        print(f"   {bus.number} - {bus.route}")

    # ==================== МЕТОДЫ COLLECTION SORT_BY/FILTER_BY ====================
    print_separator("6. МЕТОДЫ КОЛЛЕКЦИИ sort_by() И filter_by()")

    # Сортировка методом коллекции
    fleet_sorted = BusFleet()
    for bus in fleet.get_all():
        fleet_sorted.add(bus)

    print("\n6.1 Сортировка методом sort_by(by_capacity):")
    fleet_sorted.sort_by(by_capacity)
    print(fleet_sorted)

    # Фильтрация методом коллекции
    fleet_filtered = BusFleet()
    for bus in fleet.get_all():
        fleet_filtered.add(bus)

    print("\n6.2 Фильтрация методом filter_by(is_electric):")
    fleet_filtered.filter_by(is_electric)
    print(fleet_filtered)

    # ==================== СРАВНЕНИЕ LAMBDA И ИМЕНОВАННЫХ ФУНКЦИЙ ====================
    print_separator("7. СРАВНЕНИЕ lambda И ИМЕНОВАННЫХ ФУНКЦИЙ")

    # Именованная функция
    print("\n7.1 Сортировка через ИМЕНОВАННУЮ функцию (by_capacity):")
    named_sorted = sorted(fleet.get_all(), key=by_capacity)
    for bus in named_sorted[:3]:
        print(f"   {bus.number}: {bus.capacity} мест")

    # Lambda выражение
    print("\n7.2 Сортировка через ЛЯМБДА-функцию (по вместимости):")
    lambda_sorted = sorted(fleet.get_all(), key=lambda b: b.capacity)
    for bus in lambda_sorted[:3]:
        print(f"   {bus.number}: {bus.capacity} мест")

    # Именованная функция для фильтрации
    print("\n7.3 Фильтрация через ИМЕНОВАННУЮ функцию (is_modern):")
    modern_named = list(filter(is_modern, fleet.get_all()))
    for bus in modern_named:
        print(f"   {bus.number} - {bus.year} год")

    # Lambda для фильтрации
    print("\n7.4 Фильтрация через ЛЯМБДА-функцию (год > 2021):")
    modern_lambda = list(filter(lambda b: b.year > 2021, fleet.get_all()))
    for bus in modern_lambda:
        print(f"   {bus.number} - {bus.year} год")

    # ==================== ЦЕПОЧКИ ОПЕРАЦИЙ ====================
    print_separator("8. ЦЕПОЧКИ ОПЕРАЦИЙ ЧЕРЕЗ ВОЗВРАТ self")

    # Создаем копию для цепочечных операций
    chain_fleet = BusFleet()
    for bus in fleet.get_all():
        chain_fleet.add(bus)

    print("\nИсходная коллекция:")
    print(chain_fleet)

    print("\n8.1 Цепочка: filter_by(is_electric) -> sort_by(by_year) -> apply(print_info)")
    (chain_fleet
     .filter_by(is_electric)
     .sort_by(by_year)
     .apply(print_info))

    # Другая цепочка
    chain_fleet2 = BusFleet()
    for bus in fleet.get_all():
        chain_fleet2.add(bus)

    print("\n8.2 Цепочка: filter_by(by_max_capacity(45)) -> sort_by(by_route) -> map(to_short_string)")
    result = (chain_fleet2
              .filter_by(by_max_capacity(45))
              .sort_by(by_route)
              .map(to_short_string))

    for item in result:
        print(f"   {item}")

    # ==================== ВСТРОЕННЫЕ ФУНКЦИИ ====================
    print_separator("9. ИСПОЛЬЗОВАНИЕ ВСТРОЕННЫХ ФУНКЦИЙ map/filter/sorted")

    # map с лямбдой
    print("\n9.1 map + lambda: увеличение вместимости на 5 мест")
    increased = list(map(lambda b: f"{b.number}: {b.capacity} -> {b.capacity + 5}", fleet.get_all()))
    for item in increased[:3]:
        print(f"   {item}")

    # filter с несколькими условиями
    print("\n9.2 filter + лямбда: автобусы с вместимостью 40-50 мест")
    mid_capacity = list(filter(lambda b: 40 <= b.capacity <= 50, fleet.get_all()))
    for bus in mid_capacity:
        print(f"   {bus.number}: {bus.capacity} мест")

    # sorted с лямбдой
    print("\n9.3 sorted + лямбда: сортировка по убыванию вместимости")
    sorted_desc = sorted(fleet.get_all(), key=lambda b: b.capacity, reverse=True)
    for bus in sorted_desc:
        print(f"   {bus.number}: {bus.capacity} мест")

    print_separator("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")

if __name__ == "__main__":
    main()
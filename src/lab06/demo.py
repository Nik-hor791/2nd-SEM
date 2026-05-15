"""
Демонстрация лабораторной работы №6 - Generics и typing (Задание на 3)
"""

from base import Bus
from models import ElectricBus, DieselBus
from container import TypedCollection


def print_separator(title: str) -> None:
    """Вспомогательная функция для вывода разделителей"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def main() -> None:
    print_separator("ЛАБОРАТОРНАЯ РАБОТА №6 - GENERICS И TYPING")

    # ==================== ЧАСТЬ 1: ДЕМОНСТРАЦИЯ АННОТАЦИЙ ТИПОВ ====================
    print_separator("1. ОБЪЕКТЫ С АННОТАЦИЯМИ ТИПОВ")

    # Создаем объекты разных типов
    bus1: Bus = Bus("A001", 40, "Route 10", 2020)
    electric1: ElectricBus = ElectricBus("E001", 50, "Route 20", 2023, 300.0, 2.5)
    diesel1: DieselBus = DieselBus("D001", 55, "Route 30", 2022, 250.0, 28.0)

    print("\nСозданы объекты с аннотациями типов:")
    print(f"  {bus1}")
    print(f"  {electric1}")
    print(f"  {diesel1}")

    # Демонстрация работы методов с аннотациями
    print("\nДемонстрация методов с аннотациями типов:")
    print(f"  bus1.can_take_passengers(35) -> {bus1.can_take_passengers(35)}")
    print(f"  electric1.calculate_range() -> {electric1.calculate_range():.1f} км")
    print(f"  diesel1.calculate_range() -> {diesel1.calculate_range():.1f} км")

    # ==================== ЧАСТЬ 2: СОЗДАНИЕ TYPEDCOLLECTION ====================
    print_separator("2. СОЗДАНИЕ TYPEDCOLLECTION ДЛЯ РАЗНЫХ ТИПОВ")

    # Коллекция для Bus
    bus_collection: TypedCollection[Bus] = TypedCollection()
    print("\n2.1 TypedCollection[Bus] - коллекция для базового типа")

    bus_collection.add(bus1)
    bus_collection.add(Bus("A002", 35, "Route 11", 2021))
    bus_collection.add(Bus("A003", 45, "Route 12", 2019))

    print(f"Добавлено {len(bus_collection)} автобусов:")
    print(bus_collection)

    # Коллекция для ElectricBus
    electric_collection: TypedCollection[ElectricBus] = TypedCollection()
    print("\n2.2 TypedCollection[ElectricBus] - коллекция для электроавтобусов")

    electric_collection.add(electric1)
    electric_collection.add(ElectricBus("E002", 45, "Route 21", 2024, 350.0, 3.0))
    electric_collection.add(ElectricBus("E003", 40, "Route 22", 2022, 280.0, 2.2))

    print(f"Добавлено {len(electric_collection)} электроавтобусов:")
    print(electric_collection)

    # Коллекция для DieselBus
    diesel_collection: TypedCollection[DieselBus] = TypedCollection()
    print("\n2.3 TypedCollection[DieselBus] - коллекция для дизельных автобусов")

    diesel_collection.add(diesel1)
    diesel_collection.add(DieselBus("D002", 50, "Route 31", 2023, 260.0, 26.0))
    diesel_collection.add(DieselBus("D003", 48, "Route 32", 2021, 230.0, 24.0))

    print(f"Добавлено {len(diesel_collection)} дизельных автобусов:")
    print(diesel_collection)

    # ==================== ЧАСТЬ 3: ВАЛИДАЦИЯ ТИПОВ ====================
    print_separator("3. ВАЛИДАЦИЯ ТИПОВ ПРИ ДОБАВЛЕНИИ")

    print("\n3.1 Правильное использование - только объекты ElectricBus:")
    electric_only = TypedCollection[ElectricBus]()
    electric_only.add(ElectricBus("E004", 42, "Route 23", 2023, 320.0, 2.8))
    print(f"  Добавлен: {electric_only.get_all()[0]}")

    # Демонстрация метода get_all
    print("\n3.2 Метод get_all() возвращает список с правильным типом:")
    items: list[ElectricBus] = electric_collection.get_all()
    print(f"  Получено {len(items)} элементов")
    for item in items:
        print(f"    - {item.number}: {item.battery_capacity} kWh")

    # ==================== ЧАСТЬ 4: МЕТОДЫ КОЛЛЕКЦИИ ====================
    print_separator("4. МЕТОДЫ TYPEDCOLLECTION")

    # Сортировка
    print("\n4.1 Сортировка по вместимости:")
    sorted_by_capacity = TypedCollection[Bus]()
    for bus in bus_collection.get_all():
        sorted_by_capacity.add(bus)

    sorted_by_capacity.sort_by(lambda b: b.capacity)
    for bus in sorted_by_capacity.get_all():
        print(f"    {bus.number}: {bus.capacity} мест")

    # Фильтрация
    print("\n4.2 Фильтрация (только электроавтобусы с батареей > 300 kWh):")
    filtered = TypedCollection[ElectricBus]()
    for bus in electric_collection.get_all():
        filtered.add(bus)

    filtered.filter_by(lambda b: b.battery_capacity > 300)
    for bus in filtered.get_all():
        print(f"    {bus.number}: {bus.battery_capacity} kWh")

    # Apply
    print("\n4.3 Применение функции apply() (вывод информации):")
    apply_collection = TypedCollection[Bus]()
    for bus in bus_collection.get_all():
        apply_collection.add(bus)

    apply_collection.apply(lambda b: print(f"    Применено к: {b.number}"))

    # Map
    print("\n4.4 Преобразование через map() (извлечение номеров):")
    numbers = bus_collection.map(lambda b: b.number)
    print(f"    Номера автобусов: {numbers}")

    # Find
    print("\n4.5 Поиск элементов:")
    found = electric_collection.find_first(lambda b: b.battery_capacity > 300)
    if found:
        print(f"    Найден электроавтобус: {found.number} ({found.battery_capacity} kWh)")

    all_found = electric_collection.find_all(lambda b: b.capacity >= 45)
    print(f"    Найдено электроавтобусов с вместимостью >= 45: {len(all_found)}")

    # ==================== ЧАСТЬ 5: ПОЛУЧЕНИЕ ВСЕХ ЭЛЕМЕНТОВ ====================
    print_separator("5. ПОЛУЧЕНИЕ ВСЕХ ЭЛЕМЕНТОВ И ИХ ВЫВОД")

    print("\n5.1 Все элементы TypedCollection[Bus]:")
    all_buses = bus_collection.get_all()
    for i, bus in enumerate(all_buses, 1):
        print(f"    {i}. {bus}")

    print("\n5.2 Все элементы TypedCollection[ElectricBus]:")
    all_electric = electric_collection.get_all()
    for i, bus in enumerate(all_electric, 1):
        print(f"    {i}. {bus}")

    print("\n5.3 Все элементы TypedCollection[DieselBus]:")
    all_diesel = diesel_collection.get_all()
    for i, bus in enumerate(all_diesel, 1):
        print(f"    {i}. {bus}")

    # ==================== ЧАСТЬ 6: ОПЕРАТОРЫ КОЛЛЕКЦИИ ====================
    print_separator("6. ОПЕРАТОРЫ И МЕТОДЫ КОЛЛЕКЦИИ")

    print("\n6.1 Оператор len():")
    print(f"    Количество автобусов: {len(bus_collection)}")

    print("\n6.2 Оператор in (проверка наличия):")
    test_bus = Bus("A001", 40, "Route 10", 2020)
    print(f"    {test_bus.number} в коллекции? {test_bus in bus_collection}")

    print("\n6.3 Доступ по индексу (__getitem__):")
    if len(bus_collection) > 0:
        print(f"    Первый элемент: {bus_collection[0]}")

    # ==================== ЧАСТЬ 7: ПРИМЕРЫ С РАЗНЫМИ ТИПАМИ ====================
    print_separator("7. ПРИМЕРЫ С РАЗНЫМИ ТИПАМИ ДАННЫХ")

    # Коллекция строк
    string_collection: TypedCollection[str] = TypedCollection()
    string_collection.add("Первый автобус")
    string_collection.add("Второй автобус")
    string_collection.add("Третий автобус")

    print("\n7.1 TypedCollection[str]:")
    print(f"    {string_collection}")

    # Коллекция чисел
    int_collection: TypedCollection[int] = TypedCollection()
    int_collection.add(100)
    int_collection.add(200)
    int_collection.add(300)

    print("\n7.2 TypedCollection[int]:")
    print(f"    {int_collection}")

    # Коллекция смешанная (Union типов) - но лучше использовать базовый класс
    mixed_collection: TypedCollection[Bus] = TypedCollection()
    mixed_collection.add(Bus("M001", 40, "Mix Route", 2020))
    mixed_collection.add(ElectricBus("M002", 45, "Mix Electric", 2023, 300, 2.5))
    mixed_collection.add(DieselBus("M003", 50, "Mix Diesel", 2022, 250, 28))

    print("\n7.3 TypedCollection[Bus] (может хранить любой наследник Bus):")
    print(f"    {mixed_collection}")




if __name__ == "__main__":
    main()
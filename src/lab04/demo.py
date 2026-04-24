from models import ElectricBus, DieselBus, SimpleBus
from interfaces import Printable, Comparable, Chargeable, Refuelable


def print_all(items: list[Printable]):
    """
    Универсальная функция, работающая через интерфейс Printable
    (Использование интерфейса как типа)
    """
    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСА PRINTABLE")
    print("Функция принимает список объектов Printable")
    print("=" * 70)

    for i, item in enumerate(items, 1):
        print(f"\n{i}. {item.to_string()}")
        print(f"   Кратко: {item.get_short_info()}")


def compare_objects(obj1: Comparable, obj2: Comparable):
    """
    Универсальная функция сравнения через интерфейс Comparable
    """
    print(f"СРАВНЕНИЕ ЧЕРЕЗ ИНТЕРФЕЙС COMPARABLE")
    print(f"   Объект 1: {obj1.get_short_info()}")
    print(f"   Объект 2: {obj2.get_short_info()}")

    result = obj1.compare_to(obj2)

    if result < 0:
        print(f"   Результат: {result} (Первый МЕНЬШЕ второго)")
    elif result == 0:
        print(f"   Результат: {result} (Объекты РАВНЫ)")
    else:
        print(f"   Результат: {result} (Первый БОЛЬШЕ второго)")


def demonstrate_chargeable(obj: Chargeable):
    """
    Функция для работы с заряжаемыми объектами
    """
    print(f"\nРАБОТА С ЗАРЯЖАЕМЫМ ОБЪЕКТОМ")
    print(f"   {obj.get_short_info()}")
    print(f"   Текущий заряд: {obj.get_battery_percentage()}%")
    print(f"   → {obj.charge(1.0)}")


def demonstrate_refuelable(obj: Refuelable):
    """
    Функция для работы с заправляемыми объектами
    """
    print(f"\nРАБОТА С ЗАПРАВЛЯЕМЫМ ОБЪЕКТОМ")
    print(f"   {obj.get_short_info()}")
    print(f"   Текущий уровень топлива: {obj.get_fuel_level()}%")
    print(f"   → {obj.refuel(50)}")


def check_interfaces(obj, interfaces: list):
    """
    Проверка реализации интерфейсов через isinstance
    """
    print(f"\nПРОВЕРКА ИНТЕРФЕЙСОВ ДЛЯ {obj.get_short_info()}")
    print("   " + "=" * 50)

    for interface in interfaces:
        if isinstance(obj, interface):
            print(f"   Реализует {interface.__name__}")
        else:
            print(f"   НЕ реализует {interface.__name__}")


def main():
    print("=" * 70)
    print("ЛАБОРАТОРНАЯ РАБОТА №4 - ИНТЕРФЕЙСЫ И АБСТРАКТНЫЕ КЛАССЫ")
    print("=" * 70)

    # 1. СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ
    print("\n" + "=" * 70)
    print("1. СОЗДАНИЕ ОБЪЕКТОВ")
    print("=" * 70)

    electric1 = ElectricBus("E001", 50, "Route 10", 2023, 300.0, 2.5)
    electric2 = ElectricBus("E002", 45, "Route 12", 2024, 350.0, 3.0)

    diesel1 = DieselBus("D001", 55, "Route 20", 2022, 250.0, 28.0)
    diesel2 = DieselBus("D002", 48, "Route 22", 2023, 220.0, 24.0)

    simple1 = SimpleBus("S001", 40, "Route 30", 2020)
    simple2 = SimpleBus("S002", 35, "Route 31", 2021)

    print("Созданы:")
    print(f"   - Электроавтобусы: {electric1.get_short_info()}, {electric2.get_short_info()}")
    print(f"   - Дизельные автобусы: {diesel1.get_short_info()}, {diesel2.get_short_info()}")
    print(f"   - Обычные автобусы: {simple1.get_short_info()}, {simple2.get_short_info()}")

    # 2. ДЕМОНСТРАЦИЯ PRINTABLE ИНТЕРФЕЙСА
    print("\n" + "=" * 70)
    print("2. ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСА PRINTABLE")
    print("=" * 70)

    # Функция работает с любыми объектами, реализующими Printable
    printable_list: list[Printable] = [electric1, diesel1, simple1, electric2, diesel2]
    print_all(printable_list)

    # 3. ДЕМОНСТРАЦИЯ COMPARABLE ИНТЕРФЕЙСА
    print("\n" + "=" * 70)
    print("3. ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСА COMPARABLE")
    print("=" * 70)

    compare_objects(electric1, electric2)  # Сравнение электроавтобусов
    compare_objects(diesel1, diesel2)  # Сравнение дизельных автобусов

    # 4. ДЕМОНСТРАЦИЯ CHARGEABLE ИНТЕРФЕЙСА
    print("\n" + "=" * 70)
    print("4. ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСА CHARGEABLE")
    print("=" * 70)

    demonstrate_chargeable(electric1)
    demonstrate_chargeable(electric2)

    # 5. ДЕМОНСТРАЦИЯ REFUELABLE ИНТЕРФЕЙСА
    print("\n" + "=" * 70)
    print("5. ДЕМОНСТРАЦИЯ ИНТЕРФЕЙСА REFUELABLE")
    print("=" * 70)

    demonstrate_refuelable(diesel1)
    demonstrate_refuelable(diesel2)

    # 6. ПРОВЕРКА isinstance ДЛЯ РАЗНЫХ ИНТЕРФЕЙСОВ
    print("\n" + "=" * 70)
    print("6. ПРОВЕРКА РЕАЛИЗАЦИИ ИНТЕРФЕЙСОВ ЧЕРЕЗ isinstance()")
    print("=" * 70)

    all_interfaces = [Printable, Comparable, Chargeable, Refuelable]

    check_interfaces(electric1, all_interfaces)
    check_interfaces(diesel1, all_interfaces)
    check_interfaces(simple1, all_interfaces)

    # 7. РАЗНОЕ ПОВЕДЕНИЕ У РАЗНЫХ КЛАССОВ
    print("\n" + "=" * 70)
    print("7. РАЗНОЕ ПОВЕДЕНИЕ МЕТОДОВ В РАЗНЫХ КЛАССАХ")
    print("=" * 70)

    print("\nМетод to_string():")
    print(f"   ElectricBus: {electric1.to_string()}")
    print(f"   DieselBus:   {diesel1.to_string()}")
    print(f"   SimpleBus:   {simple1.to_string()}")

    print("\nМетод get_short_info():")
    print(f"   ElectricBus: {electric1.get_short_info()}")
    print(f"   DieselBus:   {diesel1.get_short_info()}")
    print(f"   SimpleBus:   {simple1.get_short_info()}")

    print("\nМетод compare_to():")
    print(
        f"   ElectricBus: сравнивает по емкости батареи ({electric1.battery_capacity} vs {electric2.battery_capacity} kWh)")
    print(
        f"   DieselBus:   сравнивает по расходу топлива ({diesel1.fuel_consumption} vs {diesel2.fuel_consumption} L/100km)")

    # 8. ПОЛИМОРФИЗМ ЧЕРЕЗ ИНТЕРФЕЙСЫ
    print("\n" + "=" * 70)
    print("8. ПОЛИМОРФИЗМ - РАБОТА С РАЗНЫМИ ОБЪЕКТАМИ ЧЕРЕЗ ЕДИНЫЙ ИНТЕРФЕЙС")
    print("=" * 70)

    # Список объектов с разными типами, но реализующими Printable
    polymorphic_list = [electric1, diesel1, simple1, electric2, diesel2, simple2]

    print("\nВывод всех объектов через единый интерфейс Printable:")
    for obj in polymorphic_list:
        print(f"   → {obj.get_short_info()}")  # Полиморфный вызов

    # Функция принимает объекты с разными типами
    print("\nПример полиморфизма в функции:")
    print("   Функция compare_objects() принимает ЛЮБЫЕ объекты с интерфейсом Comparable")
    compare_objects(electric2, electric1)  # Работает с ElectricBus

    # Работа с Chargeable - оба метода из интерфейса
    print("\nРабота с Chargeable интерфейсом:")
    charging_objects = [electric1, electric2]
    for obj in charging_objects:
        print(f"   {obj.get_short_info()} → заряд: {obj.get_battery_percentage()}%")

    # 9. ДОПОЛНИТЕЛЬНАЯ ДЕМОНСТРАЦИЯ МНОЖЕСТВЕННОЙ РЕАЛИЗАЦИИ
    print("\n" + "=" * 70)
    print("9. МНОЖЕСТВЕННАЯ РЕАЛИЗАЦИЯ ИНТЕРФЕЙСОВ")
    print("=" * 70)

    print("\nElectricBus реализует:")
    print("   - Printable (to_string, get_short_info)")
    print("   - Comparable (compare_to)")
    print("   - Chargeable (charge, get_battery_percentage)")

    print("\nDieselBus реализует:")
    print("   - Printable (to_string, get_short_info)")
    print("   - Comparable (compare_to)")
    print("   - Refuelable (refuel, get_fuel_level)")

    print("\nSimpleBus реализует:")
    print("   - Printable (to_string, get_short_info)")

    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("Все требования задания на 4 выполнены:")
    print("✓ Использование интерфейса как типа")
    print("✓ Универсальная функция через интерфейс")
    print("✓ Множественная реализация интерфейсов")
    print("✓ Проверка через isinstance()")
    print("=" * 70)


if __name__ == "__main__":
    main()
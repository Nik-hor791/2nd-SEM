from model import Bus
from collection import BusFleet


def main():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КОЛЛЕКЦИИ BusFleet")
    print("=" * 60)

    # Создание нескольких объектов Bus
    print("\n1. СОЗДАНИЕ АВТОБУСОВ:")
    bus1 = Bus("A123BC", 50, "Central Station - Airport", 2018)
    bus2 = Bus("B456CD", 40, "City Center - University", 2020)
    bus3 = Bus("C789EF", 60, "North Terminal - South Mall", 2022)
    bus4 = Bus("D012GH", 35, "Railway Station - Old Town", 2019)

    print(f" Создан {bus1}")
    print(f" Создан {bus2}")
    print(f" Создан {bus3}")
    print(f" Создан {bus4}")

    # Создание коллекции и добавление автобусов
    print("\n2. ДОБАВЛЕНИЕ В КОЛЛЕКЦИЮ:")
    fleet = BusFleet()

    fleet.add(bus1)
    fleet.add(bus2)
    fleet.add(bus3)
    fleet.add(bus4)

    # Вывод всех элементов
    print("\n3. ВСЕ АВТОБУСЫ В КОЛЛЕКЦИИ:")
    all_buses = fleet.get_all()
    for bus in all_buses:
        print(f"   • {bus}")

    # Проверка типа (попытка добавить неправильный объект)
    print("\n4. ПРОВЕРКА ТИПИЗАЦИИ:")
    try:
        print("   Пытаемся добавить строку вместо автобуса")
        fleet.add("не автобус")
    except TypeError as e:
        print(f" Ошибка: {e}")

    try:
        print("   Пытаемся добавить число")
        fleet.add(123)
    except TypeError as e:
        print(f" Ошибка: {e}")

    # Удаление элемента
    print("\n5. УДАЛЕНИЕ АВТОБУСА:")
    print(f"   Удаляем {bus2.number}")
    fleet.remove(bus2)

    # Повторный вывод коллекции
    print("\n6. КОЛЛЕКЦИЯ ПОСЛЕ УДАЛЕНИЯ:")
    print(fleet)

    # Дополнительная проверка: удаление несуществующего объекта
    print("\n7. ПОПЫТКА УДАЛИТЬ НЕСУЩЕСТВУЮЩИЙ АВТОБУС:")
    fake_bus = Bus("FAKE99", 10, "Fake Route", 2023)
    fleet.remove(fake_bus)

    # Демонстрация метода get_all
    print("\n8. ПРОВЕРКА МЕТОДА get_all():")
    buses_copy = fleet.get_all()
    print(f"   Получено {len(buses_copy)} автобусов через get_all()")
    print(f"   Это копия? {buses_copy is not fleet._items}")  # True, если копия

    # Дополнительная информация о коллекции
    print("\n9. СТАТИСТИКА КОЛЛЕКЦИИ:")
    print(f"   Количество автобусов: {len(fleet)}")
    print(f"   Общая вместимость: {sum(bus.capacity for bus in fleet.get_all())} пассажиров")
    print(f"   Средний год выпуска: {sum(bus.year for bus in fleet.get_all()) / len(fleet):.0f}")

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()
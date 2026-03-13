from model import Bus

def main():
    # создание объекта
    bus1 = Bus("A123BC", 50, "Central Station - Airport", 2018)
    bus2 = Bus("B456CD", 40, "City Center - University", 2020)

 # вывод через print
    print("Информация об автобусах:")
    print(bus1)
    print(bus2)

    print()

    # сравнение двух объектов
    print("Сравнение автобусов:")
    if bus1 == bus2:
        print("Автобусы одинаковые")
    else:
        print("Автобусы разные")

    print()

    # проверка бизнес-метода
    passengers = 45
    print(f"Может ли автобус {bus1.number} взять {passengers} пассажиров?")
    print(bus1.can_take_passengers(passengers))

    print()

    # пример некорректного создания
    print("Попытка создать некорректный объект:")
    try:
        bad_bus = Bus("", -10, "Test Route", 1800)
    except ValueError as e:
        print("Ошибка создания автобуса:", e)


if __name__ == "__main__":
    main()
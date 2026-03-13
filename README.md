# Лаба 1

Код model.py

```python
class Bus:
    def __init__(self, number: str, capacity: int, route: str, year: int):
        # базовая проверка данных
        if not number:
            raise ValueError("Номер автобуса не может быть пустым")
        if capacity <= 0:
            raise ValueError("Вместимость должна быть больше 0")
        if year < 1900:
            raise ValueError("Некорректный год выпуска")

        self._number = number
        self._capacity = capacity
        self._route = route
        self._year = year

    
    @property
````    def number(self):
        return self._number

    @property
    def capacity(self):
        return self._capacity

    @property
    def route(self):
        return self._route

    @property
    def year(self):
        return self._year

    # строковое представление объекта
    def __str__(self):
        return f"Bus {self._number} | Route: {self._route} | Capacity: {self._capacity} | Year: {self._year}"

    # сравнение автобусов
    def __eq__(self, other):
        if not isinstance(other, Bus):
            return False
        return self._number == other._number and self._route == other._route

    # простой бизнес-метод
    def can_take_passengers(self, passengers: int):
        """Проверяет, может ли автобус взять указанное количество пассажиров"""
        return passengers <= self._capacity

```

Код demo.py

```python
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
```

Вывод файла demo.py
![alt text](images/lab01/01.img`)

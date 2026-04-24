from interfaces import Printable, Comparable, Chargeable, Refuelable


class Bus:
    def __init__(self, number: str, capacity: int, route: str, year: int):
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
    def number(self):
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


class ElectricBus(Bus, Printable, Comparable, Chargeable):
    """Электроавтобус с реализацией интерфейсов"""

    def __init__(self, number: str, capacity: int, route: str, year: int,
                 battery_capacity: float, charging_time: float):
        super().__init__(number, capacity, route, year)
        self._battery_capacity = battery_capacity
        self._charging_time = charging_time
        self._battery_percentage = 100

    @property
    def battery_capacity(self):
        return self._battery_capacity

    @property
    def charging_time(self):
        return self._charging_time

    # Реализация Printable
    def to_string(self) -> str:
        return f"ElectricBus[{self._number}] | Route: {self._route} | Cap: {self._capacity} | Battery: {self._battery_capacity}kWh | Charge: {self._battery_percentage}%"

    def get_short_info(self) -> str:
        return f"E-{self._number} ({self._route}) 🔋{self._battery_percentage}%"

    # Реализация Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, ElectricBus):
            raise TypeError(f"Cannot compare ElectricBus with {type(other)}")

        if self._battery_capacity < other._battery_capacity:
            return -1
        elif self._battery_capacity == other._battery_capacity:
            return 0
        else:
            return 1

    # Реализация Chargeable
    def charge(self, hours: float) -> str:
        if hours <= 0:
            return "Invalid charging time"

        charge_added = (hours / self._charging_time) * 100
        self._battery_percentage = min(100, self._battery_percentage + charge_added)
        return f"Charged for {hours}h. Battery: {self._battery_percentage:.0f}%"

    def get_battery_percentage(self) -> int:
        return int(self._battery_percentage)

    def calculate_range(self, consumption_per_km: float = 0.8):
        return self._battery_capacity / consumption_per_km


class DieselBus(Bus, Printable, Comparable, Refuelable):
    """Дизельный автобус с реализацией интерфейсов"""

    def __init__(self, number: str, capacity: int, route: str, year: int,
                 fuel_tank_capacity: float, fuel_consumption: float):
        super().__init__(number, capacity, route, year)
        self._fuel_tank_capacity = fuel_tank_capacity
        self._fuel_consumption = fuel_consumption
        self._fuel_level = 100

    @property
    def fuel_tank_capacity(self):
        return self._fuel_tank_capacity

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    # Реализация Printable
    def to_string(self) -> str:
        return f"DieselBus[{self._number}] | Route: {self._route} | Cap: {self._capacity} | Tank: {self._fuel_tank_capacity}L | Fuel: {self._fuel_level}%"

    def get_short_info(self) -> str:
        return f"D-{self._number} ({self._route}) ⛽{self._fuel_level}%"

    # Реализация Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, DieselBus):
            raise TypeError(f"Cannot compare DieselBus with {type(other)}")

        if self._fuel_consumption < other._fuel_consumption:
            return -1
        elif self._fuel_consumption == other._fuel_consumption:
            return 0
        else:
            return 1

    # Реализация Refuelable
    def refuel(self, liters: float) -> str:
        if liters <= 0:
            return "Invalid fuel amount"

        max_liters = self._fuel_tank_capacity
        current_liters = (self._fuel_level / 100) * max_liters
        new_liters = min(max_liters, current_liters + liters)
        self._fuel_level = (new_liters / max_liters) * 100

        return f"Refueled {liters}L. Fuel level: {self._fuel_level:.0f}%"

    def get_fuel_level(self) -> int:
        return int(self._fuel_level)

    def calculate_range(self):
        return (self._fuel_tank_capacity / self._fuel_consumption) * 100


class SimpleBus(Bus, Printable):
    """Обычный автобус (реализует только Printable)"""

    def __init__(self, number: str, capacity: int, route: str, year: int):
        super().__init__(number, capacity, route, year)

    def to_string(self) -> str:
        return f"SimpleBus[{self._number}] | Route: {self._route} | Capacity: {self._capacity}"

    def get_short_info(self) -> str:
        return f"S-{self._number} ({self._route})"
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

    def __str__(self):
        return f"Bus {self._number} | Route: {self._route} | Capacity: {self._capacity} | Year: {self._year}"

    def __eq__(self, other):
        if not isinstance(other, Bus):
            return False
        return self._number == other._number and self._route == other._route

    def can_take_passengers(self, passengers: int):
        return passengers <= self._capacity
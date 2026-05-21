class Bus:
    
    def __init__(self, number: str, capacity: int, route: str, year: int) -> None:
        if not number:
            raise ValueError("Номер автобуса не может быть пустым")
        if capacity <= 0:
            raise ValueError("Вместимость должна быть больше 0")
        if year < 1900:
            raise ValueError("Некорректный год выпуска")

        self._number: str = number
        self._capacity: int = capacity
        self._route: str = route
        self._year: int = year

    @property
    def number(self) -> str:
        return self._number

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def route(self) -> str:
        return self._route

    @property
    def year(self) -> int:
        return self._year

    def __str__(self) -> str:
        return f"Bus {self._number} | Route: {self._route} | Capacity: {self._capacity} | Year: {self._year}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bus):
            return False
        return self._number == other._number and self._route == other._route

    def can_take_passengers(self, passengers: int) -> bool:
        return passengers <= self._capacity
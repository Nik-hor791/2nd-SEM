class Bus:
    """Базовый класс автобуса с аннотациями типов"""
    
    def __init__(self, number: str, capacity: int, route: str, year: int) -> None:
        """
        Конструктор автобуса
        
        Args:
            number: Номер автобуса
            capacity: Вместимость
            route: Маршрут
            year: Год выпуска
        """
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
        """Возвращает номер автобуса"""
        return self._number

    @property
    def capacity(self) -> int:
        """Возвращает вместимость автобуса"""
        return self._capacity

    @property
    def route(self) -> str:
        """Возвращает маршрут автобуса"""
        return self._route

    @property
    def year(self) -> int:
        """Возвращает год выпуска автобуса"""
        return self._year

    def __str__(self) -> str:
        """Строковое представление автобуса"""
        return f"Bus {self._number} | Route: {self._route} | Capacity: {self._capacity} | Year: {self._year}"

    def __eq__(self, other: object) -> bool:
        """Сравнение автобусов"""
        if not isinstance(other, Bus):
            return False
        return self._number == other._number and self._route == other._route

    def can_take_passengers(self, passengers: int) -> bool:
        """
        Проверяет, может ли автобус взять указанное количество пассажиров
        
        Args:
            passengers: Количество пассажиров
            
        Returns:
            True если может, False если нет
        """
        return passengers <= self._capacity
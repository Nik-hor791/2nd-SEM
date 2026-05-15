from base import Bus

class ElectricBus(Bus):
    """Электроавтобус с аннотациями типов"""
    
    def __init__(self, number: str, capacity: int, route: str, year: int, 
                 battery_capacity: float, charging_time: float) -> None:
        """
        Конструктор электроавтобуса
        
        Args:
            number: Номер автобуса
            capacity: Вместимость
            route: Маршрут
            year: Год выпуска
            battery_capacity: Емкость батареи (кВт·ч)
            charging_time: Время зарядки (часы)
        """
        super().__init__(number, capacity, route, year)
        self._battery_capacity: float = battery_capacity
        self._charging_time: float = charging_time
    
    @property
    def battery_capacity(self) -> float:
        """Возвращает емкость батареи"""
        return self._battery_capacity
    
    @property
    def charging_time(self) -> float:
        """Возвращает время зарядки"""
        return self._charging_time
    
    def calculate_range(self, consumption_per_km: float = 0.8) -> float:
        """
        Рассчитывает максимальный пробег на одной зарядке
        
        Args:
            consumption_per_km: Расход энергии на км (кВт·ч/км)
            
        Returns:
            Пробег в километрах
        """
        if consumption_per_km <= 0:
            return 0.0
        return self._battery_capacity / consumption_per_km
    
    def __str__(self) -> str:
        """Строковое представление электроавтобуса"""
        return (f"ElectricBus {self._number} | Route: {self._route} | "
                f"Capacity: {self._capacity} | Year: {self._year} | "
                f"Battery: {self._battery_capacity}kWh")


class DieselBus(Bus):
    """Дизельный автобус с аннотациями типов"""
    
    def __init__(self, number: str, capacity: int, route: str, year: int,
                 fuel_tank_capacity: float, fuel_consumption: float) -> None:
        """
        Конструктор дизельного автобуса
        
        Args:
            number: Номер автобуса
            capacity: Вместимость
            route: Маршрут
            year: Год выпуска
            fuel_tank_capacity: Объем топливного бака (литры)
            fuel_consumption: Расход топлива (л/100 км)
        """
        super().__init__(number, capacity, route, year)
        self._fuel_tank_capacity: float = fuel_tank_capacity
        self._fuel_consumption: float = fuel_consumption
    
    @property
    def fuel_tank_capacity(self) -> float:
        """Возвращает объем топливного бака"""
        return self._fuel_tank_capacity
    
    @property
    def fuel_consumption(self) -> float:
        """Возвращает расход топлива"""
        return self._fuel_consumption
    
    def calculate_range(self) -> float:
        """
        Рассчитывает максимальный пробег на полном баке
        
        Returns:
            Пробег в километрах
        """
        if self._fuel_consumption <= 0:
            return 0.0
        return (self._fuel_tank_capacity / self._fuel_consumption) * 100
    
    def __str__(self) -> str:
        """Строковое представление дизельного автобуса"""
        return (f"DieselBus {self._number} | Route: {self._route} | "
                f"Capacity: {self._capacity} | Year: {self._year} | "
                f"Consumption: {self._fuel_consumption}L/100km")
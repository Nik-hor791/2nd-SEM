from base import Bus

class ElectricBus(Bus):
    
    def __init__(self, number: str, capacity: int, route: str, year: int, 
                 battery_capacity: float, charging_time: float):
        # Вызов конструктора базового класса через super()
        super().__init__(number, capacity, route, year)
        
        # Новые атрибуты
        self._battery_capacity = battery_capacity  # емкость батареи (кВт·ч)
        self._charging_time = charging_time  # время зарядки (часы)
    
    @property
    def battery_capacity(self):
        return self._battery_capacity
    
    @property
    def charging_time(self):
        return self._charging_time

    def calculate_range(self, consumption_per_km: float = 0.8):
        #Рассчитывает максимальный пробег на одной зарядке (км)
        if consumption_per_km <= 0:
            return 0
        return self._battery_capacity / consumption_per_km

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | Type: Electric | Battery: {self._battery_capacity} kWh | Charging: {self._charging_time}h"


class DieselBus(Bus):
    
    def __init__(self, number: str, capacity: int, route: str, year: int,
                 fuel_tank_capacity: float, fuel_consumption: float):
        # Вызов конструктора базового класса через super()
        super().__init__(number, capacity, route, year)
        
        # Новые атрибуты
        self._fuel_tank_capacity = fuel_tank_capacity  # объем топливного бака (литры)
        self._fuel_consumption = fuel_consumption  # расход топлива (л/100 км)
    
    @property
    def fuel_tank_capacity(self):
        return self._fuel_tank_capacity
    
    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    def calculate_range(self):
        if self._fuel_consumption <= 0:
            return 0
        return (self._fuel_tank_capacity / self._fuel_consumption) * 100
    
    # Переопределение метода __str__
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | Type: Diesel | Tank: {self._fuel_tank_capacity}L | Consumption: {self._fuel_consumption}L/100km"
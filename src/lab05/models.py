from base import Bus

class ElectricBus(Bus):
    def __init__(self, number: str, capacity: int, route: str, year: int, 
                 battery_capacity: float, charging_time: float):
        super().__init__(number, capacity, route, year)
        self._battery_capacity = battery_capacity
        self._charging_time = charging_time
    
    @property
    def battery_capacity(self):
        return self._battery_capacity
    
    @property
    def charging_time(self):
        return self._charging_time
    
    def calculate_range(self, consumption_per_km: float = 0.8):
        return self._battery_capacity / consumption_per_km
    
    def __str__(self):
        return f"ElectricBus {self._number} | Route: {self._route} | Capacity: {self._capacity} | Year: {self._year} | Battery: {self._battery_capacity}kWh"


class DieselBus(Bus):
    def __init__(self, number: str, capacity: int, route: str, year: int,
                 fuel_tank_capacity: float, fuel_consumption: float):
        super().__init__(number, capacity, route, year)
        self._fuel_tank_capacity = fuel_tank_capacity
        self._fuel_consumption = fuel_consumption
    
    @property
    def fuel_tank_capacity(self):
        return self._fuel_tank_capacity
    
    @property
    def fuel_consumption(self):
        return self._fuel_consumption
    
    def calculate_range(self):
        return (self._fuel_tank_capacity / self._fuel_consumption) * 100
    
    def __str__(self):
        return f"DieselBus {self._number} | Route: {self._route} | Capacity: {self._capacity} | Year: {self._year} | Consumption: {self._fuel_consumption}L/100km"
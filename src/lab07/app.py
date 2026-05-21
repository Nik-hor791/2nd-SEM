

from typing import Optional, List

from base import Bus
from models import ElectricBus, DieselBus
from container import TypedCollection
from exceptions import BusNotFoundError, InvalidBusNumberError
from storages import BusStorage

class BusApp:
    
    def __init__(self):
        self._collection: TypedCollection[Bus] = TypedCollection()
        self._storage = BusStorage()
    
    def start(self) -> None:
        try:
            self._collection = self._storage.load()
            print(f"Загружено {len(self._collection)} автобусов")
        except Exception as e:
            print(f"Предупреждение: {e}")
    
    def save(self) -> None:
        self._storage.save(self._collection)
        print("Данные сохранены")
    
    def add_bus(self, bus: Bus) -> None:
        # Проверка на дубликат по номеру
        if self.find_by_number(bus.number):
            raise InvalidBusNumberError(f"Автобус с номером {bus.number} уже существует")
        
        self._collection.add(bus)
    
    def add_regular_bus(self, number: str, capacity: int, route: str, year: int) -> Bus:
        bus = Bus(number, capacity, route, year)
        self.add_bus(bus)
        return bus
    
    def add_electric_bus(self, number: str, capacity: int, route: str, year: int,
                         battery_capacity: float, charging_time: float) -> ElectricBus:
        bus = ElectricBus(number, capacity, route, year, battery_capacity, charging_time)
        self.add_bus(bus)
        return bus
    
    def add_diesel_bus(self, number: str, capacity: int, route: str, year: int,
                       fuel_tank_capacity: float, fuel_consumption: float) -> DieselBus:
        bus = DieselBus(number, capacity, route, year, fuel_tank_capacity, fuel_consumption)
        self.add_bus(bus)
        return bus
    
    def remove_bus(self, number: str) -> Bus:
        bus = self.find_by_number(number)
        if bus is None:
            raise BusNotFoundError(f"Автобус с номером {number} не найден")
        
        self._collection.remove(bus)
        return bus
    
    def find_by_number(self, number: str) -> Optional[Bus]:
        for bus in self._collection.get_all():
            if bus.number == number:
                return bus
        return None
    
    def find_by_route(self, route: str) -> List[Bus]:
        results = []
        for bus in self._collection.get_all():
            if route.lower() in bus.route.lower():
                results.append(bus)
        return results
    
    def get_all_buses(self) -> List[Bus]:
        return self._collection.get_all()
    
    def get_count(self) -> int:
        return len(self._collection)
    
    def sort_by(self, key_func) -> None:
        self._collection.sort_by(key_func)
    
    def get_electric_buses(self) -> List[ElectricBus]:
        return [bus for bus in self._collection.get_all() if isinstance(bus, ElectricBus)]
    
    def get_diesel_buses(self) -> List[DieselBus]:
        return [bus for bus in self._collection.get_all() if isinstance(bus, DieselBus)]
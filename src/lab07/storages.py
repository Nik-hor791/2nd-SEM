

import json
import os
from typing import List, Dict, Any

from base import Bus
from models import ElectricBus, DieselBus
from container import TypedCollection


class BusStorage:
    
    def __init__(self, filename: str = "buses.json"):
        self.filename = filename
    
    def save(self, collection: TypedCollection[Bus]) -> None:
        try:
            data = []
            for bus in collection.get_all():
                bus_dict = self._bus_to_dict(bus)
                data.append(bus_dict)
            
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            raise SaveError(f"Ошибка сохранения: {e}")
    
    def load(self) -> TypedCollection[Bus]:
        collection = TypedCollection[Bus]()
        
        if not os.path.exists(self.filename):
            return collection
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for bus_dict in data:
                bus = self._dict_to_bus(bus_dict)
                if bus:
                    collection.add(bus)
        except Exception as e:
            raise LoadError(f"Ошибка загрузки: {e}")
        
        return collection
    
    def _bus_to_dict(self, bus: Bus) -> Dict[str, Any]:
        data = {
            'type': 'Bus',
            'number': bus.number,
            'capacity': bus.capacity,
            'route': bus.route,
            'year': bus.year
        }
        
        if isinstance(bus, ElectricBus):
            data['type'] = 'ElectricBus'
            data['battery_capacity'] = bus.battery_capacity
            data['charging_time'] = bus.charging_time
        elif isinstance(bus, DieselBus):
            data['type'] = 'DieselBus'
            data['fuel_tank_capacity'] = bus.fuel_tank_capacity
            data['fuel_consumption'] = bus.fuel_consumption
        
        return data
    
    def _dict_to_bus(self, data: Dict[str, Any]) -> Bus:
        bus_type = data.get('type', 'Bus')
        
        if bus_type == 'ElectricBus':
            return ElectricBus(
                number=data['number'],
                capacity=data['capacity'],
                route=data['route'],
                year=data['year'],
                battery_capacity=data['battery_capacity'],
                charging_time=data['charging_time']
            )
        elif bus_type == 'DieselBus':
            return DieselBus(
                number=data['number'],
                capacity=data['capacity'],
                route=data['route'],
                year=data['year'],
                fuel_tank_capacity=data['fuel_tank_capacity'],
                fuel_consumption=data['fuel_consumption']
            )
        else:
            return Bus(
                number=data['number'],
                capacity=data['capacity'],
                route=data['route'],
                year=data['year']
            )
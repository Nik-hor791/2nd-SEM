from base import Bus
from models import ElectricBus, DieselBus

def main():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ИЕРАРХИИ КЛАССОВ")
    print("=" * 60)
    
    # Создание объектов базового класса
    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ БАЗОВОГО КЛАССА:")
    bus1 = Bus("A123BC", 40, "Route 10", 2018)
    bus2 = Bus("B456DE", 30, "Route 15", 2020)
    print(bus1)
    print(bus2)
    
    # Создание объектов производного класса ElectricBus
    print("\n2. СОЗДАНИЕ ОБЪЕКТОВ ЭЛЕКТРОАВТОБУСА (ElectricBus):")
    electric_bus1 = ElectricBus("E001EV", 50, "Route 20", 2023, 300.0, 2.5)
    electric_bus2 = ElectricBus("E002EV", 40, "Route 25", 2022, 250.0, 2.0)
    print(electric_bus1)
    print(electric_bus2)
    
    # Создание объектов производного класса DieselBus
    print("\n3. СОЗДАНИЕ ОБЪЕКТОВ ДИЗЕЛЬНОГО АВТОБУСА (DieselBus):")
    diesel_bus1 = DieselBus("D001DS", 45, "Route 30", 2021, 200.0, 25.0)
    diesel_bus2 = DieselBus("D002DS", 35, "Route 35", 2020, 180.0, 22.0)
    print(diesel_bus1)
    print(diesel_bus2)
    
    # Демонстрация методов базового класса
    print("\n4. ИСПОЛЬЗОВАНИЕ МЕТОДОВ БАЗОВОГО КЛАССА:")
    passengers_count = 45
    print(f"Bus {electric_bus1.number}: Can take {passengers_count} passengers? {electric_bus1.can_take_passengers(passengers_count)}")
    print(f"Bus {diesel_bus1.number}: Can take {passengers_count} passengers? {diesel_bus1.can_take_passengers(passengers_count)}")
    
    # Сравнение автобусов
    print(f"\nBus {bus1.number} == Bus {bus2.number}? {bus1 == bus2}")
    print(f"Bus {electric_bus1.number} == Bus {electric_bus1.number}? {electric_bus1 == electric_bus1}")
    
    # Демонстрация новых методов производных классов
    print("\n5. ИСПОЛЬЗОВАНИЕ НОВЫХ МЕТОДОВ ПРОИЗВОДНЫХ КЛАССОВ:")
    
    # Метод ElectricBus
    range_electric = electric_bus1.calculate_range()
    print(f"ElectricBus {electric_bus1.number}: Range on full charge = {range_electric:.1f} km")
    range_electric2 = electric_bus2.calculate_range(0.9)
    print(f"ElectricBus {electric_bus2.number}: Range on full charge = {range_electric2:.1f} km")
    
    # Метод DieselBus
    range_diesel = diesel_bus1.calculate_range()
    print(f"DieselBus {diesel_bus1.number}: Range on full tank = {range_diesel:.1f} km")
    range_diesel2 = diesel_bus2.calculate_range()
    print(f"DieselBus {diesel_bus2.number}: Range on full tank = {range_diesel2:.1f} km")
    
    # Демонстрация доступа к атрибутам через property
    print("\n6. ДОСТУП К АТРИБУТАМ ЧЕРЕЗ PROPERTY:")
    print(f"ElectricBus {electric_bus1.number}: Battery = {electric_bus1.battery_capacity} kWh, Charging = {electric_bus1.charging_time}h")
    print(f"DieselBus {diesel_bus1.number}: Tank = {diesel_bus1.fuel_tank_capacity}L, Consumption = {diesel_bus1.fuel_consumption}L/100km")
    
    # Сравнение характеристик
    print("\n7. СРАВНЕНИЕ ХАРАКТЕРИСТИК:")
    print(f"Запас хода:")
    print(f"  {electric_bus1.number}: {electric_bus1.calculate_range():.1f} км (электрический)")
    print(f"  {diesel_bus1.number}: {diesel_bus1.calculate_range():.1f} км (дизельный)")
    
    # Проверка типов
    print("\n8. ПРОВЕРКА ТИПОВ ОБЪЕКТОВ:")
    print(f"electric_bus1 is Bus: {isinstance(electric_bus1, Bus)}")
    print(f"electric_bus1 is ElectricBus: {isinstance(electric_bus1, ElectricBus)}")
    print(f"diesel_bus1 is Bus: {isinstance(diesel_bus1, Bus)}")
    print(f"diesel_bus1 is DieselBus: {isinstance(diesel_bus1, DieselBus)}")
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)

if __name__ == "__main__":
    main()
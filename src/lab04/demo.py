from models import ElectricBus, DieselBus, SimpleBus
from interfaces import Printable, Comparable, Chargeable, Refuelable


def print_all(items: list[Printable]):
    print("\n--- Универсальная функция через интерфейс Printable ---")
    for item in items:
        print(f"  {item.to_string()}")
        print(f"  Short: {item.get_short_info()}\n")


def compare_objects(obj1: Comparable, obj2: Comparable):
    print("\n--- Универсальная функция через интерфейс Comparable ---")
    print(f"  Comparing: {obj1.get_short_info()} vs {obj2.get_short_info()}")
    result = obj1.compare_to(obj2)
    if result < 0:
        print(f"  Result: First is LESS\n")
    elif result == 0:
        print(f"  Result: Objects are EQUAL\n")
    else:
        print(f"  Result: First is GREATER\n")


def main():

    # Create objects
    electric1 = ElectricBus("E001", 50, "Route 10", 2023, 300.0, 2.5)
    electric2 = ElectricBus("E002", 45, "Route 12", 2024, 350.0, 3.0)
    diesel1 = DieselBus("D001", 55, "Route 20", 2022, 250.0, 28.0)
    diesel2 = DieselBus("D002", 48, "Route 22", 2023, 220.0, 24.0)
    simple1 = SimpleBus("S001", 40, "Route 30", 2020)

    # 1. Printable interface demo
    print_all([electric1, diesel1, simple1])

    # 2. Comparable interface demo
    compare_objects(electric1, electric2)  # Compare by battery capacity
    compare_objects(diesel1, diesel2)  # Compare by fuel consumption

    # 3. Chargeable interface demo (only ElectricBus)
    print("--- CHARGEABLE INTERFACE DEMO ---")
    print(f"  Before charge: {electric1.get_battery_percentage()}%")
    print(f"  {electric1.charge(1.0)}")
    print(f"  After charge: {electric1.get_battery_percentage()}%\n")

    # 4. Refuelable interface demo (only DieselBus)
    print("--- REFUELABLE INTERFACE DEMO ---")
    print(f"  Before refuel: {diesel1.get_fuel_level()}%")
    print(f"  {diesel1.refuel(50)}")
    print(f"  After refuel: {diesel1.get_fuel_level()}%\n")

    # 5. Multiple interfaces implementation check
    print("--- MULTIPLE INTERFACES IMPLEMENTATION ---")

    print(f"ElectricBus:")
    print(f"  - Printable: {isinstance(electric1, Printable)}")
    print(f"  - Comparable: {isinstance(electric1, Comparable)}")
    print(f"  - Chargeable: {isinstance(electric1, Chargeable)}")
    print(f"  - Refuelable: {isinstance(electric1, Refuelable)}\n")

    print(f"DieselBus:")
    print(f"  - Printable: {isinstance(diesel1, Printable)}")
    print(f"  - Comparable: {isinstance(diesel1, Comparable)}")
    print(f"  - Chargeable: {isinstance(diesel1, Chargeable)}")
    print(f"  - Refuelable: {isinstance(diesel1, Refuelable)}\n")

    print(f"SimpleBus:")
    print(f"  - Printable: {isinstance(simple1, Printable)}")
    print(f"  - Comparable: {isinstance(simple1, Comparable)}")
    print(f"  - Chargeable: {isinstance(simple1, Chargeable)}")
    print(f"  - Refuelable: {isinstance(simple1, Refuelable)}\n")

    # 6. Polymorphism through interface
    print("--- Полиморфизм через интерфейс ---")
    polymorphic_list: list[Printable] = [electric1, diesel1, simple1]
    print("All objects (different types) through Printable interface:")
    for obj in polymorphic_list:
        print(f"  {obj.get_short_info()}")




if __name__ == "__main__":
    main()
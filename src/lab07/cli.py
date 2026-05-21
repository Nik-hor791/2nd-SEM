
from typing import Optional
from base import Bus
from models import ElectricBus, DieselBus
from app import BusApp
from exceptions import (
    BusNotFoundError, 
    InvalidBusNumberError,
    InvalidCapacityError,
    InvalidYearError
)


class BusCLI:
    
    def __init__(self):
        self.app = BusApp()
    
    def run(self) -> None:
        self.app.start()
        
        while True:
            self._show_menu()
            choice = self._get_choice()
            
            if choice == 0:
                self._exit()
                break
            elif choice == 1:
                self._add_bus()
            elif choice == 2:
                self._show_all_buses()
            elif choice == 3:
                self._find_bus()
            elif choice == 4:
                self._remove_bus()
            elif choice == 5:
                self._show_stats()
            elif choice == 6:
                self._save_data()
            else:
                print("\n Ошибка: Неверный пункт меню. Попробуйте снова.")
    
    def _show_menu(self) -> None:
        print("\n" + "=" * 50)
        print("        УПРАВЛЕНИЕ АВТОБУСНЫМ ПАРКОМ")
        print("=" * 50)
        print(f"  Всего автобусов: {self.app.get_count()}")
        print("-" * 50)
        print("  1. Добавить автобус")
        print("  2. Показать все автобусы")
        print("  3. Найти автобус")
        print("  4. Удалить автобус")
        print("  5. Показать статистику")
        print("  6. Сохранить данные")
        print("  0. Выход")
        print("-" * 50)
    
    def _get_choice(self) -> int:
        while True:
            try:
                choice = int(input("\nВыберите пункт меню: "))
                return choice
            except ValueError:
                print(" Ошибка: Введите число от 0 до 6")
    
    def _get_number_input(self, prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print(" Ошибка: Поле не может быть пустым")
    
    def _get_int_input(self, prompt: str, min_val: int = None, max_val: int = None) -> int:
        while True:
            try:
                value = int(input(prompt))
                if min_val is not None and value < min_val:
                    print(f" Ошибка: Значение должно быть не меньше {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f" Ошибка: Значение должно быть не больше {max_val}")
                    continue
                return value
            except ValueError:
                print(" Ошибка: Введите целое число")
    
    def _get_float_input(self, prompt: str, min_val: float = None) -> float:
        while True:
            try:
                value = float(input(prompt))
                if min_val is not None and value < min_val:
                    print(f" Ошибка: Значение должно быть не меньше {min_val}")
                    continue
                return value
            except ValueError:
                print(" Ошибка: Введите число")
    
    def _get_bus_type(self) -> str:
        print("\nТипы автобусов:")
        print("  1. Обычный автобус")
        print("  2. Электрический автобус")
        print("  3. Дизельный автобус")
        
        while True:
            choice = self._get_int_input("Выберите тип (1-3): ", 1, 3)
            if choice == 1:
                return "regular"
            elif choice == 2:
                return "electric"
            elif choice == 3:
                return "diesel"
    
    def _add_bus(self) -> None:
        print("\n" + "-" * 40)
        print("ДОБАВЛЕНИЕ НОВОГО АВТОБУСА")
        print("-" * 40)
        
        bus_type = self._get_bus_type()
        
        try:
            number = self._get_number_input("Номер автобуса: ")
            capacity = self._get_int_input("Вместимость (мест): ", 1, 100)
            route = self._get_number_input("Маршрут: ")
            year = self._get_int_input("Год выпуска: ", 1900, 2025)
            
            if bus_type == "regular":
                bus = self.app.add_regular_bus(number, capacity, route, year)
                print(f"\n Обычный автобус {bus.number} успешно добавлен!")
                
            elif bus_type == "electric":
                battery = self._get_float_input("Емкость батареи (кВт·ч): ", 10)
                charging = self._get_float_input("Время зарядки (часы): ", 0.5)
                bus = self.app.add_electric_bus(number, capacity, route, year, battery, charging)
                print(f"\n Электрический автобус {bus.number} успешно добавлен!")
                
            elif bus_type == "diesel":
                tank = self._get_float_input("Объем топливного бака (л): ", 50)
                consumption = self._get_float_input("Расход топлива (л/100км): ", 5)
                bus = self.app.add_diesel_bus(number, capacity, route, year, tank, consumption)
                print(f"\n Дизельный автобус {bus.number} успешно добавлен!")
                
        except InvalidBusNumberError as e:
            print(f"\n Ошибка: {e}")
        except Exception as e:
            print(f"\n Ошибка: {e}")
    
    def _show_all_buses(self) -> None:
        buses = self.app.get_all_buses()
        
        print("\n" + "-" * 40)
        print("ВСЕ АВТОБУСЫ")
        print("-" * 40)
        
        if not buses:
            print("\n Коллекция пуста. Добавьте автобусы.")
            return
        
        for i, bus in enumerate(buses, 1):
            print(f"\n{i}. {bus}")
    
    def _find_bus(self) -> None:
        print("\n" + "-" * 40)
        print("ПОИСК АВТОБУСА")
        print("-" * 40)
        print("  1. По номеру")
        print("  2. По маршруту")
        
        choice = self._get_int_input("\nВыберите способ поиска (1-2): ", 1, 2)
        
        if choice == 1:
            number = self._get_number_input("Введите номер автобуса: ")
            bus = self.app.find_by_number(number)
            
            if bus:
                print(f"\n Найден автобус:\n{bus}")
            else:
                print(f"\n Автобус с номером {number} не найден")
        
        elif choice == 2:
            route = self._get_number_input("Введите маршрут (или часть): ")
            buses = self.app.find_by_route(route)
            
            if buses:
                print(f"\n Найдено автобусов: {len(buses)}")
                for bus in buses:
                    print(f"  • {bus.number} - {bus.route}")
            else:
                print(f"\n Автобусы на маршруте '{route}' не найдены")
    
    def _remove_bus(self) -> None:
        print("\n" + "-" * 40)
        print("УДАЛЕНИЕ АВТОБУСА")
        print("-" * 40)
        
        number = self._get_number_input("Введите номер автобуса для удаления: ")
        
        # Показываем информацию перед удалением
        bus = self.app.find_by_number(number)
        if bus:
            print(f"\nАвтобус для удаления:\n{bus}")
            confirm = input("\nПодтвердите удаление (да/нет): ").strip().lower()
            
            if confirm in ['да', 'yes', 'y', 'д']:
                try:
                    self.app.remove_bus(number)
                    print(f"\n Автобус {number} успешно удален!")
                except BusNotFoundError as e:
                    print(f"\n {e}")
            else:
                print("\n Удаление отменено")
        else:
            print(f"\n Автобус с номером {number} не найден")
    
    def _show_stats(self) -> None:
        print("\n" + "-" * 40)
        print("СТАТИСТИКА АВТОБУСНОГО ПАРКА")
        print("-" * 40)
        
        total = self.app.get_count()
        electric = len(self.app.get_electric_buses())
        diesel = len(self.app.get_diesel_buses())
        regular = total - electric - diesel
        
        print(f"\n Общая статистика:")
        print(f"  • Всего автобусов: {total}")
        print(f"  • Обычных: {regular}")
        print(f"  • Электрических: {electric}")
        print(f"  • Дизельных: {diesel}")
        
        if total > 0:
            avg_capacity = sum(b.capacity for b in self.app.get_all_buses()) / total
            oldest = min(b.year for b in self.app.get_all_buses())
            newest = max(b.year for b in self.app.get_all_buses())
            
            print(f"\n Характеристики:")
            print(f"  • Средняя вместимость: {avg_capacity:.1f} мест")
            print(f"  • Самый старый: {oldest} год")
            print(f"  • Самый новый: {newest} год")
    
    def _save_data(self) -> None:
        print("\n" + "-" * 40)
        print("СОХРАНЕНИЕ ДАННЫХ")
        print("-" * 40)
        
        try:
            self.app.save()
        except Exception as e:
            print(f"\n Ошибка сохранения: {e}")
    
    def _exit(self) -> None:
        print("\n" + "=" * 50)
        print("  Данные будут сохранены...")
        print("=" * 50)
        self.app.save()


def main():
    cli = BusCLI()
    cli.run()


if __name__ == "__main__":
    main()
from model import Bus


class BusFleet:

    def __init__(self):
        self._items = []

    def add(self, bus: Bus) -> None:

        if not isinstance(bus, Bus):
            raise TypeError(f"Можно добавлять только объекты Bus. Получен: {type(bus).__name__}")
        self._items.append(bus)
        print(f"Автобус {bus.number} добавлен в коллекцию")

    def remove(self, bus: Bus) -> bool:

        if not isinstance(bus, Bus):
            raise TypeError(f"Можно удалять только объекты Bus. Получен: {type(bus).__name__}")

        if bus in self._items:
            self._items.remove(bus)
            print(f"Автобус {bus.number} удалён из коллекции")
            return True
        else:
            print(f"⚠Автобус {bus.number} не найден в коллекции")
            return False

    def get_all(self) -> list:

        return self._items.copy()

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        if not self._items:
            return "BusFleet: пустая коллекция"

        result = f"BusFleet (всего {len(self._items)} автобусов):\n"
        for i, bus in enumerate(self._items, 1):
            result += f"  {i}. {bus}\n"
        return result

    def clear(self) -> None:
        count = len(self._items)
        self._items.clear()
        print(f"🗑️ Коллекция очищена. Удалено {count} автобусов.")
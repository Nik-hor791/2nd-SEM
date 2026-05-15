# Лабораторная работа №5 - Функции как аргументы. Стратегии и делегаты

## Цель работы
- Освоить передачу функций как аргументов в другие функции и методы
- Научиться применять встроенные функции высшего порядка: map, filter, sorted
- Понять концепцию паттерна «Стратегия» и реализовать его на Python
- Освоить lambda-выражения и их практическое применение
- Интегрировать функциональный стиль с объектно-ориентированным кодом из предыдущих ЛР

## Структура проекта

    lab05/
    ├── base.py # Базовый класс Bus из ЛР-1
    ├── models.py # Классы ElectricBus и DieselBus из ЛР-3
    ├── collection.py # Класс BusFleet (коллекция) с методами sort_by, filter_by, apply, map
    ├── strategies.py # Функции-стратегии для сортировки, фильтрации, преобразования
    ├── demo.py # Демонстрация всех возможностей
    └── README.md


## Класс BusFleet (коллекция)

### Методы коллекции:

| Метод | Описание |
|-------|----------|
| `add(bus)` | Добавляет автобус в коллекцию |
| `sort_by(key_func)` | Сортирует коллекцию по функции-ключу (возвращает self) |
| `filter_by(predicate)` | Фильтрует коллекцию по предикату (возвращает self) |
| `apply(func)` | Применяет функцию к каждому элементу (возвращает self) |
| `map(transform)` | Преобразует коллекцию в список результатов |
| `get_all()` | Возвращает копию списка автобусов |

## Стратегии сортировки (strategies.py)

| Функция | Описание |
|---------|----------|
| `by_number(bus)` | По номеру автобуса |
| `by_capacity(bus)` | По вместимости |
| `by_year(bus)` | По году выпуска |
| `by_route(bus)` | По маршруту |
| `by_battery_capacity(bus)` | По емкости батареи (ElectricBus) |
| `by_fuel_efficiency(bus)` | По расходу топлива (DieselBus) |
| `by_combined(bus)` | По комбинации (год, вместимость, номер) |

## Функции-фильтры

| Функция | Описание |
|---------|----------|
| `is_electric(bus)` | Только электрические автобусы |
| `is_diesel(bus)` | Только дизельные автобусы |
| `is_modern(bus)` | Автобусы после 2020 года |
| `has_high_capacity(bus)` | Вместимость > 45 |
| `by_min_year(year)` | **Фабрика**: автобусы не старше года |
| `by_max_capacity(capacity)` | **Фабрика**: автобусы с вместимостью ≤ capacity |
| `by_route_contains(substring)` | **Фабрика**: маршрут содержит подстроку |

## Функции преобразования (для map)

| Функция | Описание |
|---------|----------|
| `to_short_string(bus)` | Преобразует в короткую строку |
| `to_dict(bus)` | Преобразует в словарь |
| `to_number(bus)` | Извлекает номер |
| `to_year(bus)` | Извлекает год |

### 1. Сортировка разными стратегиями

```python

# Через метод коллекции
fleet.sort_by(by_capacity)

# Через встроенную функцию sorted
sorted_buses = sorted(fleet.get_all(), key=by_year)

# Через lambda
sorted_buses = sorted(fleet.get_all(), key=lambda b: b.capacity)

```

### 2. Фильтрация

```python

# Через метод коллекции
fleet.filter_by(is_electric)

# Через встроенную функцию filter
electric = list(filter(is_electric, fleet.get_all()))

# Через lambda
modern = list(filter(lambda b: b.year > 2020, fleet.get_all()))

```

### 3. Преобразование через map

```python

# Получить все номера
numbers = fleet.map(to_number)

# Получить все годы через lambda
years = fleet.map(lambda b: b.year)

# Преобразовать в строки
strings = fleet.map(to_short_string)

```

### 4. Фабрика функций

```python

# Создаем фильтр для автобусов после 2022 года
filter_2022 = by_min_year(2022)
recent = [bus for bus in fleet.get_all() if filter_2022(bus)]

```

### Демонстрация Demo.py:

![alt text](<../../images/lab05/Снимок экрана (41).png>)
![alt text](<../../images/lab05/Снимок экрана (42).png>)
![alt text](<../../images/lab05/Снимок экрана (43).png>)
![alt text](<../../images/lab05/Снимок экрана (44).png>)
![alt text](<../../images/lab05/Снимок экрана (45).png>)
![alt text](<../../images/lab05/Снимок экрана (46).png>)
![alt text](<../../images/lab05/Снимок экрана (47).png>)
![alt text](<../../images/lab05/Снимок экрана (48).png>)



















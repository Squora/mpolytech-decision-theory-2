# Определяем класс для представления предмета
class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    # Функция для вычисления отношения ценности к весу
    def value_to_weight_ratio(self):
        return self.weight / self.value

def knapsack_greedy(items, max_weight):
    # Сортируем предметы по отношению ценности к весу
    items_sorted = sorted(items, key=lambda x: x.value_to_weight_ratio(), reverse=True)

    total_weight = 0
    total_value = 0
    chosen_items = []

    for item in items_sorted:
        if total_weight + item.weight <= max_weight:
            chosen_items.append(item)
            total_weight += item.weight
            total_value += item.value

    return items_sorted, chosen_items, total_weight, total_value

# Пример использования программы
if __name__ == "__main__":
    # Определяем предметы (название, вес, ценность)
    items = [
        Item("Предмет 1", 100, 120),
        Item("Предмет 2", 200, 180),
        Item("Предмет 3", 300, 240),
        Item("Предмет 4", 400, 350),
        Item("Предмет 5", 500, 450),
        Item("Предмет 6", 100, 90),
        Item("Предмет 7", 150, 150),
        Item("Предмет 8", 250, 200),
        Item("Предмет 9", 300, 250),
        Item("Предмет 10", 350, 300)
    ]

    # Максимальный допустимый вес рюкзака
    max_weight = 750

    # Выводим все предметы с их характеристиками
    print("Все предметы:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item.name} - Вес: {item.weight}, Ценность: {item.value}")

    # Применяем жадный алгоритм для упаковывания рюкзака
    items_sorted, chosen_items, total_weight, total_value = knapsack_greedy(items, max_weight)

    # Выводим упорядоченные значения pi/wi
    print("\nОтношение ценности к весу (pi/wi) для всех предметов:")
    for i, item in enumerate(items_sorted, 1):
        print(f"{i}. {item.name} - pi/wi: {item.value_to_weight_ratio():.2f}")

    # Выводим список предметов, которые берутся
    print("\nВыбранные предметы:")
    for item in chosen_items:
        print(f"{item.name} - вес: {item.weight}, ценность: {item.value}")

    print(f"\nОбщий вес: {total_weight}")
    print(f"Общая ценность: {total_value}")
    input()

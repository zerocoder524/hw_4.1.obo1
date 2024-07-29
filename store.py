class Store:
    """Класс для представления магазина."""

    def __init__(self, name, address):
        """Инициализирует магазин.

        Args:
            name (str): Название магазина.
            address (str): Адрес магазина.
        """
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент.

        Args:
            item_name (str): Название товара.
            price (float): Цена товара.
        """
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента.

        Args:
            item_name (str): Название товара.
        """
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию.

        Args:
            item_name (str): Название товара.

        Returns:
            float: Цена товара, если он есть в ассортименте; None, если товара нет.
        """
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара.

        Args:
            item_name (str): Название товара.
            new_price (float): Новая цена.
        """
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")


# Создание магазинов
store1 = Store("Супермаркет", "ул. Ленина 100")
store2 = Store("Продуктовый магазин", "ул. Октябрьская 50")
store3 = Store("Магазин электроники", "ул. Пушкина 20")

# Добавление товаров
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store1.add_item("Молоко", 1.2)

store2.add_item("Хлеб", 1.0)
store2.add_item("Сыр", 2.5)

store3.add_item("Телефон", 1000)
store3.add_item("Ноутбук", 2000)

# Тестирование методов
print(f"nМагазин: {store1.name}")
print(f"Адрес: {store1.address}")

print(f"nТовары в магазине: {store1.items}")

print("nДобавление товара 'Груши' за 0.6")
store1.add_item("Груши", 0.6)
print(f"Товары в магазине: {store1.items}")

print("nПолучение цены 'Яблок':", store1.get_price("Яблоки"))
print("Получение цены 'Груш':", store1.get_price("Груши"))
print("Получение цены 'Хлеб':", store1.get_price("Хлеб"))

print("nОбновление цены 'Яблок' на 0.7")
store1.update_price("Яблоки", 0.7)
print(f"Товары в магазине: {store1.items}")

print("nУдаление товара 'Бананы'")
store1.remove_item("Бананы")
print(f"Товары в магазине: {store1.items}")

print("nПопытка удалить товар, которого нет: 'Апельсины'")
store1.remove_item("Апельсины")

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name} - {self.price} so'm"


class Order:
    def __init__(self):
        self.items = []

    def add_food(self, food):
        self.items.append(food)
        print(f"{food.name} qo'shildi.")

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_order(self):
        print("\nBuyurtma:")
        for item in self.items:
            print(item.get_info())

        print("Jami:", self.total_price())


class Restaurant:
    def __init__(self):
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def show_menu(self):
        print("\nMenu:")
        for food in self.menu:
            print(food.get_info())


def run_restaurant():
    res = Restaurant()
    order = Order()

    f1 = Food("Osh", 25000)
    f2 = Food("Somsa", 8000)
    f3 = Food("Choy", 3000)

    res.add_food(f1)
    res.add_food(f2)
    res.add_food(f3)

    res.show_menu()

    order.add_food(f1)
    order.add_food(f2)
    order.show_order()


run_restaurant()

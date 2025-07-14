from collections import defaultdict
from datetime import datetime, timedelta
from operator import attrgetter
import json
# from core.json_file_manager import *

class Order:
    def __init__(self, user, order_time):
        self.user = user
        self.order_time = order_time
        self.created =  datetime.now()

    def __str__(self):
        return f"{self.user.username} - {self.order_time.strftime('%Y-%m-%d %H:%M')}"


class User:
    def __init__(self, username):
        self.username = username
        self.orders = []
        # self.json_manager = JsonManager(filename="orders")


    def order(self, order_time, system):
        if system.add_order(self, order_time):
            order = {
                "name": self.username,
                "order_time": order_time,
            }
            with open('orders.json', 'w') as file:
                json.dump(data, file, indent=4)
                print(f"{self.username}, zakaz soat {order_time}da qabul qilindi")
        else:
            print(f"uzr {self.username}, bo'sh joy yo'q")

    def view_today_orders(self):
        today = datetime.now().date()

        for order in self.orders:
            if order.order_time.date() == today:
                print(f" - {order}")

    def view_all(self):
        for order in self.orders:
            print(f"- {order}")

class Admin(User):
    def show_all(self, system):
        for order in system.get_all_orders():
            print(f"-{order}")

    def delete(self, order, system):
        if order.remove_order(order):
            print(f"Zakaz o'chirildi: {order}")
        else:
            print("Zakaz topilmadi.")

class System:
    def __init__(self, max_orders):
        self.orders_per_hour = defaultdict(list)
        self.max_orders = max_orders


    def add_order(self, user, ordered_time):
        hour = ordered_time.replace(second=0, microsecond=0)

        for order in self.orders_per_hour[hour]:
            if order.user == user:
                return False

        if len(self.orders_per_hour[hour]) < self.max_orders:
            order = Order(user, ordered_time)
            self.orders_per_hour[hour].append(order)
            user.orders.append(order)
            return True
        else:
            return False

    def get_all_orders(self):
        all_orders = []
        for order_list in self.orders_per_hour.values():
            all_orders.extend(order_list)
            return sorted(all_orders, key=attrgetter('order_time'))

    def remove_order(self, order_to_remove):
        hour = order_to_remove.order_time.replace(minute=0, second=0, microsecond=0)
        if order_to_remove in self.orders_per_hour[hour]:
            self.orders_per_hour[hour].remove(order_to_remove)
            order_to_remove.user.orders.remove(order_to_remove)
            return True
        return False

system = System(max_orders=2)


# Foydalanuvchilar
user1 = User("Ali")
user2 = User("Vali")
admin = Admin("kimdir")


# # Zakaz vaqtlarini belgilash
time1 = datetime.now().replace(second=0, microsecond=0) + timedelta(hours=1)

# Foydalanuvchilar zakaz qilishmoqda
user1.order(time1, system)
# user2.order(time1, system)
# user1.order(time1, system)
# user1_order = user1.orders[0]
# print(user1_order)
# user1.view_today_orders()
# user1.view_all()
# admin.show_all(system)
# admin.delete(system, user1_order)

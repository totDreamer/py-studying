from datetime import datetime


class LoggerMixin:
    def log(self, lvl_log, text):
        print(
            f"[{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] - {lvl_log} - {self.__class__.__name__}: {text}"
        )


class Database(LoggerMixin):
    def connect(self):
        self.log("INFO", "Выполнено подключение к базе данных.")

    def disconnect(self):
        self.log("INFO", "Подключение к базе данных закрыто.")


db = Database()
db.connect()
db.disconnect()
print()


class Order(LoggerMixin):
    def __init__(self, order_id):
        self.order_id = order_id

    def create_order(self):
        self.log("INFO", f"Заказ № {self.order_id} создан.")

    def cancel_order(self):
        self.log("WARNING", f"Заказ № {self.order_id} отменен.")


order1 = Order(9876287)
order1.create_order()

order2 = Order(4778616)
order2.create_order()
order2.cancel_order()

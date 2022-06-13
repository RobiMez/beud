import imp
from order import Order


class User:
    def __init__(self, phone, name, location, orders):
        self.phone: phone
        self.name: name
        self.telegram_id = None

        self.live_orders = []
        self.order_history = []

        self.is_banned: False
        self.is_vip: False


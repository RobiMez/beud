

class User:
    def __init__(self,  telegram_id, telegram_identifier , phone=0,):
        self.phone: 'phone'
        self.name: telegram_identifier
        self.telegram_id = telegram_id
        self.role = None
        self.live_orders = []
        self.order_history = []

        self.is_banned: False
        self.is_vip: False


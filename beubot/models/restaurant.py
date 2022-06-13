
class Restaurant:
    def __init__(self, phone, location):
        self.phone = phone
        self.location = location
        self.is_open = False
        self.working_hours = []
        self.menu = [] # takes meal objects 
        self.orders_queue = [] # takes order objects


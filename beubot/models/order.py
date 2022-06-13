
class Order:
    def __init__(self, issuer, issued_for, meals):
        self.order_id = None
        # [user , restaurant]
        self.issuer = issuer
        self.issued_for = issued_for

        self.state = "init"

        self.meals = meals

        self.is_paid = False
        self.gross_price = self.calculate_price()

    def calculate_price(self):
        price = 0
        for meal in self.meals:
            price += meal.price
        return price

    def add_meal(self, meal):
        self.meals.append(meal)

    def remove_meal(self, meal):
        self.meals.remove(meal)

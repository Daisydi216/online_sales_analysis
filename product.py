class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
    
    def display_info(self):
        return f"Name: {self._name}, Price: {self._price}, Quantity: {self._quantity}"
    
    def update_quantity(self, amount):
        try:
            self._quantity += amount
        except TypeError:
            print("Invalid Quantity type.")
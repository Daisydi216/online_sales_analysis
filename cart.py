from product import Product
class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        if isinstance(product, Product):
            self.cart_items.append(product)

    def total_cart_value(self):
        total = sum(item._price * item._quantity for item in self.cart_items)
        print(f"Total basket value: {total}")

    def display_cart(self):
        for item in self.cart_items:
            print(item.display_info())
from product import Product

class ProductManager:
    def __init__(self):
        self._products = []
        
    def add_product(self, product):
        if isinstance(product, Product):
            self._products.append(product)
        else:
            print("Invalid product.")
            
    def view_all_products(self):
        for product in self._products:
            print(product.display_info())
            
    def total_value(self):
        total = sum(p._price * p._quantity for p in self._products)
        print(f"Total Inventory Value: {total}")
    
    def remove_product_by_name(self, name):
        self._products = [p for p in self._products if p._name != name]
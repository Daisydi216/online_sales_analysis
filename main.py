from product_manager import ProductManager
from product import Product
from cart import Cart
import random

product_manager = ProductManager()
cart = Cart()

products = [
    Product("Laptop", 2.150, 15),
    Product("Samsung Galaxy s23 Ultra", 1.502, 15),
    Product("Monitor", 400, 14)
]

for product in products:
     product_manager.add_product(product)
     


try:
    random_products = random.sample(products, 3)
    for product in random_products:
        cart.add_to_cart(product)
except ValueError:
    print(f"Not enough products to choose from.")
    
cart.display_cart()
cart.total_cart_value()  

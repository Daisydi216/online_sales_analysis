from product_manager import ProductManager
from product import Product
from cart import Cart
import random

product_manager = ProductManager()
cart = Cart()

products = [
    Product("Laptop Asus TUF", 2.150, 25),
    Product("Samsung Galaxy s25 Ultra", 1.502, 5),
    Product("LG TV", 400, 4)
]

for product in products:
     product_manager.add_product(product)
     
product_manager.view_all_products()
product_manager.total_value()

try:
    random_products = random.sample(products, 3)
    for product in random_products:
        cart.add_to_cart(product)
except ValueError:
    print(f"Not enough products to choose from.")
    
cart.display_cart()
cart.total_cart_value()  
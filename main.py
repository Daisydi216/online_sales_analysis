from product_manager import ProductManager
from product import Product


product_manager = ProductManager()


products = [
    Product("Laptop", 2.150, 15),
    Product("Samsung Galaxy s23 Ultra", 1.502, 15),
    Product("Monitor", 400, 14)
]

for product in products:
     product_manager.add_product(product)
     

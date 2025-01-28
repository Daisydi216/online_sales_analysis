from product_manager import ProductManager
from product import Product


product_manager = ProductManager()


products = [
    Product("Laptop Asus TUF", 2.150, 25),
    Product("Samsung Galaxy s25 Ultra", 1.502, 5),
    Product("LG TV", 400, 4)
]

for product in products:
     product_manager.add_product(product)
     
product_manager.view_all_products()
product_manager.total_value()
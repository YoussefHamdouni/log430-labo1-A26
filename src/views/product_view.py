"""
Product view
SPDX - License - Identifier: LGPL - 3.0 - or -later
"""
from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def display_list():
        """ Show the list of products """
        controller = ProductController()
        ProductView.show_products(controller.list_products())
        controller.shutdown()

    @staticmethod
    def add():
        """ Fill the form and add a new product """
        name, brand, price = ProductView.get_inputs()
        controller = ProductController()
        controller.create_product(Product(None, name, brand, price))
        controller.shutdown()

    @staticmethod
    def delete():
        """ Delete product with given ID (bonus) """
        product_id = input("ID de l'item à supprimer : ").strip()
        controller = ProductController()
        controller.delete_product(product_id)
        controller.shutdown()

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{p.id}: {p.name} - {p.brand} ({p.price} $)" for p in products))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add a new product """
        name = input("Nom de l'item : ").strip()
        brand = input("Marque : ").strip()
        price = float(input("Prix : ").strip())
        return name, brand, price
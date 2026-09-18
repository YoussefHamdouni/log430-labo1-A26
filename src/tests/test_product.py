from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    dao.insert(Product(None, 'Test 1', 'BrandA', 9.99))
    dao.insert(Product(None, 'Test 2', 'BrandB', 19.99))
    dao.insert(Product(None, 'Test 3', 'BrandC', 29.99))

    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'Clavier', 'Logitech', 49.99)
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'Souris', 'Genius', 12.50)
    assigned_id = dao.insert(product)

    corrected_name = 'Souris Pro'
    product.id = assigned_id
    product.name = corrected_name
    dao.update(product)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert corrected_name in names

    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, 'Écran', 'Dell', 199.99)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)
    new_dao = ProductDAO()
    product_list = new_dao.select_all()
    ids = [p.id for p in product_list]
    assert assigned_id not in ids
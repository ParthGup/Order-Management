from my_app.models import *
from .db_product import *
class db_order_product :

    def __init__(self):
        pass

    def create_order_product(self, order_obj, product_info):
        
        for products in product_info :
            
            product_obj = db_product()
            product = product_obj.get_product_by_id(products["product_id"])
            a = Order_Product(
            order_id = order_obj,
            product_id = product,
            qty = products["quantity"]
            )
            a.save()
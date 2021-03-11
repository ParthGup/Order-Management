from my_app.models import *
from my_app.DB_Layer.db_store import *
from my_app.DB_Layer.db_customer import *
from my_app.DB_Layer.db_order_product import *

class db_order :

    def __init__(self):
        pass

    def place_order(self, customer_id, store_id, total, product_info):

        customer_obj = db_customer()
        store_obj = db_store()

        customer = customer_obj.get_customer_by_id(customer_id)
        store = store_obj.verify_and_return_store_id(store_id, product_info)

        a = Order(
         store_id = store,
         customer_id = customer,
         total = total
        )
        a.save(force_insert=True)

        order_product_object = db_order_product()
        order_product_object.create_order_product(a,product_info)

        result = {
            "order_id" : str(a.id),
            "customer_id" : str(customer.id),
            "customer_name" : str(customer.first_name + " " +customer.last_name),
            "store_id" : str(store.id),
            "store_name" : str(store.name),
            "product_info" :  product_info,
            "total" :  str(a.total),
            }

        return result

        


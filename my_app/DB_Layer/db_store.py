from my_app.models import *
from .db_store_products import *
class db_store :

    def __init__(self):
        pass

    def verify_and_return_store_id(self, store_id, product_info):
        
        storeById = Store.objects.get(id = store_id)

        store_product_object = db_store_product()
        store_product_object.check_if_product_available(store_id, product_info)

        return storeById

from my_app.Service_Layer.Members.product_members import *
from my_app.DB_Layer.db_product import *

class Service_Product_Functions:

    def __init__(self):
        pass

    def get_price(self, id_to_find):

        obj = Service_Product_member()
        obj.id = id_to_find
        
        data_obj = db_product()
        obj = data_obj.get_price(obj.id)
        
        return obj
    
    def get_product_by_id(self, id_to_find):

        obj = Service_Product_member()
        obj.id = id_to_find
        
        data_obj = db_product()
        obj = data_obj.get_product_by_id(obj.id)
        
        return obj






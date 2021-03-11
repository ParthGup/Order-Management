from my_app.Service_Layer.Members.order_members import *
from my_app.DB_Layer.db_order import *
from my_app.Service_Layer.Functions.product_functions import *
from my_app.Service_Layer.Functions.order_product_functions import *

class Service_Order_Functions:

    def __init__(self):
        pass

            
    def create_order(self,store_id,customer_id,product_info):


        total = 0

        obj = Service_Product_Functions()
        for d in product_info :
            total += (obj.get_price(d["product_id"]) * d["quantity"])
        
        my_obj = Service_Order_member()

        my_obj.customer_id = customer_id
        my_obj.store_id = store_id
        my_obj.total = total


        data_obj = db_order()
        ans = data_obj.place_order(my_obj.customer_id, my_obj.store_id, my_obj.total,product_info)


        return ans

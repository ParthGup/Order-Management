from my_app.models import *
class db_store_product :

    def __init__(self):
        pass

    def check_if_product_available(self, store_id, product_info):
        

        for products in product_info :

            print(products["product_id"])
            print(store_id)

            
            store_product = Store_Product.objects.get(store_id = store_id, product_id = products["product_id"])
            
            if products["quantity"] < 0 :
                raise Exception("Quantity entered for " + store_product.product_id.name + " is negative")

            if store_product.in_stock_qty < products["quantity"] :
                raise Exception("Order quantity for " + store_product.product_id.name +  " is greater than available quantity at store")
        
        for products in product_info :

            store_product = Store_Product.objects.get(store_id = store_id, product_id = products["product_id"])
            
            updated_qty =  store_product.in_stock_qty - products["quantity"]
            store_product.in_stock_qty = updated_qty

            store_product.save()
            
        
           

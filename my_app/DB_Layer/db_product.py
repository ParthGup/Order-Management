
from my_app.models import *

class db_product :

    def __init__(self):
        pass

    def get_price(self, sid):

        productById = Product.objects.get(id = sid)
        return productById.price
    
    def get_product_by_id(self, sid):

        productById = Product.objects.get(id = sid)
        return productById
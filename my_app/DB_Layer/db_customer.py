from my_app.models import *
class db_customer :

    def __init__(self):
        pass

    def get_customer_by_id(self, customer_id):
        
        customerById = Customer.objects.get(id = customer_id)
        return customerById

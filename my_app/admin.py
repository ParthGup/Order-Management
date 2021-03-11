from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Store)
admin.site.register(Store_Product)
admin.site.register(Order)
admin.site.register(Order_Product)
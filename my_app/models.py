from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=400, blank=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField((u"Created Time"), auto_now_add=True, blank=True)
    updated_date = models.DateTimeField((u"Updated Time"),auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    created_date = models.DateTimeField((u"Created Time"), auto_now_add=True, blank=True)
    updated_date = models.DateTimeField((u"Updated Time"),auto_now=True)

    def __str__(self):
        return self.first_name

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)
    created_date = models.DateTimeField((u"Created Time"), auto_now_add=True, blank=True)
    updated_date = models.DateTimeField((u"Updated Time"),auto_now=True)

    def __str__(self):
        return self.name

class Store_Product(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    in_stock_qty = models.IntegerField(default=0)
    created_date = models.DateTimeField((u"Created Time"), auto_now_add=True, blank=True)
    updated_date = models.DateTimeField((u"Updated Time"),auto_now=True)

    def __str__(self):
        return self.store_id.name

class Order(models.Model):

    STATUS = (
    ("Approved", "Approved"),
    ("Canceled", "Canceled"), 
    )

    id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey(Store,on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices = STATUS, default=STATUS[0])
    total = models.FloatField(default=0)
    created_date = models.DateTimeField((u"Created Time"), auto_now_add=True, blank=True)

    def __str__(self):
        return self.customer_id.first_name

class Order_Product(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return self.order_id.customer_id.first_name
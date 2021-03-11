from django.shortcuts import render
from django.http import HttpResponse
from my_app.Service_Layer.Functions.product_functions import *
from my_app.Service_Layer.Functions.order_functions import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request) :
    return HttpResponse("hello world")

def get_price(request, id):
    response = {"status": "error"}
    try:
        if request.method == "GET" :
            obj = Service_Product_Functions()
            product_object = obj.get_product_by_id(id)

            product = {}
            product["product_id"] = str(product_object.id)
            product["name"] = str(product_object.name)
            product["price"] = str(product_object.price)

            response["status"] = "success"
            response["result"] = (product)
            
            return JsonResponse(response)

    except Exception as e:
        response["error"] = str(e)
        return JsonResponse(response) 
        

@csrf_exempt
def place_order(request):
    response = {"status": "error"}
    try:
        if request.method == "POST":

            # Check_application header
            # {"store_id" : 2 , "customer_id" : 3, "product_info" : [{"product_id" : 1 , "quantity" :3},{"product_id" : 3, "quantity" :5}] }
            reqBody=json.loads(request.body.decode('utf-8'))

            store_id = reqBody['store_id']
            customer_id = reqBody['customer_id']
            product_info = reqBody['product_info']

            obj = Service_Order_Functions()
            ans = obj.create_order(store_id,customer_id,product_info)

            # total = obj.create_order(1,2,[{"product_id" : 1 , "quantity" :1},{"product_id" : 2, "quantity" :1}])
            
            response["status"] = "success"
            response["result"] = ans
            return JsonResponse(response)
            
    except Exception as e:
        response["error"] = str(e)
        return JsonResponse(response) 



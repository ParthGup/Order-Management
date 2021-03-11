# Order Management Service

OMS is an service that helps people getting price for a product and placing an order for products at a particular store.

## APIs

1. Fetch price quote for a particular product

```
url: GET /products/get_price/p_id

sample response: 
status: 200
body: 
{
    "status": "success",
    "result": {
        "product_id": "1",
        "name": "Iphone 11",
        "price": "1000.0"
    }
}
```

2. Create Order for products at a particular store
```
url: POST /place_order
sample request body: 
{ 
      "store_id" : 2 ,
      "customer_id" : 2, 
      "product_info" : [{"product_id" : 1, "quantity" :1}] 
}

sample response:
status: 200
{
    "status": "success",
    "result": {
        "order_id": "16",
        "customer_id": "2",
        "customer_name": "Sid Roy",
        "store_id": "2",
        "store_name": "Chroma South Delhi",
        "product_info": [
            {
                "product_id": 1,
                "quantity": 1
            }
        ],
        "total": "1000.0"
    }
}
```

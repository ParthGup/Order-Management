from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('products/get_price/<int:id>/', views.get_price, name='get_price'),
    path('place_order/', views.place_order, name='place_order')

]
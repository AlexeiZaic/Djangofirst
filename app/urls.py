from django.urls import path

from .views import landingview, productlistview, supplierlistview, addsupplier, addproducts

urlpatterns = [
    path('', landingview),


    path('products/', productlistview),
    path('add-product/', addproducts),

    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
]

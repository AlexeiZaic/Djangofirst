from django.urls import path

from .views import landingview, productlistview, supplierlistview

urlpatterns = [
    path('',landingview),

    path('product/',productlistview),

    path('supplier/',supplierlistview)


    ]
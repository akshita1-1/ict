from fries_app.views import home , menu , checkout
from django.urls import path
urlpatterns=[
    path('',home,name='home'),
    path('menu',menu ,name='menu'),
    path('checkout',checkout ,name='checkout'),
    
]

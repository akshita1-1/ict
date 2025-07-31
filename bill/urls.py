from django.urls import path
from bill import views

urlpatterns = [
    path('', views.home, name='home'),
]

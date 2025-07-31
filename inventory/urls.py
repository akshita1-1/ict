from django.urls import path
from inventory.views import inventory, edit, delete

urlpatterns = [
    path('', inventory, name='inventory'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
]

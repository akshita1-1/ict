from todo_list.views import home, edit, delete
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
]

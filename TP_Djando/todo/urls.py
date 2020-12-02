from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('addnew',views.addnew),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]

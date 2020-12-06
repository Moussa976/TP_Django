from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<id>',views.delete, name="delete"),
    path('is_done/<id>',views.is_done, name="is_done"),
    path('not_done/<id>',views.not_done, name="not_done"),
    path('edit/<id>',views.edit, name="edit"),

]

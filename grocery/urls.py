from django.urls import path
from . import views


urlpatterns=[
    path("",views.grocery,name="grocery"),
    path("grocery/add",views.grocery_add,name="grocery_add"),
    path("grocery/<int:pk>/edit/",views.grocery_edit,name="grocery_edit"),
    path("grocery/<int:pk>/delete/",views.grocery_delete,name="grocery_delete"),
]
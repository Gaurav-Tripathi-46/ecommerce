from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("electronics/",views.electronics,name="electronics"),
    path("electronics/add",views.electronics_add,name="electronics_add"),
    path("electronics/<int:pk>/edit/",views.electronics_edit,name="electronics_edit"),
    path("electronics/<int:pk>/delete/",views.electronics_delete,name="electronics_delete"),
]
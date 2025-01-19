from django.urls import path
from . import views

urlpatterns=[
    path('',views.fashion,name="fashion"),
    path("fashion/add",views.fashion_add,name="fashion_add"),
    path("fashion/<int:pk>/edit/",views.fashion_edit,name="fashion_edit"),
    path("fashion/<int:pk>/delete/",views.fashion_delete,name="fashion_delete"),
]
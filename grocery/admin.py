from django.contrib import admin
from .models import Grocery

# Register your models here.
@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display=("id","item","price","quantity")


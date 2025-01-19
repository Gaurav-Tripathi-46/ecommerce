from django.contrib import admin
from .models import Fashion

# Register your models here.
@admin.register(Fashion)
class FashionAdmin(admin.ModelAdmin):
    list_display=("name","price","brand")

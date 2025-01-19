from django.contrib import admin
from .models import Electronics

@admin.register(Electronics)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display=("Sid","name","price","desc")

# Register your models here.

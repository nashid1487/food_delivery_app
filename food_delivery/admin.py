from django.contrib import admin
from .models import Food

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'category', 'price',)
    list_editable = ('available',)


admin.site.register(Food, FoodAdmin)
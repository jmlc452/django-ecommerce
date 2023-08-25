from django.contrib import admin
from .models import producto,categoria_producto

# Register your models here.

class productoadmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    
class categoria_productoadmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(producto)
admin.site.register(categoria_producto)
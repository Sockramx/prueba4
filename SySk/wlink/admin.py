from django.contrib import admin

from .models import Link, Categoria

# Register your models here.

class AdminLink(admin.ModelAdmin):
    list_display = ["web","link","categoria"]
    list_editable = ["link"]

class AdminCategoria(admin.ModelAdmin):
    list_display = ["categoria","descripcion"]
    
admin.site.register(Link, AdminLink)
admin.site.register(Categoria, AdminCategoria)

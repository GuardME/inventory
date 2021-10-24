from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

# buat atur header table
class ProducAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category',)
    list_filter = ['category']

# ganti nama Header di django admin
admin.site.site_header = 'Rama Django Learning'

# Register your models here.
admin.site.register(Product, ProducAdmin)
admin.site.register(Order)
# untuk Unregis si Group dari django admin
# admin.site.unregister(Group)

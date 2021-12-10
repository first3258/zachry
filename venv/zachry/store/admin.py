from django.contrib import admin
from store.models import Category,Product, Cart, CartItem, Order, OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'total', 'token', 'created', 'updated', 'status']

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order', 'product', 'quantity', 'price', 'created', 'updated']


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
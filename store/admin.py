from django.contrib import admin

from store.models import Category, Product #, Cart, Order

admin.site.register(Category)
admin.site.register(Product)
#admin.site.register(Cart)
#admin.site.register(Order)
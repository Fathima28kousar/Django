from django.contrib import admin

# Register your models here.
from .models import Product,Order,Contact,OrderUpdate
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(OrderUpdate)    



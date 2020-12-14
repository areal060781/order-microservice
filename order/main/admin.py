from django.contrib import admin

from .models import Order
from .models import OrderItems
from .models import OrderCustomer

admin.autodiscover()

admin.site.register(Order)
admin.site.register(OrderCustomer)
admin.site.register(OrderItems)

# Register your models here.

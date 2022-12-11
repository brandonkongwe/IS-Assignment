from django.contrib import admin
from login.models import user_group, customer

# Register your models here.
admin.site.register(customer)
admin.site.register(user_group)
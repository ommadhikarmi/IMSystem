from django.contrib import admin
from.models import Department,Resources,ResourceType,Purchase,Vendor
from.models import User
# Register your models here.
admin.site.register(Department)
admin.site.register(ResourceType)
admin.site.register(Resources)
admin.site.register(Vendor)
admin.site.register(Purchase)
admin.site.register(User)
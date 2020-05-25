from django.contrib import admin
from .models import Category,Images,Location

# Register your models here.
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Location)
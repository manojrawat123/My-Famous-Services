from django.contrib import admin
from services.models import MyService

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'description', 'meta_description', 'active' ]

admin.site.register(MyService, ServiceAdmin)

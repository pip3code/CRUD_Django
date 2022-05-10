from django.contrib import admin
from .models import DashboardCollection, DashboardPage

# Register your models here.
admin.site.register(DashboardCollection)
admin.site.register(DashboardPage)
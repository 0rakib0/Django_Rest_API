from django.contrib import admin
from .models import Studet
# Register your models here.

@admin.register(Studet)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
from django.contrib import admin
from django.urls import path
from api_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentcreate/', views.Create_Student)
]

from django.contrib import admin
from django.urls import path
from api_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.studen_api),
    path('stuapi/<id>/', views.studen_api)
]

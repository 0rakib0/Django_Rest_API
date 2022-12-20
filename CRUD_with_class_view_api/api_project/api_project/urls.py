from django.contrib import admin
from django.urls import path
from api_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.studen_api.as_view()),
    path('stuapi/<id>/', views.studen_api.as_view())
]

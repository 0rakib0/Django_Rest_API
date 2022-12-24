from django.contrib import admin
from django.urls import path
from api_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/', views.StudentView.as_view()),
    path('cr/', views.cr.as_view()),
    path('add/', views.StudentAdd.as_view()),
    path('view/<int:pk>/', views.StudentRet.as_view()),
    path('update/<int:pk>/', views.StudentUp.as_view()),
    path('delete/<int:pk>/', views.StudentDe.as_view()),
    path('ru/<int:pk>/', views.RU.as_view()),
    path('rd/<int:pk>/', views.RD.as_view()),
    path('rud/<int:pk>/', views.rud.as_view()),
]

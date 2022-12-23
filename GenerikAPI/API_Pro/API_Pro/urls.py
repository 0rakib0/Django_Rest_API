from django.contrib import admin
from django.urls import path
from api_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('creat/', views.Studet_view.as_view()),
    # path('', views.StudentList.as_view()),
    # path('create/', views.StudentCreate.as_view()),
    path('rud/<int:pk>/', views.Student_RUD.as_view()),
    # path('retrive/<int:pk>/', views.StudentRetrive.as_view()),
    # path('update/<int:pk>/', views.StudentUpdate.as_view()),
    # path('delete/<int:pk>/', views.StudentDalete.as_view()),
]

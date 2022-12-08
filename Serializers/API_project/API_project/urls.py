from django.contrib import admin
from django.urls import path
from API_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/<int:pk>/', views.Student_view),
    path('studentinfo/', views.Student_list)

]

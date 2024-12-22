from django.contrib import admin
from django.urls import path
from Chatbot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('get_response/', views.get_response, name='get_response'),
]


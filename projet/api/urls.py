from django.contrib import admin
from django.urls import path,include
from .views import TodoListApiView

urlpatterns = [
    path('', TodoListApiView.as_view()),
    
]

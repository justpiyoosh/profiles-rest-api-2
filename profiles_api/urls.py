from django.urls import path , include
from profiles_api import views
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('hello-view',views.HelloApiView.as_view()),
]
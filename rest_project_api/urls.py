from django.urls import path
from rest_project_api import views

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
]

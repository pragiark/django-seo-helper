from django.urls import path
from . import views

urlpatterns = [
    path('add-client/', views.AddClientView.as_view()),
    path('list-client/', views.ListClientView.as_view()),

 ]

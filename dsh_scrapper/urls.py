from django.urls import path
from . import views

urlpatterns = [
    path('add-client/', views.AddClientView.as_view(), name='add_client'),
    path('list-client/', views.ListClientView.as_view()),
 ]

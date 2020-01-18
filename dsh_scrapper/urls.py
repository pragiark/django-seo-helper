from django.urls import path
from . import views

urlpatterns = [
    path('add-client/', views.AddClientView.as_view(), name='add_client'),
    path('scrapp-list/', views.ListScrapeView.as_view(), name='scrapp_list'),
    path('', views.ListClientView.as_view(), name='list_client'),
 ]

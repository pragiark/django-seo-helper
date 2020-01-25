from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-client/', views.AddClientView.as_view(), name='add_client'),
    path('scrapp-list/', views.ListScrapeView.as_view(), name='scrapp_list'),
    path('', views.ListClientView.as_view(), name='list_client'),
]

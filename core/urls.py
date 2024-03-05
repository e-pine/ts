from django.urls import path
from .import views
from auth_user import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('controller/', views.controller, name='controller'),
    path('staff/', views.staff, name='staff'),
    path('repair/', views.repair, name="repair"),
    path('ticket_logs/', views.ticket_logs, name="ticket_logs"),
    # department
    path('hopps/', views.hopps, name="hopps"),
    path('hopps2/<int:event_id>/', views.hopps2, name='hopps2'),
    path('hopss_update/<int:pk>/', views.hopss_update, name='hopss_update'),

    path('nursing/', views.nursing, name="nursing"),
    path('medical/', views.medical, name="medical"),
    path('allied/', views.allied, name="allied"),
    path('finance/', views.finance, name="finance"),
    path('mcc/', views.mcc, name="mcc"),

    path('login/', auth_views.user_login, name='login'),
    path('logout/', auth_views.user_logout, name="logout"),

]
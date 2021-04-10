from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard,name='dashboard'),
    path('customer/<str:pk_test>/', views.customer,name='customer1'),
    path('dash_services/', views.dash_services,name='dash_services'),
    path('dash_staff/', views.dash_staff,name='dash_staff'),
    path('create_order/<str:pk>/', views.createOrder, name="createOrder"),
    path('update_order/<str:pk>/', views.updateOrder, name="updateOrder"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="deleteOrder"),
    path('user_dashboard/', views.userPage, name="user_dash"),
    path('handlerequst/', views.handlerequest, name='handlerequest'),
    path('account/', views.accountSettings, name='account'),


]
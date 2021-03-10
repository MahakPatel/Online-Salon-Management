from django.urls import path,include
from .import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from gallery import views as gallery_views
from contact import views as contact_views
from services import views as services_views
from about import views as about_views
urlpatterns =[

    path('login/', views.loginhandle, name='loginhandle'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logouthandle, name='logouthandle'),
    path('/service',include('services.urls')),
    path('login1/', views.login1, name='login1'),
    path('loginhandle/', views.loginhandle, name='loginhandle'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('myprofile/', views.updateprofile, name='myprofile'),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),

]

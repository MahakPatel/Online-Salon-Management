"""salon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1.5/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Staff import views
from gallery import views as gallery_views
from contact import views as contact_views
from services import views as services_views
from about import views as about_views
from home import views as home_views
from appoinment import views as appoinment_views
from dashboard import views as dashboard_views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls')),
    path('gallery/', include('gallery.urls')),
    path('services/', include('services.urls')),
    path('about/', include('about.urls')),
    path('/home/login', include('home.urls')),
    path('logout/', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('appoinment/', include('appoinment.urls')),

    path('new/', gallery_views.new),
    path('contact/', contact_views.contact),
    path('home/', home_views.home),
    path('service/', services_views.service),
    path('about/', about_views.about),
    path('loginhandle/', home_views.loginhandle),
    path('logouthandle/', home_views.logouthandle),
    path('appoinment/', appoinment_views.appoinment),
    path('appoinment/handlerequest/', appoinment_views.appoinment),
    path('dashboard/', dashboard_views.dashboard),
    path('customer/<str:pk_test>/', dashboard_views.customer),
    path('dash_services/', dashboard_views.dash_services),
    path('customer/', dashboard_views.customer),
    path('dash_staff/', dashboard_views.dash_staff),
    path('create_order/<str:pk>/', dashboard_views.createOrder),
    path('update_order/<str:pk>/', dashboard_views.updateOrder),
    path('delete_order/<str:pk>/', dashboard_views.deleteOrder),
    path('login1/', home_views.login),
    path('user_dash/', dashboard_views.userPage),
    path('myprofile/', home_views.updateprofile),
    path('dashboard/handlerequest/', dashboard_views.createOrder),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

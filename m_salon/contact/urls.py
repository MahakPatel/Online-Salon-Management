from django.urls import path,include
from django.contrib import admin
from . import views
from . import views
from gallery import views as gallery_views
from about import views as about_views
from services import views as services_views
from home import views as home_views

urlpatterns = [
       path('', views.contact ,name='contact'),



]


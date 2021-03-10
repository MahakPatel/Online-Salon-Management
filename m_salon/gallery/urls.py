from django.urls import path,include
from django.contrib import admin

from . import views
from about import views as about_views
from contact import views as contact_views
from services import views as services_views
from gallery import views as gallery_views
from home import views as home_views
urlpatterns = [
       path('', views.new ,name='new'),



]


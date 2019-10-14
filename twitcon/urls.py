from django.urls import path
from . import views


urlpatterns = [
    
   path('', views.index, name = 'twitcon-index'),

   path('upload', views.index, name = 'twitcon-upload')



]
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="news"),
   path('create_news', views.create, name="create_news"),
]
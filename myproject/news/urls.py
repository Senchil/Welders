from django.urls import path
from news import views

urlpatterns = [
   path('', views.index, name="news"),
   path('create/', views.create, name='create_news'),
   path('<int:article_id>/', views.detail, name='detail'),
]
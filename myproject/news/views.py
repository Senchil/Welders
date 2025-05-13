from django.shortcuts import render
from .models import Articles

def index(request):
   news = Articles.objects.order_by('date')
   return render(request, 'news/index.html', {'news': news})

def create(request):
   return render(request, 'news/create_news.html')

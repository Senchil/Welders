from django.shortcuts import render
from news.models import Articles

def index(request):
   articles = Articles.objects.order_by('-date')[:5]
   return render(request, 'mainstr/index.html', {'articles': articles})
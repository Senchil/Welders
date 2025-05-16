from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from .forms import ArticleForm

def index(request):
   news = Articles.objects.order_by('date')
   return render(request, 'news/index.html', {'news': news})

def create(request):
   if request.method == "POST":
      form = ArticleForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('news')
   else:
      form = ArticleForm()
      
def detail(request, article_id):
   article = get_object_or_404(Articles, id=article_id)
   return render(request, 'news/detail.html', {'article': article})

   return render(request, 'news/create_news.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Articles
from .forms import ArticleForm

def index(request):
   news = Articles.objects.order_by('date')
   return render(request, 'news/index.html', {'news': news})

@login_required(login_url='/auth/login/')
def create(request):
   if request.method == "POST":
      form = ArticleForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('news')
   else:
      form = ArticleForm()
      return render(request, 'news/create_news.html', {'form': form})
      
def detail(request, article_id):
   article = get_object_or_404(Articles, id=article_id)
   return render(request, 'news/detail.html', {'article': article})



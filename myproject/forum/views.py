from django.shortcuts import render

def index(request):
   data = {
      'title': 'Форум',
      'massive': ['pigga', 'nigga', 'egga']
   }
   return render(request, 'forum/index.html', data)

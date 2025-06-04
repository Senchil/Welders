from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainstr.urls')),
    path('auth/', include('authreg.urls')),
    path('forum/', include('forum.urls')),
    path('news/', include('news.urls')),
    path('about/', include('about.urls')),
    path('logout/', LogoutView.as_view(), name='logout')
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
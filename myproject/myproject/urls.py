from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainstr.urls')),
    path('registration/', include('registration.urls')),
    path('authorization/', include('authorization.urls')),
    path('forum/', include('forum.urls')),
    path('news/', include('news.urls'))
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
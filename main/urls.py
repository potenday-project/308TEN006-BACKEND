from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import board.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', board.views.index, name='index'),
    path('', board.views.splash, name='splash'),
    path('member/', include('member.urls')),
    path('board/', include('board.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
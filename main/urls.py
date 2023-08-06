from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import board.views, member.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.index, name='index'),
    path('member/', include('member.urls')),
    path('board/', include('board.urls')),
]

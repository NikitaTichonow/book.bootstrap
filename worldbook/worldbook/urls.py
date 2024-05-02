from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


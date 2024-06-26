from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from catalog import views

# Обработка ошибок
handler400 = 'catalog.views.tr_handler400'
handler403 = 'catalog.views.tr_handler403'
handler404 = 'catalog.views.tr_handler404'
handler500 = 'catalog.views.tr_handler500'

urlpatterns = [
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('api/v1/authorlist/', views.AuthorsAPIView.as_view()),
    path('api/v1/booklist/', views.BooksAPIView.as_view()),
    path('api/v1/genrelist/', views.GenresAPIView.as_view()),
    path('api/v1/user/', views.UserAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

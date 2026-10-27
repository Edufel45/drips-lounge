from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from shop.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("favicon.ico", RedirectView.as_view(url="/static/img/favicon.ico")),
    path("", index),
]
if settings.DEBUG and not settings.USE_CLOUD:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

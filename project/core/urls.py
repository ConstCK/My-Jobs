from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('catalogue.urls')),
]

if settings.DEBUG:
    urlpatterns += path("__debug__/", include("debug_toolbar.urls")),

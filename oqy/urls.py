from django.contrib import admin
from django.urls import include, path

from oqy.yasg import urlpatterns as docurls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("oqy.core.infrastructure.api.urls")),
    path("auth/", include("oqy.auth.urls")),
]

urlpatterns += docurls

from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("oqy.core.infrastructure.api.urls")),
    path("auth/", include("oqy.auth.urls")),
    path('swagger/', get_swagger_view(title='OQY App API')),
]

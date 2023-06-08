from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include("oqy.core.infrastructure.api.urls")),
    path("auth/", include("oqy.auth.urls")),
]

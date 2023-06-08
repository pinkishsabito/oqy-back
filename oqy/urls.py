from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="OQY BACK",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="ozhetov.arsen@gmail.com"),
        license=openapi.License(name="AITU License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("oqy.core.infrastructure.api.urls")),
    path("auth/", include("oqy.auth.urls")),
    path("swagger/", schema_view.with_ui("swagger"), name="swagger"),
]

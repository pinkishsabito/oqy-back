from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
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
    patterns=[
        path("api/", include("oqy.core.infrastructure.api.urls")),
        path("auth/", include("oqy.auth.urls")),
    ],
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(
        "swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    # path(
    #     "swagger/",
    #     TemplateView.as_view(
    #         template_name="./oqy/swaggerui/swaggerui.html",
    #         extra_context={"schema_url": "openapi-schema"},
    #     ),
    #     name="swagger",
    # ),
    path(
        "openapi/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

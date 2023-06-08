from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view


router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", include(router.urls)),

    path("auth/", include("oqy.auth.urls")),
    path("api/", include("oqy.core.infrastructure.api.urls")),

    path('api_schema/', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
    path('docs/', TemplateView.as_view(template_name='docs.html', extra_context={'schema_url': 'api_schema'}), name='swagger-ui'),
]

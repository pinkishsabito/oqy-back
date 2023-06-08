from django.urls import include, path


urlpatterns = [
    path("", include("oqy.core.infrastructure.api.book.urls")),
    path("", include("oqy.core.infrastructure.api.group.urls")),
    path("", include("oqy.core.infrastructure.api.user.urls")),
]

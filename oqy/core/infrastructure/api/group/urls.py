from django.urls import path

from oqy.core.infrastructure.api.group.views import (
    GroupCreateView,
    GroupDetailView,
    GroupUpdateView,
    GroupDeleteView,
    ManagerAddView,
    ManagerRemoveView,
    ForumDetailView,
    ForumMessageCreateView,
    ForumMessageDetailView,
    ForumMessageUpdateView,
    ForumMessageDeleteView,
)

urlpatterns = [
    path("groups/", GroupCreateView.as_view(), name="group-create"),
    path("groups/<int:pk>/", GroupDetailView.as_view(), name="group-detail"),
    path("groups/<int:pk>/", GroupUpdateView.as_view(), name="group-update"),
    path("groups/<int:pk>/", GroupDeleteView.as_view(), name="group-delete"),
    path("groups/<int:pk>/managers/", ManagerAddView.as_view(), name="manager-add"),
    path(
        "groups/<int:group_pk>/managers/<int:manager_pk>/",
        ManagerRemoveView.as_view(),
        name="manager-remove",
    ),
    path(
        "groups/<int:group_id>/forum/", ForumDetailView.as_view(), name="forum-detail"
    ),
    path(
        "groups/<int:group_id>/forum/messages/",
        ForumMessageCreateView.as_view(),
        name="forum-message-create",
    ),
    path(
        "groups/<int:group_id>/forum/messages/<int:message_id>/",
        ForumMessageDetailView.as_view(),
        name="forum-message-detail",
    ),
    path(
        "groups/<int:group_id>/forum/messages/<int:message_id>/",
        ForumMessageUpdateView.as_view(),
        name="forum-message-update",
    ),
    path(
        "groups/<int:group_id>/forum/messages/<int:message_id>/",
        ForumMessageDeleteView.as_view(),
        name="forum-message-delete",
    ),
]

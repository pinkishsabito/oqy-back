from django.urls import path

from oqy.core.infrastructure.api.user.views import (
    CreateUserView,
    UserDetailsView,
    UserGroupsView,
    UpdateUserView,
    DeleteUserView,
)


urlpatterns = [
    path("users/", CreateUserView.as_view(), name="create_user"),
    path("users/<int:user_id>/", UserDetailsView.as_view(), name="user_details"),
    path("users/<int:user_id>/groups/", UserGroupsView.as_view(), name="user_groups"),
    path("users/<int:user_id>/", UpdateUserView.as_view(), name="update_user"),
    path("users/<int:user_id>/", DeleteUserView.as_view(), name="delete_user"),
]

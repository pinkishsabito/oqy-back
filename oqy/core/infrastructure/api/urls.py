from django.urls import path

from oqy.core.infrastructure.api.views import (
    CreateUserView,
    UserDetailsView,
    UserGroupsView,
    UpdateUserView,
    DeleteUserView,
    GroupCreateView,
    GroupDetailView,
    GroupUpdateView,
    GroupDeleteView,
    ManagerAddView,
    ManagerRemoveView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookQuestionCreateView,
    BookQuestionDetailView,
    BookQuestionUpdateView,
    BookQuestionDeleteView,
    ForumDetailView,
    ForumMessageCreateView,
    ForumMessageDetailView,
    ForumMessageUpdateView,
    ForumMessageDeleteView,
)

urlpatterns = [
    path("users/", CreateUserView.as_view(), name="create_user"),
    path("users/<int:user_id>/", UserDetailsView.as_view(), name="user_details"),
    path("users/<int:user_id>/groups/", UserGroupsView.as_view(), name="user_groups"),
    path("users/<int:user_id>/", UpdateUserView.as_view(), name="update_user"),
    path("users/<int:user_id>/", DeleteUserView.as_view(), name="delete_user"),
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
    path("books/", BookCreateView.as_view(), name="create_book"),
    path("books/<int:book_id>/", BookDetailView.as_view(), name="book_detail"),
    path("books/<int:book_id>/", BookUpdateView.as_view(), name="update_book"),
    path("books/<int:book_id>/", BookDeleteView.as_view(), name="delete_book"),
    path(
        "books/<int:book_id>/questions/",
        BookQuestionCreateView.as_view(),
        name="create_book_question",
    ),
    path(
        "books/<int:book_id>/questions/<int:question_id>/",
        BookQuestionDetailView.as_view(),
        name="book_question_detail",
    ),
    path(
        "books/<int:book_id>/questions/<int:question_id>/",
        BookQuestionUpdateView.as_view(),
        name="update_book_question",
    ),
    path(
        "books/<int:book_id>/questions/<int:question_id>/",
        BookQuestionDeleteView.as_view(),
        name="delete_book_question",
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

from django.urls import path

from oqy.core.infrastructure.api.book.views import (
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookQuestionCreateView,
    BookQuestionDetailView,
    BookQuestionUpdateView,
    BookQuestionDeleteView,
)

urlpatterns = [
    path("book/", BookCreateView.as_view(), name="create_book"),
    path("book/<int:book_id>/", BookDetailView.as_view(), name="book_detail"),
    path("book/<int:book_id>/", BookUpdateView.as_view(), name="update_book"),
    path("book/<int:book_id>/", BookDeleteView.as_view(), name="delete_book"),
    path(
        "book/<int:book_id>/questions/",
        BookQuestionCreateView.as_view(),
        name="create_book_question",
    ),
    path(
        "book/<int:book_id>/questions/<int:question_id>/",
        BookQuestionDetailView.as_view(),
        name="book_question_detail",
    ),
    path(
        "book/<int:book_id>/questions/<int:question_id>/",
        BookQuestionUpdateView.as_view(),
        name="update_book_question",
    ),
    path(
        "book/<int:book_id>/questions/<int:question_id>/",
        BookQuestionDeleteView.as_view(),
        name="delete_book_question",
    ),
]

from django.urls import path

from oqy.core.infrastructure.api.book.views import (
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
    BookQuestionCreateView,
    BookQuestionDetailView,
    BookQuestionUpdateView,
    BookQuestionDeleteView,
    BookUploadView,
)


urlpatterns = [
    path("books/", BookCreateView.as_view(), name="create_book"),
    path("books/<int:book_id>/", BookDetailView.as_view(), name="book_detail"),
    path("books/<int:book_id>/update/", BookUpdateView.as_view(), name="update_book"),
    path("books/<int:book_id>/delete/", BookDeleteView.as_view(), name="delete_book"),
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
        "books/<int:book_id>/questions/<int:question_id>/update/",
        BookQuestionUpdateView.as_view(),
        name="update_book_question",
    ),
    path(
        "books/<int:book_id>/questions/<int:question_id>/delete/",
        BookQuestionDeleteView.as_view(),
        name="delete_book_question",
    ),
    path("books/upload/", BookUploadView.as_view(), name="upload_book"),
]

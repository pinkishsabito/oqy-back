from django.http import JsonResponse
from django.views import View

from oqy.core.domain.entities import Book, BookQuestion
from oqy.core.domain.repositories import (
    BookRepository,
    BookQuestionRepository,
)
from oqy.core.infrastructure.api.book.serializers import (
    BookSerializer,
    BookQuestionSerializer,
)
from oqy.core.infrastructure.database.repositories import (
    DjangoGroupRepository,
    DjangoBookRepository,
    DjangoBookQuestionRepository,
)


class BookCreateView(View):
    def post(self, request) -> JsonResponse:
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_date = request.POST.get("publication_date")
        group_id = request.POST.get("group_id")

        book_repository: BookRepository = DjangoBookRepository()
        group_repository = DjangoGroupRepository()
        group = group_repository.get_group(group_id)
        if group is None:
            return JsonResponse({"error": "Invalid group ID"}, status=400)

        book = book_repository.create_book(title, author, publication_date, group)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, status=201)


class BookDetailView(View):
    def get(self, request, book_id) -> JsonResponse:
        book_repository: BookRepository = DjangoBookRepository()
        book = book_repository.get_book(book_id)
        if book is None:
            return JsonResponse({"error": "Book not found"}, status=404)

        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)


class BookUpdateView(View):
    def put(self, request, book_id) -> JsonResponse:
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_date = request.POST.get("publication_date")

        book_repository: BookRepository = DjangoBookRepository()
        book = book_repository.get_book(book_id)
        if book is None:
            return JsonResponse({"error": "Book not found"}, status=404)

        updated_book = Book(book.id, title, author, publication_date, book.group)
        book_repository.update_book(updated_book)
        serializer = BookSerializer(updated_book)
        return JsonResponse(serializer.data)


class BookDeleteView(View):
    def delete(self, request, book_id) -> JsonResponse:
        book_repository: BookRepository = DjangoBookRepository()
        book = book_repository.get_book(book_id)
        if book is None:
            return JsonResponse({"error": "Book not found"}, status=404)

        book_repository.delete_book(book)
        return JsonResponse({"message": "Book deleted"}, status=204)


class BookQuestionCreateView(View):
    def post(self, request, book_id) -> JsonResponse:
        question_text = request.POST.get("question_text")

        book_repository: BookRepository = DjangoBookRepository()
        book = book_repository.get_book(book_id)
        if book is None:
            return JsonResponse({"error": "Invalid book ID"}, status=400)

        book_question_repository: BookQuestionRepository = (
            DjangoBookQuestionRepository()
        )
        book_question = book_question_repository.create_question(question_text, book)
        serializer = BookQuestionSerializer(book_question)
        return JsonResponse(serializer.data, status=201)


class BookQuestionDetailView(View):
    def get(self, request, book_id, question_id) -> JsonResponse:
        book_question_repository: BookQuestionRepository = (
            DjangoBookQuestionRepository()
        )
        book_question = book_question_repository.get_question(question_id)
        if book_question is None:
            return JsonResponse({"error": "Invalid question ID"}, status=404)

        serializer = BookQuestionSerializer(book_question)
        return JsonResponse(serializer.data, status=200)


class BookQuestionUpdateView(View):
    def put(self, request, book_id, question_id) -> JsonResponse:
        question_text = request.POST.get("question_text")

        book_question_repository: BookQuestionRepository = (
            DjangoBookQuestionRepository()
        )
        book_question = book_question_repository.get_question(question_id)
        if book_question is None:
            return JsonResponse({"error": "Invalid question ID"}, status=404)

        book_question_repository.update_question(
            BookQuestion(book_question.id, question_text, book_question.book)
        )

        serializer = BookQuestionSerializer(book_question)
        return JsonResponse(serializer.data, status=200)


class BookQuestionDeleteView(View):
    def delete(self, request, book_id, question_id) -> JsonResponse:
        book_question_repository: BookQuestionRepository = (
            DjangoBookQuestionRepository()
        )
        book_question = book_question_repository.get_question(question_id)
        if book_question is None:
            return JsonResponse({"error": "Invalid question ID"}, status=404)

        book_question_repository.delete_question(book_question)
        return JsonResponse({"message": "Question deleted successfully"}, status=204)

import re
from collections import Counter
from random import randint

from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.views import APIView

from oqy.core.domain.entities import Book, BookQuestion
from oqy.core.domain.repositories import (
    BookRepository,
    BookQuestionRepository,
)
from oqy.core.infrastructure.api.book.serializers import (
    BookSerializer,
    BookQuestionSerializer,
)
from oqy.core.infrastructure.database.models import ModelWordOrder
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


class BookUploadView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()

            common_words = self._extract_common_words(book.content)

            word_order = self._generate_word_order(book.content, common_words)

            for _, word in enumerate(word_order, start=1):
                if word in common_words:
                    order = common_words.index(word) + 1
                else:
                    order = randint(2001, 5000)

                ModelWordOrder.objects.create(book=book, word=word, order=order)

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def _extract_common_words(content):
        words = re.findall(r"\b\w+\b", content)

        filtered_words = [word.lower() for word in words if len(word) > 6]
        word_counter = Counter(filtered_words)

        common_words = [word for word, _ in word_counter.most_common(2000)]

        return common_words

    @staticmethod
    def _generate_word_order(content, common_words):
        words = re.findall(r"\b\w+\b", content)

        filtered_words = [word.lower() for word in words if len(word) > 6]

        word_order = []
        for _, word in enumerate(filtered_words):
            if word in common_words:
                word_order.append(word)

        return word_order

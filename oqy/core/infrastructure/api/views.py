from django.http import JsonResponse
from django.views import View

from oqy.core.domain.entities import User, Group, Book, BookQuestion, ForumMessage
from oqy.core.domain.repositories import (
    GroupRepository,
    UserRepository,
    BookRepository,
    BookQuestionRepository,
    ForumRepository,
)
from oqy.core.infrastructure.api.serializers import (
    BookSerializer,
    BookQuestionSerializer,
)
from oqy.core.infrastructure.database.repositories import (
    DjangoUserRepository,
    DjangoGroupRepository,
    DjangoBookRepository,
    DjangoBookQuestionRepository,
    DjangoForumRepository,
)


class CreateUserView(View):
    def post(self, request) -> JsonResponse:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_repository = DjangoUserRepository()
        user = user_repository.create_user(username, email, password)
        return JsonResponse(
            {"id": user.id, "username": user.username, "email": user.email}
        )


class UserDetailsView(View):
    def get(self, request, user_id) -> JsonResponse:
        user_repository = DjangoUserRepository()
        user = user_repository.get_user_by_id(user_id)

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)
        return JsonResponse(
            {"id": user.id, "username": user.username, "email": user.email}
        )


class UpdateUserView(View):
    def put(self, request, user_id) -> JsonResponse:
        user_repository = DjangoUserRepository()
        user = user_repository.get_user_by_id(user_id)

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        updated_username = request.POST.get("username")
        updated_email = request.POST.get("email")

        user_repository.update_user(User(user.id, updated_username, updated_email))
        return JsonResponse(
            {"id": user.id, "username": user.username, "email": user.email}
        )


class DeleteUserView(View):
    def delete(self, request, user_id) -> JsonResponse:
        user_repository = DjangoUserRepository()
        user = user_repository.get_user_by_id(user_id)

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        user_repository.delete_user(user)
        return JsonResponse({"message": "User deleted"})


class UserGroupsView(View):
    def get(self, request, user_id) -> JsonResponse:
        user_repository = DjangoUserRepository()

        user = user_repository.get_user_by_id(user_id)
        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        groups = user_repository.get_user_groups(user)

        group_data = [group.to_dict() for group in groups]

        return JsonResponse({"groups": group_data})


class GroupCreateView(View):
    def post(self, request) -> JsonResponse:
        name = request.POST.get("name")
        group_repository: GroupRepository = DjangoGroupRepository()
        group = group_repository.create_group(name)
        return JsonResponse({"group_id": group.id})


class GroupDetailView(View):
    def get(self, request, pk) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        group = group_repository.get_group(pk)
        if group:
            return JsonResponse({"group_id": group.id, "name": group.name})
        return JsonResponse({"error": "Group not found"}, status=404)


class GroupUpdateView(View):
    def put(self, request, pk) -> JsonResponse:
        name = request.PUT.get("name")
        group_repository: GroupRepository = DjangoGroupRepository()
        group = group_repository.get_group(pk)
        if group:
            group_repository.update_group(Group(group.id, name, group.managers))
            return JsonResponse({"success": "Group updated successfully"})
        return JsonResponse({"error": "Group not found"}, status=404)


class GroupDeleteView(View):
    def delete(self, request, pk) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        group = group_repository.get_group(pk)
        if group:
            group_repository.delete_group(group)
            return JsonResponse({"success": "Group deleted successfully"})
        return JsonResponse({"error": "Group not found"}, status=404)


class ManagerAddView(View):
    def post(self, request, pk) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        user_repository: UserRepository = DjangoUserRepository()

        group = group_repository.get_group(pk)
        if not group:
            return JsonResponse({"error": "Group not found"}, status=404)

        username = request.POST.get("username")
        user = user_repository.get_user_by_username(username)
        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        group_repository.add_manager(group, user)
        return JsonResponse({"success": "Manager added successfully"})


class ManagerRemoveView(View):
    def delete(self, request, group_pk, manager_pk) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        user_repository: UserRepository = DjangoUserRepository()

        group = group_repository.get_group(group_pk)
        if not group:
            return JsonResponse({"error": "Group not found"}, status=404)

        manager = user_repository.get_user_by_id(manager_pk)
        if not manager:
            return JsonResponse({"error": "Manager not found"}, status=404)

        group_repository.remove_manager(group, manager)
        return JsonResponse({"success": "Manager removed successfully"})


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


class ForumDetailView(View):
    def get(self, request, group_id) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        forum_repository: ForumRepository = DjangoForumRepository()

        group = group_repository.get_group(group_id)
        if group is None:
            return JsonResponse({"error": "Invalid group ID"}, status=400)

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        return JsonResponse(forum.to_dict(), status=200)


class ForumMessageCreateView(View):
    def post(self, request, group_id) -> JsonResponse:
        user_repository: UserRepository = DjangoUserRepository()
        group_repository: GroupRepository = DjangoGroupRepository()
        forum_repository: ForumRepository = DjangoForumRepository()

        user_id = request.POST.get("user_id")
        message_text = request.POST.get("message_text")

        user = user_repository.get_user_by_id(user_id)
        if user is None:
            return JsonResponse({"error": "User not found"}, status=404)

        group = group_repository.get_group(group_id)
        if group is None:
            return JsonResponse({"error": "Group not found"}, status=404)

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        message = forum_repository.create_message(user, forum, message_text)
        return JsonResponse(message.to_dict(), status=201)


class ForumMessageDetailView(View):
    def get(self, request, group_id, message_id) -> JsonResponse:
        forum_repository: ForumRepository = DjangoForumRepository()

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        messages = forum_repository.get_messages(forum)
        message = next((m for m in messages if m.id == message_id), None)
        if message is None:
            return JsonResponse({"error": "Message not found"}, status=404)

        return JsonResponse(message.to_dict(), status=200)


class ForumMessageUpdateView(View):
    def put(self, request, group_id, message_id) -> JsonResponse:
        message_text = request.POST.get("message_text")

        forum_repository: ForumRepository = DjangoForumRepository()

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        messages = forum_repository.get_messages(forum)
        message = next((m for m in messages if m.id == message_id), None)
        if message is None:
            return JsonResponse({"error": "Message not found"}, status=404)

        forum_repository.update_message(
            ForumMessage(message.id, message.sender, message.forum, message_text)
        )

        return JsonResponse(message.to_dict(), status=200)


class ForumMessageDeleteView(View):
    def delete(self, request, group_id, message_id) -> JsonResponse:
        forum_repository: ForumRepository = DjangoForumRepository()

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        messages = forum_repository.get_messages(forum)
        message = next((m for m in messages if m.id == message_id), None)
        if message is None:
            return JsonResponse({"error": "Message not found"}, status=404)

        forum_repository.delete_message(message)

        return JsonResponse({"message": "Message deleted"}, status=200)

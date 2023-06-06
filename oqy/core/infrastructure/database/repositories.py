from typing import Optional

from oqy.core.domain.entities import (
    User,
    Group,
    Book,
    BookQuestion,
    Forum,
    ForumMessage,
)
from oqy.core.domain.repositories import (
    UserRepository,
    GroupRepository,
    BookRepository,
    BookQuestionRepository,
    ForumRepository,
)
from oqy.core.infrastructure.database.models import (
    ModelUser,
    ModelGroup,
    ModelBook,
    ModelBookQuestion,
    ModelForum,
    ModelForumMessage,
)


class DjangoUserRepository(UserRepository):
    def create_user(self, username: str, email: str, password: str) -> User:
        user = ModelUser.objects.create(
            username=username, email=email, password=password
        )
        return User(user.id, user.username, user.email)

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        try:
            user = ModelUser.objects.get(id=user_id)
            return User(user.id, user.username, user.email)
        except ModelUser.DoesNotExist:
            return None

    def get_user_by_username(self, username: str) -> Optional[User]:
        try:
            user = ModelUser.objects.get(username=username)
            return User(user.id, user.username, user.email)
        except ModelUser.DoesNotExist:
            return None

    def get_user_by_email(self, email: str) -> Optional[User]:
        try:
            user = ModelUser.objects.get(email=email)
            return User(user.id, user.username, user.email)
        except ModelUser.DoesNotExist:
            return None

    def delete_user(self, user: User) -> None:
        ModelUser.objects.filter(id=user.id).delete()

    def get_user_groups(self, user: User) -> list[Group]:
        user_model = ModelUser.objects.get(id=user.id)
        group_models = user_model.groups.all()
        groups = [Group(group.id, group.name, []) for group in group_models]
        return groups

    def update_user(self, user: User) -> None:
        user_model = ModelUser.objects.get(id=user.id)
        user_model.username = user.username
        user_model.email = user.email
        user_model.save()


class DjangoGroupRepository(GroupRepository):
    def create_group(self, name: str) -> Group:
        group = ModelGroup.objects.create(name=name)
        return Group(group.id, group.name, [])

    def get_group(self, group_id: int) -> Optional[Group]:
        try:
            group = ModelGroup.objects.get(id=group_id)
            return Group(group.id, group.name, [])
        except ModelGroup.DoesNotExist:
            return None

    def add_manager(self, group: Group, manager: User) -> None:
        group_model = ModelGroup.objects.get(id=group.id)
        user_model = ModelUser.objects.get(id=manager.id)
        group_model.managers.add(user_model)

    def remove_manager(self, group: Group, manager: User) -> None:
        group_model = ModelGroup.objects.get(id=group.id)
        user_model = ModelUser.objects.get(id=manager.id)
        group_model.managers.remove(user_model)

    def update_group(self, group: Group) -> None:
        try:
            group_model = ModelGroup.objects.get(id=group.id)
            group_model.name = group.name
            group_model.save()
        except ModelGroup.DoesNotExist as exc:
            raise ValueError("Group not found") from exc

    def delete_group(self, group: Group) -> None:
        try:
            group_model = ModelGroup.objects.get(id=group.id)
            group_model.delete()
        except ModelGroup.DoesNotExist as exc:
            raise ValueError("Group not found") from exc


class DjangoBookRepository(BookRepository):
    def create_book(
        self, title: str, author: str, publication_date: str, group: Group
    ) -> Book:
        group_model = ModelGroup.objects.get(id=group.id)
        book = ModelBook.objects.create(
            title=title,
            author=author,
            publication_date=publication_date,
            group=group_model,
        )
        return Book(book.id, book.title, book.author, book.publication_date, group)

    def get_book(self, book_id: int) -> Optional[Book]:
        try:
            book = ModelBook.objects.get(id=book_id)
            group_repository = DjangoGroupRepository()
            group = group_repository.get_group(book.group.id)
            return Book(book.id, book.title, book.author, book.publication_date, group)
        except ModelBook.DoesNotExist:
            return None

    def update_book(self, book: Book) -> None:
        try:
            book_model = ModelBook.objects.get(id=book.id)
            book_model.title = book.title
            book_model.author = book.author
            book_model.publication_date = book.publication_date
            book_model.save()
        except ModelBook.DoesNotExist as exc:
            raise ValueError("Book not found") from exc

    def delete_book(self, book: Book) -> None:
        try:
            book_model = ModelBook.objects.get(id=book.id)
            book_model.delete()
        except ModelBook.DoesNotExist as exc:
            raise ValueError("Book not found") from exc


class DjangoBookQuestionRepository(BookQuestionRepository):
    def create_question(self, question_text: str, book: Book) -> BookQuestion:
        book_repository = DjangoBookRepository()
        book_model = book_repository.get_book(book.id)
        question = ModelBookQuestion.objects.create(
            question_text=question_text, book=book_model
        )
        return BookQuestion(question.id, question.question_text, book)

    def get_question(self, question_id: int) -> Optional[BookQuestion]:
        try:
            question = ModelBookQuestion.objects.get(id=question_id)
            book_repository = DjangoBookRepository()
            book = book_repository.get_book(question.book.id)
            return BookQuestion(question.id, question.question_text, book)
        except ModelBookQuestion.DoesNotExist:
            return None

    def update_question(self, question: BookQuestion) -> None:
        try:
            question_model = ModelBookQuestion.objects.get(id=question.id)
            question_model.question_text = question.question_text
            question_model.save()
        except ModelBookQuestion.DoesNotExist as exc:
            raise ValueError("Book question not found.") from exc

    def delete_question(self, question: BookQuestion) -> None:
        try:
            question_model = ModelBookQuestion.objects.get(id=question.id)
            question_model.delete()
        except ModelBookQuestion.DoesNotExist as exc:
            raise ValueError("Book question not found.") from exc


class DjangoForumRepository(ForumRepository):
    def create_forum(self, group: Group) -> Forum:
        group_repository = DjangoGroupRepository()
        group_model = group_repository.get_group(group.id)
        forum = ModelForum.objects.create(group=group_model)
        return Forum(forum.id, group)

    def get_forum(self, forum_id: int) -> Optional[Forum]:
        try:
            forum = ModelForum.objects.get(id=forum_id)
            group_repository = DjangoGroupRepository()
            group = group_repository.get_group(forum.group.id)
            return Forum(forum.id, group)
        except ModelForum.DoesNotExist:
            return None

    def create_message(
        self, sender: User, forum: Forum, message_text: str
    ) -> ForumMessage:
        forum_model = ModelForum.objects.get(id=forum.id)
        sender_model = ModelUser.objects.get(id=sender.id)
        message = ModelForumMessage.objects.create(
            sender=sender_model, forum=forum_model, message_text=message_text
        )
        return ForumMessage(message.id, sender, forum, message.message_text)

    def get_messages(self, forum: Forum) -> list[ForumMessage]:
        forum_model = ModelForum.objects.get(id=forum.id)
        messages = ModelForumMessage.objects.filter(forum=forum_model)
        return [
            ForumMessage(message.id, message.sender, forum, message.message_text)
            for message in messages
        ]

    def update_message(self, message: ForumMessage) -> None:
        message_model = ModelForumMessage.objects.get(id=message.id)
        message_model.message_text = message.message_text
        message_model.save()

    def delete_message(self, message: ForumMessage) -> None:
        message_model = ModelForumMessage.objects.get(id=message.id)
        message_model.delete()

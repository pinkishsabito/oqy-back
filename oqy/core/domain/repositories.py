from abc import ABC, abstractmethod
from typing import Optional

from oqy.core.domain.entities import (
    User,
    Group,
    Book,
    BookQuestion,
    Forum,
    ForumMessage,
)


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, username: str, email: str, password: str) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def delete_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user_groups(self, user: User) -> list[Group]:
        pass

    @abstractmethod
    def update_user(self, user: User) -> None:
        pass


class GroupRepository(ABC):
    @abstractmethod
    def create_group(self, name: str) -> Group:
        pass

    @abstractmethod
    def get_group(self, group_id: int) -> Optional[Group]:
        pass

    @abstractmethod
    def add_manager(self, group: Group, manager: User) -> None:
        pass

    @abstractmethod
    def remove_manager(self, group: Group, manager: User) -> None:
        pass

    @abstractmethod
    def update_group(self, group: Group) -> None:
        pass

    @abstractmethod
    def delete_group(self, group: Group) -> None:
        pass


class BookRepository(ABC):
    @abstractmethod
    def create_book(
        self, title: str, author: str, publication_date: str, group: Group
    ) -> Book:
        pass

    @abstractmethod
    def get_book(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def update_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def delete_book(self, book: Book) -> None:
        pass


class BookQuestionRepository(ABC):
    @abstractmethod
    def create_question(self, question_text: str, book: Book) -> BookQuestion:
        pass

    @abstractmethod
    def get_question(self, question_id: int) -> Optional[BookQuestion]:
        pass

    @abstractmethod
    def update_question(self, question: BookQuestion) -> None:
        pass

    @abstractmethod
    def delete_question(self, question: BookQuestion) -> None:
        pass


class ForumRepository(ABC):
    @abstractmethod
    def create_forum(self, group: Group) -> Forum:
        pass

    @abstractmethod
    def get_forum(self, forum_id: int) -> Optional[Forum]:
        pass

    @abstractmethod
    def create_message(
        self, sender: User, forum: Forum, message_text: str
    ) -> ForumMessage:
        pass

    @abstractmethod
    def get_messages(self, forum: Forum) -> list[ForumMessage]:
        pass

    @abstractmethod
    def update_message(self, message: ForumMessage) -> None:
        pass

    @abstractmethod
    def delete_message(self, message: ForumMessage) -> None:
        pass

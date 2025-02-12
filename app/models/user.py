import re
from uuid import uuid4

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, validates

from app.models.base import Base

from config import EMAIL_LENGTH, USERNAME_LENGTH


class User(Base):
    __tablename__ = "user"

    id: Mapped[PG_UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    username: Mapped[str] = mapped_column(
        String(USERNAME_LENGTH), unique=True, nullable=False, index=True
    )
    email: Mapped[str] = mapped_column(
        String(EMAIL_LENGTH), unique=True, nullable=False, index=True
    )
    password: Mapped[str] = mapped_column(nullable=False)

    @validates("email")
    def validate_email(self, key, email):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        return email

    @validates("username")
    def validate_username(self, key, first_name):
        username_regex = r"^[\w.@+-]+$"
        if not re.match(username_regex, first_name):
            raise ValueError("Username is invalid")
        return first_name

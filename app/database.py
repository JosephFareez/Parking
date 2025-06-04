from typing import Annotated

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column

# Add type annotations for custom types
int_pk: type = Annotated[int, mapped_column(primary_key=True)]
str10: type = Annotated[str, mapped_column(String(10), nullable=False)]
str50: type = Annotated[str, mapped_column(String(50), nullable=False)]
str100: type = Annotated[str, mapped_column(String(100), nullable=False)]


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

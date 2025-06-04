from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# Create typed base class
class Base(DeclarativeBase):
    pass


# Create SQLAlchemy instance with our base class
db = SQLAlchemy(model_class=Base)

# Create a type alias for our models
Model = db.Model

# from typing import Annotated
#
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import String
# from sqlalchemy.orm import mapped_column
#
# int_pk: type = Annotated[int, mapped_column(primary_key=True)]
# str10: type = Annotated[str, mapped_column(String(10), nullable=False)]
# str50: type = Annotated[str, mapped_column(String(50), nullable=False)]
# str100: type = Annotated[str, mapped_column(String(100), nullable=False)]
#
#
# db = SQLAlchemy()

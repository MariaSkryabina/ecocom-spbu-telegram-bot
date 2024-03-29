
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from typing_extensions import Annotated

int_pk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    pass




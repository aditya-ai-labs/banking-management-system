from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from database import Base


class Customer(Base):

    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    account_number = Column(
        String,
        unique=True
    )

    name = Column(
        String
    )

    email = Column(
        String
    )

    phone = Column(
        String
    )

    balance = Column(
        Float,
        default=0
    )
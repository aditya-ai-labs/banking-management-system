from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from database import Base


class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)

    account_number = Column(String, unique=True)

    name = Column(String)

    email = Column(String)

    phone = Column(String)

    balance = Column(Float, default=0)


class TransactionHistory(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer)

    account_number = Column(String)

    transaction_type = Column(String)

    amount = Column(Float)
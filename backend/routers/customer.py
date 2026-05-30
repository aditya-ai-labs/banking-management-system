from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db
from models import Customer

from schemas import CustomerCreate
from schemas import Transaction
from models import TransactionHistory

import random

router = APIRouter(
    prefix="/customer",
    tags=["Customer"]
)


@router.post("/create")
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    account_number = str(
        random.randint(
            1000000000,
            9999999999
        )
    )

    new_customer = Customer(
        account_number=account_number,
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        balance=0
    )

    db.add(new_customer)

    db.commit()

    db.refresh(new_customer)

    return {
        "message": "Account Created",
        "account_number": account_number
    }


@router.get("/all")
def get_customers(
    db: Session = Depends(get_db)
):

    return db.query(
        Customer
    ).all()


@router.put("/deposit/{customer_id}")
def deposit_money(
    customer_id: int,
    transaction: Transaction,
    db: Session = Depends(get_db)
):

    customer = db.query(
        Customer
    ).filter(
        Customer.id == customer_id
    ).first()

    if not customer:

        return {
            "message": "Customer Not Found"
        }

    customer.balance += transaction.amount

    history = TransactionHistory(
    customer_id=customer.id,
    account_number=customer.account_number,
    transaction_type="Deposit",
    amount=transaction.amount
)

    db.add(history)

    db.commit()

    return {
        "message": "Amount Deposited"
    }


@router.put("/withdraw/{customer_id}")
def withdraw_money(
    customer_id: int,
    transaction: Transaction,
    db: Session = Depends(get_db)
):

    customer = db.query(
        Customer
    ).filter(
        Customer.id == customer_id
    ).first()

    if not customer:

        return {
            "message": "Customer Not Found"
        }

    if customer.balance < transaction.amount:

        return {
            "message": "Insufficient Balance"
        }

    customer.balance -= transaction.amount

    history = TransactionHistory(
    customer_id=customer.id,
    account_number=customer.account_number,
    transaction_type="Withdraw",
    amount=transaction.amount
)

    db.add(history)

    db.commit()

    return {
        "message": "Amount Withdrawn"
    }


@router.delete("/delete/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = db.query(
        Customer
    ).filter(
        Customer.id == customer_id
    ).first()

    if not customer:

        return {
            "message": "Customer Not Found"
        }

    db.delete(customer)

    db.commit()

    return {
        "message": "Customer Deleted"
    }
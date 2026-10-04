from typing import Annotated
from fastapi import Depends

from techlog.db.local import LocalDataBase
from techlog.db.customer_repository import CustomerRepository


database = LocalDataBase()


def obtain_database() -> LocalDataBase:
    return database


def obtain_customer_repository(
        local_db: Annotated[
            LocalDataBase,
            Depends(obtain_database)
        ]
    ) -> CustomerRepository:

    return CustomerRepository(local_db)

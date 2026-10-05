from typing import Annotated

from techlog.schemas.customer import Customer, CreateUpdateCustomer
from fastapi import APIRouter, Depends, HTTPException
from techlog.dependencies import obtain_customer_repository
from techlog.db.customer_repository import CustomerRepository

router = APIRouter(
    prefix="/customers"
)

CUS_LIST = [
    Customer(id_=1, name="Raphael", email="raphael@rossi.com", telephone="123456789"),
    Customer(id_=2, name="João", email="joao@rossi.com", telephone="123456789")
]


@router.get("/", response_model=list[Customer])
async def customers_list(customer_repository: Annotated[
        CustomerRepository, Depends(obtain_customer_repository)
        ]):
    return await customer_repository.customer_list()


@router.get("/{customer_id}", response_model=Customer | None)
async def acquire_customer(
    customer_repository: Annotated[CustomerRepository, Depends(obtain_customer_repository)],
    customer_id: int
):
    customer = await customer_repository.acquire_customer(customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer don't founded")

    return customer

@router.post('/', response_model=Customer, status_code=201)
async def customer_create(
    customer_repository: Annotated[CustomerRepository, Depends(obtain_customer_repository)],
    customer: CreateUpdateCustomer
):
    return await customer_repository.create_customer(customer)

@router.put("/{cliente_id}", response_model=Customer | None)
async def update_customer(
    customer_repository: Annotated[CustomerRepository, Depends(obtain_customer_repository)],
    customer_id: int,
    customer: CreateUpdateCustomer
    ):
    updated_customer = await customer_repository.update_customer(customer_id=customer_id, customer=customer)
    if not updated_customer:
        raise HTTPException(status_code=404, detail='Customer not founded')
    return updated_customer
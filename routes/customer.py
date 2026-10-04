from techlog.schemas.customer import Customer
from fastapi import APIRouter

router = APIRouter(
    prefix="/customers"
)

CUS_LIST = [
    Customer(id_=1, name="Raphael", email="raphael@rossi.com", telephone="123456789"),
    Customer(id_=2, name="João", email="joao@rossi.com", telephone="123456789")
]


@router.get("/", response_model=list[Customer])
async def customers_list():
    return CUS_LIST


@router.get("/{customer_id}", response_model=Customer | None)
async def acquire_customer(customer_id: int):
    for customer in CUS_LIST:
        if customer.id_ == customer_id:
            return customer

    return None

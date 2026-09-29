from techlog.schemas.customer import Customer
from fastapi import APIRouter

router = APIRouter(
    prefix="/customers"
)


@router.get("/", response_model=list[Customer])
async def customers_list():
    cus_list = [
        Customer(name="Raphael", email="raphael@rossi.com", telephone="123456789"),
        Customer(name="João", email="joao@rossi.com", telephone="123456789")
    ]
    return cus_list

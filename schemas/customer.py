from pydantic import BaseModel


class Customer(BaseModel):
    id_: int
    name: str
    email: str
    telephone: str

class CreateUpdateCustomer(BaseModel):
    name: str
    email: str
    telephone: str
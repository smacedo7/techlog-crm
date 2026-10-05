from techlog.db.local import LocalDataBase
from techlog.schemas.customer import Customer, CreateUpdateCustomer


class CustomerRepository:
    def __init__(self, database: LocalDataBase):
        self.db = database

    async def customer_list(self) -> list[Customer]:
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, email, telephone FROM customers"
            )
            lines = cursor.fetchall()
            customers = [
                Customer(id_=line[0], name=line[1], email=line[2], telephone=line[3])
                for line in lines
            ]
            return customers

    async def acquire_customer(self, customer_id) -> Customer | None:
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
            SELECT id, name, email, telephone FROM customers WHERE id = ?
            ''', (customer_id,))
            linha = cursor.fetchone()
            if linha:
                return Customer(id_=linha[0], name=linha[1], email=linha[2], telephone=linha[3])
            return None

    async def create_customer(self, customer: CreateUpdateCustomer) -> Customer:
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO customers (name, email, telephone) VALUES (?,?,?)", (customer.name, customer.email, customer.telephone)
            )
            customer_id = cursor.lastrowid
            return Customer(id_=customer_id, name=customer.name, email=customer.email, telephone=customer.telephone)

    async def update_customer(self, customer_id, customer: CreateUpdateCustomer) -> Customer | None:
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE customers SET name = ?, email = ?, telephone = ?
            ''', (customer.name, customer.email, customer.telephone))

        if cursor.rowcount == 0:
            return None
        return Customer(id_=customer_id, name=customer.name, email=customer.email, telephone=customer.telephone)

    async def delete_customer(self, customer_id: int) -> bool:
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM customers WHERE id = ?
            """, (customer_id,))

            return cursor.rowcount > 0
    
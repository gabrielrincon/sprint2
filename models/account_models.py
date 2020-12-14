from pydantic import BaseModel


class AccountIn(BaseModel):
    name: str
    type: str
    balance: int
    id_account: int = 0


class AccountOut(BaseModel):
    name: str
    type: str
    balance: int
    id_account: int

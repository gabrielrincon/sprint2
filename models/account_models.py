from pydantic import BaseModel


class AccountIn(BaseModel):
    name: str
    type: str
    balance: int


class AccountOut(BaseModel):
    name: str
    type: str
    balance: int

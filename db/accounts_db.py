from datetime import datetime
from pydantic import BaseModel


class AccountInDB(BaseModel):
    id_account: int = 0
    name: str
    type: str
    balance: int = 0


database_accounts = []
generator = {"id":0}

def get_account(name: str):
    if name in database_accounts:
        return database_accounts[name]
    else:
        return None

def create_account(accounts_in_db: AccountInDB):
    generator["id"] = generator["id"] + 1
    accounts_in_db.id_account = generator["id"]
    database_accounts.append(accounts_in_db)
    return accounts_in_db

def update_account(accounts_in_db: AccountInDB):
    database_accounts[accounts_in_db.id_account] = accounts_in_db
    return accounts_in_db



from datetime import datetime
from pydantic import BaseModel

from models.account_models import AccountIn


class AccountInDB(BaseModel):
    id_account: int = 0
    name: str
    type: str
    balance: int = 0


database_accounts = []
generator = {"id":0}

def get_account_db(name: str):
    for account in database_accounts:
        print(account)
        if account.name == name:
            print("encontrado", account)
            return account
        else:
            print("no es", account)
    return None

def add_balance_account_db(account_in: AccountIn):
    for account in database_accounts:
        print(account)
        if account.name == account_in.name:
            account.balance += account_in.balance
            print("encontrado", account)
            return account
        else:
            print("no es", account)
    return None

def create_account_db(accounts_in: AccountIn):
    print("aqui")
    print(accounts_in)
    print(accounts_in.name)
    if get_account_db(accounts_in.name) is None:
        print("verdadero")
        print(generator)
        print(generator['id'])
        generator['id'] = generator['id'] + 1
        accounts_in.id_account = generator['id']
        print(accounts_in)
        database_accounts.append(accounts_in)
        return True
    else:
        print("falso")
        return False

def update_account(accounts_in_db: AccountInDB):
    database_accounts[accounts_in_db.id_account] = accounts_in_db
    return accounts_in_db



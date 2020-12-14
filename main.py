from db.accounts_db import get_account_db, create_account_db

from models.account_models import AccountIn, AccountOut

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.post("/account/create/")
async def create_account(account_in: AccountIn):
    result = create_account_db(account_in)
    print(result)
    if result:
        return {"estado":"creado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="La cuenta ya fue creada")

@api.get("/account/get/{name}")
async def get_account(name: str):
    account_in_db = get_account_db(name)
    if account_in_db == None:
        raise HTTPException(status_code=404,
                            detail="la cuenta no existe no existe")
    account_out = AccountOut(**account_in_db.dict())
    return account_out


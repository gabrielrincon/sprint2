from db.accounts_db import AccountInDB
from db.accounts_db import create_account, update_account, get_account

from models.account_models import AccountIn, AccountOut

from fastapi import FastAPI
from fastapi import HTTPException


app = FastAPI()


# @app.post("/user/auth/")
# async def auth_user(user_in: UserIn):
#     user_in_db = get_user(user_in.username)
#     if user_in_db == None:
#         raise HTTPException(status_code=404,
#                             detail="El usuario no existe")
#     if user_in_db.password != user_in.password:
#         return {"Autenticado": False}
#     return {"Autenticado": True}
#

@app.post("/account/create/")
async def create_account(account_in: AccountIn):
    account_in_db = get_account(account_in.name)
    if account_in_db == None:
        result = create_account(account_in)
        return {"estado":"creado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="La cuenta ya fue creada")

@app.get("/account/get/{name}")
async def get_account(name: str):
    account_in_db = get_account(name)
    if account_in_db == None:
        raise HTTPException(status_code=404,
                            detail="la cuenta no existe no existe")
    account_out = AccountOut(**account_in_db.dict())
    return account_out


from db.accounts_db import get_account_db, create_account_db, add_balance_account_db

from models.account_models import AccountIn, AccountOut

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
    "https://pacti-finanzas-front.herokuapp.com/"
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.post("/account/create/")
async def create_account(account_in: AccountIn):
    result = create_account_db(account_in)
    print(result)
    if result:
        return {"estado":"creado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="La cuenta ya fue creada")

@api.post("/account/add_balance/")
async def add_balance_account(account_in: AccountIn):
    result = add_balance_account_db(account_in)
    print(result)
    if result:
        return {"estado":"balance_modificado_ok","cuenta":result}
    else:
        raise HTTPException(status_code=404, detail="La cuenta " + account_in.name + " no existe")

@api.get("/account/get/{name}")
async def get_account(name: str):
    account_in_db = get_account_db(name)
    if account_in_db == None:
        raise HTTPException(status_code=404,
                            detail="la cuenta no existe no existe")
    account_out = AccountOut(**account_in_db.dict())
    return account_out


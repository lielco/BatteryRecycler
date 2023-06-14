from fastapi import FastAPI
from endpoints import pickup
from internal import admin

app = FastAPI()
app.include_router(router=pickup.router)
app.include_router(router=admin.router)
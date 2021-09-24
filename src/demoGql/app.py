from fastapi import FastAPI

from demoGql.api import router

app = FastAPI()
app.include_router(router)

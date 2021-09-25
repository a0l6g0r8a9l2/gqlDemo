import logging
from pathlib import PosixPath

from fastapi import FastAPI

from demoGql.api import router
from demoGql.database import create_db

logging.basicConfig(level=logging.INFO)
app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def check_db():
    db = PosixPath(PosixPath('..')
                   .resolve()
                   .parent
                   .resolve()
                   .__str__() + '/database.sqlite3')
    if not db.is_file():
        logging.warning(f'No db found in {db}')
        create_db()

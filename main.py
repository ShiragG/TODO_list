from fastapi import FastAPI

from routers import tasks_get
from db import models
from db.database import engine

app = FastAPI()

app.include_router(tasks_get.router)

models.Base.metadata.create_all(engine)
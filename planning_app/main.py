from fastapi import FastAPI
from . import  models
from  .routers import router

app = FastAPI()

#models.Base.metadata.create_all(engine)


app.include_router(router)




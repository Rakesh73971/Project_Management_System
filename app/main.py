from fastapi import FastAPI
from . import models
from .database import engine
from .routers import oauth,user,oraganization_member,organization,project



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(oauth.router)
app.include_router(user.router)
app.include_router(oraganization_member.router)
app.include_router(organization.router)
app.include_router(project.router)
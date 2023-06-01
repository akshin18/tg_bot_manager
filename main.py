from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uvicorn

from sql_app import models, schemas, crud
from sql_app.db import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory= "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


@app.get("/get_bots",response_model=list[schemas.Bots])
async def get_bots(db: Session = Depends(get_db)):
    print(crud.get_bots(db))
    return crud.get_bots(db)



def start_server():

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True,
    )





if __name__ == "__main__":
    start_server()
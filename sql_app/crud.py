from sqlalchemy.orm import Session

from sql_app import models

def get_bots(db:Session):
    return db.query(models.Bots).filter().all()
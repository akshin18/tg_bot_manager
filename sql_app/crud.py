from sqlalchemy.orm import Session

from sql_app import models

def get_bots(db:Session):
    bots = db.query(models.Bots).filter().all()
    for bot in bots:
        bot.subs = db.query(models.Users).filter_by(bot=bot.id).count()
    return bots

def get_users(db:Session,id:int,ofset:int):
    return db.query(models.Users).filter_by(bot=id).limit(10).offset(ofset).all()


def add_bot(db:Session,token,name):
    bot = models.Bots(token=token,name=name)
    db.add(bot)
    db.commit()
    db.refresh(bot)
    return bot
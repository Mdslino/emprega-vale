from sqlalchemy.orm import Session

from emprega_vale.db.session import SessionLocal


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    except:  # NOQA
        db.rollback()
    finally:
        db.close()

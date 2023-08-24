from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError, IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.exceptions import AppException
from config import settings

# reminder: for establishing a connection to postgres
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

# reminder: for communicating or talking to postgres
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    except DBAPIError as exc:
        db.rollback()
        raise AppException.OperationError(error_message=exc.orig.args[0])
    except IntegrityError as exc:
        db.rollback()
        raise AppException.OperationError(error_message=exc.orig.args[0])
    finally:
        db.close()

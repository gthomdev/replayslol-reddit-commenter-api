from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import Config

config = Config()
database_connection_string = config.connection_string
engine = create_engine(database_connection_string,
                       pool_pre_ping=True,
                       connect_args={
                           "keepalives": 1,
                           "keepalives_idle": 30,
                            "keepalives_interval": 10,
                            "keepalives_count": 5
                       }
                       )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

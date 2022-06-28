from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine(
    "postgresql+psycopg2://postgres:12345@localhost:5432/data_warehouse"
)
session = Session(engine)
Base = declarative_base()
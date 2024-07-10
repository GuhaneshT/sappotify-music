from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



url_for_database='sqlite:///./music.db'

engine=create_engine(url_for_database,connect_args={"check_same_thread":False})

sessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

base=declarative_base()

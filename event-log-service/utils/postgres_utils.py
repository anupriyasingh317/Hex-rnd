import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
load_dotenv()
engine = create_engine(os.environ["POSTGRES_URL"], echo=True)

def get_session():
    return Session(engine)
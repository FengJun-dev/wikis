from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://FJ:010421042@localhost:5432/Wiki')
Session = sessionmaker(bind=engine)

session = Session()

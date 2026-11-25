from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://practicedb_v7ky_user:DPhctbA6nw5IRUEfNnnuiy8VnTAsmGro@dpg-dc38680m7kps73dge0pg-a.oregon-postgres.render.com/practicedb_v7ky"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()

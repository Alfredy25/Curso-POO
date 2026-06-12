from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
                                                                                            #conector pymysql o mysqlconnector
engine = create_engine('mysql+pymysql://root:admin@127.0.0.1:3306/python_course', # dialecto+driver://usuario:password@host:puerto/name_base_de_datos
                       echo=True,
                       pool_size=10,
                       max_overflow=20,
                       pool_timeout=30,
                       pool_recycle=1800)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
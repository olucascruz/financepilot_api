from sqlalchemy.ext.declarative import declarative_base

# URL de conexão com o banco PostgreSQL
DATABASE_URL = "sqlite:///./database.db"


# Base para modelos
Base = declarative_base()
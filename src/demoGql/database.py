from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from demoGql.settings import settings
from demoGql.tables import Base

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False},
)

Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


def recreate_db():
    Base.metadata.create_all(engine)
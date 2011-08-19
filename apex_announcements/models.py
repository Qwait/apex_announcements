import datetime

from sqlalchemy import Column
from sqlalchemy import Unicode
from sqlalchemy import types

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension 

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Announcement(Base):
    __tablename__ = 'apex_announcements'
    __table_args__ = {"sqlite_autoincrement": True}
 
    id = Column(types.BigInteger(), primary_key=True)
    title = Column(Unicode(40), default=u'')
    content = Column(Unicode(255), default=u'')
    creation_date = Column(types.Date(), default=datetime.datetime.now, index=True)
    site_wide = Column(types.Boolean(), default=True)
    members_only = Column(types.Boolean(), default=False)

    @classmethod
    def current(cls, **kwargs):
        return DBSession.query(cls).filter_by(**kwargs).all()

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
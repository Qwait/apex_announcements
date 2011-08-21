from sqlalchemy import Column
from sqlalchemy import Unicode
from sqlalchemy import types

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from sqlalchemy.sql import functions

from zope.sqlalchemy import ZopeTransactionExtension 

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Announcement(Base):
    """ Announcement table - apex_announcements
    """
    __tablename__ = 'apex_announcements'
    __table_args__ = {"sqlite_autoincrement": True}
 
    id = Column(types.BigInteger(), primary_key=True)
    title = Column(Unicode(40), default=u'')
    content = Column(Unicode(255), default=u'')
    creation_date = Column(types.Date(), default=functions.current_date(), index=True)
    kind = Column(types.Enum(u'S', u'M'), default=u'S', index=True)

    @classmethod
    def current(cls, **kwargs):
        return DBSession.query(cls).filter_by(**kwargs).all()


def current_announcements_for_request(request):
    """ return list of current announcements
    """
    defaults = {
        'kind': u'S',
    }
    if request.user:
        defaults['kind'] = u'M'
    return Announcement.current(**defaults)

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

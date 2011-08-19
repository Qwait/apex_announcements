from zope.interface import implements
from zope.interface import Interface

class IApexAnnouncements(Interface):
    pass
    
class ApexAnnouncementsImplementation(object):
    implements(IApexAnnouncements)

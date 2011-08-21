from zope.interface import implements
from zope.interface import Interface

class IApexAnnouncements(Interface):
    """ Set up IApexAnnouncements
    """
    pass
    
class ApexAnnouncementsImplementation(object):
    """ Set up IApexAnnouncements
    """
    implements(IApexAnnouncements)

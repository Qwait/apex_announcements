from sqlalchemy import engine_from_config

from apex_announcements.interfaces import IApexAnnouncements
from apex_announcements.interfaces import ApexAnnouncementsImplementation
from apex_announcements.models import initialize_sql

def includeme(config):
    settings = config.registry.settings
    
    initialize_sql(engine_from_config(settings, 'sqlalchemy.'))

    config.registry.registerUtility(ApexAnnouncementsImplementation, IApexAnnouncements)
    
    config.add_subscriber('apex_announcements.subscribers.add_renderer_globals', 'pyramid.events.BeforeRender')
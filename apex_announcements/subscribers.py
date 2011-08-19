from pyramid.threadlocal import get_current_request
from pyramid.security import authenticated_userid

from apex_announcements.models import Announcement

def add_renderer_globals(event):
    request = event.get('request')
    if request is None:
        request = get_current_request()

    globs = {
        'announcements': Announcement.current(site_wide=True)
    }
    event.update(globs)

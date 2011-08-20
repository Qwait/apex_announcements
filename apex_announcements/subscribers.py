from pyramid.threadlocal import get_current_request
from pyramid.security import authenticated_userid

from apex_announcements.models import Announcement
from apex_announcements.models import current_announcements_for_request

def add_renderer_globals(event):
    request = event.get('request')
    if request is None:
        request = get_current_request()

    globs = {
        'announcements': current_announcements_for_request(request),
    }
    event.update(globs)

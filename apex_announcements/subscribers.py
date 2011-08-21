from pyramid.threadlocal import get_current_request

from apex_announcements.models import current_announcements_for_request

def add_renderer_globals(event):
    """ Adds announcements to template
    """
    request = event.get('request')
    if request is None:
        request = get_current_request()

    globs = {
        'announcements': current_announcements_for_request(request),
    }
    event.update(globs)

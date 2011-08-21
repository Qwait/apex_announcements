Using Templates with Apex Announcements
=======================================

**Jinja Templates**

::

    {%- from 'apex_announcements:templates/announcements.jinja2' import show_announcements with context -%}

Access it by doing: 

::

    {{ show_announcements() }}
    
**Mako Templates**

::

    <%namespace file="apex_announcements:templates/announcements.mako" import="*"/>

Access it by doing:

::

     ${show_announcements()}

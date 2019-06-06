from django.conf.urls import url
from django.views.generic import RedirectView

from .views import talks_list, workshops_list, schedule, workshops_refresh_tickets
from .views import session_detail, preview, session_detail_schedule

urlpatterns = [
    url('^$', RedirectView.as_view(pattern_name='talks_list')),
    url('^(?P<type>(talk|workshop|sprint))s/(?P<session_id>\\d+)/$', session_detail, name='session_detail'),
    url('^(?P<type>(talk|workshop|sprint))s/(?P<slot_id>\\d+)/schedule/$', session_detail_schedule, name='session_detail_schedule'),
    url('^talks/$', talks_list, name='talks_list'),
    url('^workshops/$', workshops_list, name='workshops_list'),
    url('^workshops/refresh_tickets$', workshops_refresh_tickets, name='workshops_refresh_tickets'),
    url('^schedule/$', schedule, name='programme_schedule'),
    url('^preview/$', preview, name='preview'),
]

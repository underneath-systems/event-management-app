from django.urls import path
from django.conf.urls import include, url
from . import views
from events_operations.views import *

app_name = 'users_operations'

urlpatterns = [
    path('', views.mainUsers.as_view(), name='mainUsers'),
    path('register_attendee', views.register_Attendee.as_view(), name='register_attendee'),
    path('register_organizer', views.register_Organizer.as_view(), name='register_organizer'),
    path('register_staff', views.register_Staff.as_view(), name='register_staff'),
    # url(r'^update/(?P<event_id>\d+)/$', event_update, name='event_update'),
    # url(r'^delete/(?P<event_id>\d+)/$', event_delete, name='event_delete'),
]

from django.urls import path
from django.conf.urls import include, url
from . import views
from users_operations.views import *
from django.contrib.auth.decorators import login_required

app_name = 'users_operations'

urlpatterns = [
    path('', login_required(views.mainUsers.as_view()), name='mainUsers'),
    # path('register_attendee', login_required(views.register_Attendee.as_view()), name='register_attendee'),

    path('register_attendee', login_required(register_attendee), name='register_attendee'),
    path('register_organizer', login_required(register_organizer), name='register_organizer'),
    path('register_staff', login_required(register_staff), name='register_staff'),
    path('invitations/', login_required(views.invitationsList.as_view(template_name = "users/invitations.html")), name='invitations'),
    path('assistance/', login_required(views.assistanceList.as_view(template_name = "users/assistance.html")), name='assistance'),
    #path('results/', login_required(views.mainUsers.results), name='results'),
    # url(r'^update/(?P<event_id>\d+)/$', event_update, name='event_update'),
    # url(r'^delete/(?P<event_id>\d+)/$', event_delete, name='event_delete'),
]

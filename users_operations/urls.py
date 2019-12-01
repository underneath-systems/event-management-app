from django.urls import path
from django.conf.urls import include, url
from . import views
from users_operations.views import *
from django.contrib.auth.decorators import login_required

app_name = 'users_operations'

urlpatterns = [
    path('', login_required(views.mainUsers.as_view()), name='mainUsers'),
    # path('register_attendee', login_required(views.register_Attendee.as_view()), name='register_attendee'),

    #path('register_attendee', login_required(register_attendee), name='register_attendee'),
    path('register_organizer', login_required(register_organizer), name='register_organizer'),
    path('register_staff', login_required(register_staff), name='register_staff'),
    path('invitations/', login_required(views.invitationsList.as_view(template_name = "users/invitations.html")), name='invitations'),
    path('assistance/', login_required(views.assistanceList.as_view(template_name = "users/assistance.html")), name='assistance'),
    path('register/', views.register),
    path('events/', login_required(views.eventsList.as_view(template_name = "users/events.html")), name='events'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('activate2/<uidb64>/<token>/', activate2, name='activate2'),
    path('invite/<int:event_id>/', login_required(send_invite), name='send_invite'),
    path('staff_events', login_required(staff_events.as_view(template_name = "users/staff_events.html")), name='staff_events'),
    path('assist_register/<int:event_id>/', assist_register, name='assist_register'),
    path('assist_confirm/<int:assist_id>/', assist_confirm, name='assist_confirm'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    #path('results/', login_required(views.mainUsers.results), name='results'),
    # url(r'^update/(?P<event_id>\d+)/$', event_update, name='event_update'),
    # url(r'^delete/(?P<event_id>\d+)/$', event_delete, name='event_delete'),
]

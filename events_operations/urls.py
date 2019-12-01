from django.urls import path
from django.conf.urls import include, url
from . import views
from events_operations.views import *
from django.contrib.auth.decorators import login_required

app_name = 'events_operations'

urlpatterns = [
    path('', login_required(views.mainEvents.as_view()), name='mainEvents'),
    # path('create', login_required(views.Create.as_view()), name='create'),
    path('create', login_required(event_create), name='create'),
    url(r'^update/(?P<event_id>\d+)/$', login_required(event_update), name='event_update'),
    url(r'^delete/(?P<event_id>\d+)/$', login_required(event_delete), name='event_delete'),
    path('details/', login_required(views.eventsList.as_view(template_name = "event/details.html")), name='details'), 
    # path(r'^details/(?P<event_id>\d+)/$' , views.displaySingleEvent.as_view(), name='single_event'),
    path('details/<int:event_id>/', login_required(views.displaySingleEvent.as_view()), name='single_event'),
    path('invite/<int:event_id>/', login_required(send_invite), name='send_invite'),
    path('assistants/<int:event_id>/', login_required(assist_List.as_view(template_name = "event/assistance.html")), name='assist_list'),
    path('guests/<int:event_id>/', login_required(guests_List.as_view(template_name = "event/guests.html")), name='guests_list'),
    path('cancel_invitation/<int:invitation_id>/', login_required(cancel_invitation.as_view()), name='cancel_invitation'),
    path('assign_staff/<int:event_id>/', login_required(assign_staff), name='assign_staff'),
]

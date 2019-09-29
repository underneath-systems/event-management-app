from django.urls import path
from django.conf.urls import include, url
from . import views
from events_operations.views import *
from django.contrib.auth.decorators import login_required

app_name = 'events_operations'

urlpatterns = [
    # path('nuevo', PostresListado.as_view(template_name = "postres/index.html"), name='leer'),
    path('', login_required(views.mainEvents.as_view()), name='mainEvents'),
    path('create', login_required(views.Create.as_view()), name='create'),
    url(r'^update/(?P<event_id>\d+)/$', login_required(event_update), name='event_update'),
    url(r'^delete/(?P<event_id>\d+)/$', login_required(event_delete), name='event_delete'),
    # path('details', views.EventDetails.as_view(), name='details'),
    path('details/', login_required(views.eventsList.as_view(template_name = "event/details.html")), name='details'), 
    # path('eventos/detalle/<int:pk>', views.EventDetails.as_view(template_name = "event/details.html"), name='detalles'),
]

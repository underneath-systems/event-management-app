from django.urls import path
from django.conf.urls import include, url
from . import views
from events_operations.views import *

urlpatterns = [
    # path('nuevo', PostresListado.as_view(template_name = "postres/index.html"), name='leer'),
    path('', views.mainEvents.as_view(), name='mainEvents'),
    path('create', views.Create.as_view(), name='create'),
    url(r'^update/(?P<event_id>\d+)/$', event_update, name='event_update'),
    url(r'^delete/(?P<event_id>\d+)/$', event_delete, name='event_delete'),
    # path('details', views.EventDetails.as_view(), name='details'),
    path('details/', views.eventsList.as_view(template_name = "event/details.html"), name='details'), 
    # path('eventos/detalle/<int:pk>', views.EventDetails.as_view(template_name = "event/details.html"), name='detalles'),
]

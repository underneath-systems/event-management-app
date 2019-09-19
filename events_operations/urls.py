from django.urls import path
from django.conf.urls import include, url
from . import views
from events_operations.views import *

urlpatterns = [
    # path('nuevo', PostresListado.as_view(template_name = "postres/index.html"), name='leer'),
    path('', views.mainEvents.as_view(), name='mainEvents'),
    path('create', views.Create.as_view(), name='create'),
    # path('details', views.EventDetails.as_view(), name='details'),
    # path('update', views.UpdateEvent.as_view(), name='update'),
    # path('cancel', views.CancelEvent.as_view(), name='cancel'),
    # path('tag', views.TagEvent.as_view(), name='tag'),
    # path('staff', views.StaffEvent.as_view(), name='staff'),
    # path('cancelInvitation', views.CancelInvitation.as_view(), name='cancelInvitation'),
    url(r'^nuevo$', views.Create.as_view(), name='evento_crear'),
    # url(r'^nuevo$', event_view, name='event_view'),
    # url(r'tabla/', views.mostrarTabla, name='mostrarTabla'),
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('eventos/', views.eventosListado.as_view(template_name = "event/details.html"), name='eventos'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('eventos/detalle/<int:pk>', views.EventDetails.as_view(template_name = "event/details.html"), name='detalles'),
]

from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.mainEvents.as_view(), name='mainEvents'),
    path('create', views.Create.as_view(), name='create'),
    path('details', views.EventDetails.as_view(), name='details'),
    path('update', views.CancelEvent.as_view(), name='update'),
    path('cancel', views.CancelEvent.as_view(), name='cancel'),
    path('tag', views.TagEvent.as_view(), name='tag'),
    path('staff', views.StaffEvent.as_view(), name='staff'),
    path('cancelInvitation', views.CancelInvitation.as_view(), name='cancelInvitation'),
]

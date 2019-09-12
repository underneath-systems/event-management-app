from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.mainEvents.as_view(), name='mainEvents'),
    path('create', views.Create.as_view(), name='create'),
]

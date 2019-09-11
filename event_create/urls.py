from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Create.as_view(), name='create'),
]

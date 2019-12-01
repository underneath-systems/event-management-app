from django.core.exceptions import PermissionDenied
from functools import wraps
from .models import *

class AttendeeMixin:
    def dispatch(self, request, *args, **kwargs):
        if Attendees.objects.filter(email=request.user.email):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class OrganizerMixin:
    def dispatch(self, request, *args, **kwargs):
        if Organizer.objects.filter(email=request.user.email):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied



class StaffMixin:
    def dispatch(self, request, *args, **kwargs):
        if Staff_event.objects.filter(email=request.user.email):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class AdminMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.users.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class AttendeeAndOrganizerMixin:
    def dispatch(self, request, *args, **kwargs):
        if Attendees.objects.filter(email=request.user.email) or Organizer.objects.filter(email=request.user.email):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class OrganizerAndStaffMixin:
    def dispatch(self, request, *args, **kwargs):
        if Staff_event.objects.filter(email=request.user.email) or Organizer.objects.filter(email=request.user.email):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

        
def organizer_required(f):
    @wraps(f)
    def g(request, *args, **kwargs):
        if Organizer.objects.filter(email=request.user.email):
            return f(request, *args, **kwargs)
        else:
            raise PermissionDenied
            #return HttpResponse('Unauthorized', status=401)
    return g


def staff_required(f):
    @wraps(f)
    def g(request, *args, **kwargs):
        if Staff_event.objects.filter(email=request.user.email):
            return f(request, *args, **kwargs)
        else:
            raise PermissionDenied
            #return HttpResponse('Unauthorized', status=401)
    return g

def admin_required(f):
    @wraps(f)
    def g(request, *args, **kwargs):
        if request.user.is_admin:
            return f(request, *args, **kwargs)
        else:
            raise PermissionDenied
            #return HttpResponse('Unauthorized', status=401)
    return g

def attendee_required(f):
    @wraps(f)
    def g(request, *args, **kwargs):
        if Attendees.objects.filter(email=request.user.email):
            return f(request, *args, **kwargs)
        else:
            raise PermissionDenied
            #return HttpResponse('Unauthorized', status=401)
    return g
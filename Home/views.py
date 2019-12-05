from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from users_operations.models import *
from events_operations.models import *
from django.db.models import Q


# def index(request):
#     template = loader.get_template('Home/index.html')
#     return HttpResponse( template.render({}, request))


class Index(View):
    template = 'Home/index.html'
    user_type = ''
    context = {'title': 'Index'}

    def get(self, request):
        queryset = request.GET.get("buscar")
        if queryset:
            event = Event.objects.filter(
                Q(name__icontains=queryset) |
                Q(description__icontains=queryset) |
                Q(tag__name__icontains=queryset)
                ).distinct()
            return render(request, 'users/results.html', {'event':event})
        elif request.user.is_authenticated:
            if Attendees.objects.filter(email=request.user.email):
                user_type = "Attendee"
                context = {'user_type': user_type}
                return render(request, self.template, context)
            if Organizer.objects.filter(email=request.user.email):
                user_type = "Organizer"
                context = {'user_type': user_type}
                return render(request, self.template, context)
            if Staff_event.objects.filter(email=request.user.email):
                user_type = "Staff"
                context = {'user_type': user_type}
                return render(request, self.template, context)
            if request.user.is_admin:
                user_type = "Admin"
                context = {'user_type': user_type}
                return render(request, self.template, context)
        return render(request, self.template, self.context)


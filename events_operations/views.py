from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic


class mainEvents(View):
    template = 'event/index.html'
    context = {'title': 'Events page'}

    def get(self, request):
        """
            Main events page.
        """
        print("Main events page request")
        return render(request, self.template, self.context)


class Create(View):
    template = 'event/create.html'
    context = {'title': 'create event'}

    def get(self, request):
        """
            Create a new event.
        """
        print("Creating event")
        return render(request, self.template, self.context)


class EventDetails(View):
    template = 'event/details.html'
    context = {'title': 'Event details'}

    def get(self, request):
        """
            Display event details.
        """
        print("Event details request.")
        return render(request, self.template, self.context)


class UpdateEvent(View):
    template = 'event/update.html'
    context = {'title': 'Cancel Event'}

    def get(self, request):
        """
            Update a event.
        """
        print("Event update request.")
        return render(request, self.template, self.context)


class CancelEvent(View):
    template = 'event/cancel.html'
    context = {'title': 'Cancel Event'}

    def get(self, request):
        """
            Cancel a event.
        """
        print("Event cancel request.")
        return render(request, self.template, self.context)


class TagEvent(View):
    template = 'event/tag.html'
    context = {'title': 'Tag Event'}

    def get(self, request):
        """
            Tag a event.
        """
        print("Event tag request.")
        return render(request, self.template, self.context)


class StaffEvent(View):
    template = 'event/staff.html'
    context = {'title': 'Staff Event'}

    def get(self, request):
        """
            Set staff to event.
        """
        print("Event staff request.")
        return render(request, self.template, self.context)


class CancelInvitation(View):
    template = 'event/cancelInvitation.html'
    context = {'title': 'Cancel invitation'}

    def get(self, request):
        """
            Cancel a invitation.
        """
        print("Cancel invitation request.")
        return render(request, self.template, self.context)

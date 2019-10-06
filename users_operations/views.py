from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse, reverse_lazy
from django.shortcuts import render,redirect
from users_operations.models import *
from users_operations.forms import *
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from django.views import generic
from django import forms

class mainUsers(View):
    template = 'users/index.html'
    context = {'title': 'Main users page'}

    def get(self, request):
        """
            Main users page.
        """
        print("Main users page request")
        return render(request, self.template, self.context)

class register_Attendee(CreateView):
    model = Attendees
    form_class = attendeesForm
    template_name = 'users/attendees_form.html'
    # fields = "__all__"
    success_message = 'Asistente a evento creado correctamente !'
    def get_success_url(self):
        return reverse('events_operations:details')


class register_Organizer(CreateView):
    model = Organizer
    form_class = organizerForm
    template_name = 'users/organizer_form.html'
    # fields = "__all__"
    success_message = 'Organizador creado correctamente !'
    def get_success_url(self):
        return reverse('events_operations:details')

class register_Staff(CreateView):
    model = Staff
    form_class = staffForm
    template_name = 'users/staff_form.html'
    # fields = "__all__"
    success_message = 'Staff creado correctamente !'
    def get_success_url(self):
        return reverse('events_operations:details')



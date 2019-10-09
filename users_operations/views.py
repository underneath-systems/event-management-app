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
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

class mainUsers(View):
    template = 'users/index.html'
    context = {'title': 'Main users page'}

    def get(self, request):
        """
            Main users page.
        """
        print("Main users page request")
        return render(request, self.template, self.context)

def register_attendee(request):
        if request.method == 'POST':
                form = attendeesForm(request.POST)
                if form.is_valid():
                        form.save()
                        name = request.POST.get('name')
                        email = request.POST.get('email')
                        password = request.POST.get('password')
                        photo_id = request.POST.get('photo_id')
                        qr_code = request.POST.get('qr_code')

                        attendees_body = render_to_string(
                        'users/email_attendee_registration.html', {
                                'Nombre': name,
                                'Email': email,
                                'Password': password,
                                'Fotografia': photo_id,
                                'Codigo QR': qr_code,
                                },
                        )

                        attendees_email_message = EmailMessage(
                                subject= 'Te han registrado como asistente en la plataforma!:  | Underneath Systems',
                                body=attendees_body,
                                from_email='sorgv.47@gmail.com',
                                to=['sorgv.47@gmail.com'],
                        )

                        attendees_email_message.content_subtype = 'html'
                        attendees_email_message.send()
                        print("------Enviando notificaciones por email------")
                return redirect('events_operations:details')
        else:
                form = attendeesForm()
        return render(request, 'users/attendees_form.html', {'form':form})



def register_organizer(request):
        if request.method == 'POST':
                form = organizerForm(request.POST)
                if form.is_valid():
                        form.save()
                        name = request.POST.get('name')
                        email = request.POST.get('email')
                        password = request.POST.get('password')
                        photo_id = request.POST.get('photo_id')
                        phone = request.POST.get('phone')

                        organizers_body = render_to_string(
                        'users/email_organizers_registration.html', {
                                'Nombre': name,
                                'Email': email,
                                'Password': password,
                                'Fotografia': photo_id,
                                'Telefono': phone,
                                },
                        )

                        organizers_email_message = EmailMessage(
                                subject= 'Tu registro como organizador esta completo! :  | Underneath Systems',
                                body=organizers_body,
                                from_email='underneath.systems@gmail.com',
                                to=['sorgv.47@gmail.com'],
                        )

                        organizers_email_message.content_subtype = 'html'
                        organizers_email_message.send()
                        print("------Enviando notificaciones por email al organizador------")
                return redirect('events_operations:details')
        else:
                form = organizerForm()
        return render(request, 'users/organizer_form.html', {'form':form})



def register_staff(request):
        if request.method == 'POST':
                form = staffForm(request.POST)
                if form.is_valid():
                        form.save()
                        name = request.POST.get('name')
                        email = request.POST.get('email')
                        password = request.POST.get('password')
                        photo_id = request.POST.get('photo_id')
                        working_hours = request.POST.get('working_hours')

                        staff_body = render_to_string(
                        'users/email_staff_registration.html', {
                                'Nombre': name,
                                'Email': email,
                                'Password': password,
                                'Fotografia': photo_id,
                                'Horas disponibles': working_hours,
                                },
                        )

                        staff_email_message = EmailMessage(
                                subject=  name + ' Has sido registrado exitosamente como miembro del staff : ' +   '  | Underneath Systems',
                                body=staff_body,
                                from_email='underneath.systems@gmail.com',
                                to=['sorgv.47@gmail.com'],
                        )

                        staff_email_message.content_subtype = 'html'
                        staff_email_message.send()
                        print("------Enviando notificaciones por email al staff------")
                return redirect('events_operations:details')
        else:
                form = staffForm()
        return render(request, 'users/staff_form.html', {'form':form})






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

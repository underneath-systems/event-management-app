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
from events_operations.models import Event, Assist
from django.db.models import Q

from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .admin import UserCreationForm
from .mixins import *

from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.shortcuts import get_object_or_404, render
import users_operations.qr as qra
import os


import datetime
from datetime import datetime


class mainUsers(AttendeeMixin, View):
    template = 'users/index.html'

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
            user = User.objects.get(email = request.user.email)
            context = {'user': user}
            return render(request, self.template, context)
        context = {'title': 'Main'}
        return render(request, self.template, context)
"""
@organizer_required
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
        return render(request, 'users/attendees_form.html', {'form':form})"""

@admin_required
def register_organizer(request):
        form = organizerForm()
        if request.method == "POST":
                form = organizerForm(data=request.POST)
                if form.is_valid():
                        user = form.save()
                        user.is_active = False
                        user.set_unusable_password()
                        user.save()
                        print(user.email)
                        current_site = get_current_site(request)
                        name = user.get_full_name()
                        email = request.POST.get('email')
                        admin = request.user.email
                        uid = urlsafe_base64_encode(force_bytes(user.pk))
                        token = account_activation_token.make_token(user)
                        activation_link = "http://{0}/users/activate2/{1}/{2}".format(current_site, uid, token)


                        attendees_body = render_to_string(
                                'users/email_organizers_registration.html', {
                                'Nombre': name,
                                'Admin': admin,
                                'Activation_link': activation_link,
                                },
                        )
                
                        attendees_email_message = EmailMessage(
                                subject= 'Te registraron como organizador.',
                                body=attendees_body,
                                to=[email],
                        )
                
                        attendees_email_message.content_subtype = 'html'
                        attendees_email_message.send()
                        return render(request, "users/pre_register_success.html")
        return render(request, "users/register.html", {'form': form})


@organizer_required
def register_staff(request):
        form = staffForm()
        if request.method == "POST":
                form = staffForm(data=request.POST)
                if form.is_valid():
                        user = form.save()
                        user.is_active = False
                        user.set_unusable_password()
                        user.save()
                        current_site = get_current_site(request)
                        name = user.get_full_name()
                        email = request.POST.get('email')
                        organizer = request.user.get_full_name()
                        uid = urlsafe_base64_encode(force_bytes(user.pk))
                        token = account_activation_token.make_token(user)
                        activation_link = "http://{0}/users/activate2/{1}/{2}".format(current_site, uid, token)


                        attendees_body = render_to_string(
                                'users/email_staff_registration.html', {
                                'Nombre': name,
                                'Activation_link': activation_link,
                                'Organizer': organizer,
                                },
                        )
                
                        attendees_email_message = EmailMessage(
                                subject= 'Te registraron como usuario Staff',
                                body=attendees_body,
                                to=[email],
                        )
                
                        attendees_email_message.content_subtype = 'html'
                        attendees_email_message.send()
                        return render(request, "users/pre_register_success.html")
        return render(request, "users/register.html", {'form': form})



class register_Attendee(OrganizerMixin, CreateView):
    model = Attendees
    form_class = attendeesForm
    template_name = 'users/attendees_form.html'
    # fields = "__all__"
    success_message = 'Asistente a evento creado correctamente !'
    def get_success_url(self):
        return reverse('events_operations:details')


class register_Organizer(OrganizerMixin, CreateView):
    model = Organizer
    form_class = organizerForm
    template_name = 'users/organizer_form.html'
    # fields = "__all__"
    success_message = 'Organizador creado correctamente !'
    def get_success_url(self):
        return reverse('events_operations:details')

    
class register_Staff(OrganizerMixin, CreateView):
    model = Staff_event
    form_class = staffForm
    template_name = 'users/staff_form.html'
    # fields = "__all__"
    success_message = 'Staff creado correctamente !'
    def get_success_url(self):
        return reverse('events_operations:details')

    
class invitationsList(AttendeeMixin, View):
    model = Assist
    template_name = 'users/invitations.html'

    def get(self, request):
        if request.user.is_authenticated:
            invitaciones = Assist.objects.filter(
                user__email = request.user.email,
                invitation = True,
                confirm = False)
            return render(request, self.template_name, {'invitaciones': invitaciones})
        return render(request, self.template, self.context)
    

class assistanceList(AttendeeMixin, View):
    model = Assist
    template_name = 'users/assistance.html'
    def get(self, request):
        if request.user.is_authenticated:
            asistencias = Assist.objects.filter(
                user__email = request.user.email,
                confirm = True)
            return render(request, self.template_name, {'asistencias': asistencias})
        return render(request, self.template, self.context)


class staff_events(StaffMixin, View):
        model = Event
        template_name = 'users/staff_events.html'
        def get(self, request):
                events = Event.objects.filter(
                        Q(staff_list__email__icontains=request.user.email)
                ).distinct()
                print(events)
                return render(request, self.template_name, {'Eventos': events})


class eventsList(ListView):
    model = Event
    template_name = 'users/events.html'
    # paginate_by = 2
    ordering = ['id']



def register(request):
    if request.user.is_authenticated:
        return HttpResponse("Ya estas registrado en la plataforma")
    else:
        form = attendeesForm()
        if request.method == "POST":
            form = attendeesForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                name = user.get_full_name()
                email = request.POST.get('email')
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user)
                activation_link = "http://{0}/users/activate/{1}/{2}".format(current_site, uid, token)


                attendees_body = render_to_string(
                    'users/email_attendee_registration.html', {
                        'Nombre': name,
                        'Activation_link': activation_link,
                    },
                )
                
                attendees_email_message = EmailMessage(
                    subject= 'Te registraste como usuario en la plataforma!:  | Underneath Systems',
                    body=attendees_body,
                    to=[email],
                )
                
                attendees_email_message.content_subtype = 'html'
                attendees_email_message.send()
                return render(request, "users/register_success.html", {'Email': user.email})
        return render(request, "users/register.html", {'form': form})


def activate(request, uidb64, token):    
        try:
                uid = force_text(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None
        if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                do_login(request, user)
                return redirect('/')
        else:
                return HttpResponse('<h1>Ocurrio un error.</h1><br>Por favor contacta al usuario que te registro')



def activate2(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                user = form.save()
                user.is_active = True
                user.save()
                user.backend = "django.contrib.auth.backends.ModelBackend"
                login(request, user)
                return redirect('/')
        else:
            form = SetPasswordForm(request.user)
            return render(request, 'users/activation.html', {'form': form})
    return HttpResponse('<h1>Ocurrio un error.</h1><br>Por favor contacta al usuario que te registro')

@attendee_required
def send_invite(request, event_id):
        event = get_object_or_404(Event, id=event_id)
        user = request.user
        invitated = Assist.objects.filter(
                user__email = user.email,
                event__id = event.id,
                invitation = True)
        if invitated.exists():
                message = "Ya cuentas con invitación al evento"
                return render(request, "users/invitation_error.html", {'Message': message})
        else:
                if event.capacity > 0:
                        prueba = Assist(invitation=True)
                        prueba.save()
                        qr = qra.create_qr(event.name, prueba.id)
                        prueba.qr_code = qr
                        prueba.save()
                        prueba.user.add(user)
                        prueba.event.add(event)
                        event.capacity -= 1
                        event.save()

                        body = render_to_string(
                                'users/invitation.html', {
                                'Nombre': user.get_full_name(),
                                'Evento': event.name,
                                },
                        )
                
                        message = EmailMessage(
                        subject= "Invitacion al evento " + event.name,
                        body=body,
                        to=[user.email],
                        )
                
                        message.content_subtype = 'html'
                        message.attach_file(prueba.qr_code.path)
                        message.send()

                        return render(request, "users/invitation_success.html", {'Evento': event.name, 'Email': user.email})
                else:
                        message = "Lo sentimos. El evento ya no cuenta con lugares disponibles"
                        return render(request, "users/invitation_error.html", {'Message': message})


@staff_required
def assist_register(request, event_id):
        qr = qra.read_qr()
        qs = Assist.objects.filter(
                id = qr,
                event__id = event_id
        )
        if qs.exists():
                invitated = qs.last()
                if invitated.confirm == True:
                        message = "El usuario ya registro su asistencia"
                        return render(request, "users/assist_error.html", {'Message': message})
                else:
                        user = invitated.user.last()
                        return render(request, "users/confirm_assist.html", {'Usuario': user, 'Evento':invitated})
        else:
                message = "La invitación proporcionada es incorrecta, favor de verificarla"
                return render(request, "users/assist_error.html", {'Message': message})


@staff_required
def assist_confirm(request, assist_id):
        qs = Assist.objects.filter(
                id = assist_id
        )
        assist = qs.last()
        assist.confirm = True
        assist.save()
        return render(request, "users/assist_success.html")
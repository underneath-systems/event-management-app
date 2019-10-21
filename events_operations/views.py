from django.shortcuts import render,redirect
from django.views.generic import View
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from events_operations.models import Event
from users_operations.models import User
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from events_operations.forms import eventForm, sendInviteForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def event_create(request):
        if request.method == 'POST':
                form = eventForm(request.POST)
                if form.is_valid():
                        form.save()
                        name = request.POST.get('name')
                        description = request.POST.get('description')
                        organizer = request.POST.get('organizer')
                        start = request.POST.get('start_date_time')
                        end = request.POST.get('end_date_time')
                        address = request.POST.get('address')
                        attendees = request.POST.getlist('attendees_list')
                        staff = request.POST.get('staff_list')
                        tag = request.POST.get('tag')
                        capacity = request.POST.get('capacity')

                        organizer_body = render_to_string(
                        'event/email_event_creation_organizer.html', {
                                'Nombre': name,
                                'Descripcion': description,
                                'Organizador': organizer,
                                'FechaInicio': start,
                                'FechaFin': end,
                                'Direccion': address,
                                'InvitadosIniciales': attendees,
                                'Staff': staff,
                                'Etiquetas': tag,
                                'Capacidadmaxima': capacity
                                },
                        )


                        attendees_body = render_to_string(
                        'event/email_event_creation_attendees.html', {
                                'Nombre': name,
                                'Descripcion': description,
                                'Organizador': organizer,
                                'FechaInicio': start,
                                'FechaFin': end,
                                'Direccion': address,
                                'InvitadosIniciales': attendees,
                                'Staff': staff,
                                'Etiquetas': tag,
                                'Capacidadmaxima': capacity
                                },
                        )

                        organizer_email_message = EmailMessage(
                                subject= 'Nuevo evento creado!: ' + name + ' | Underneath Systems',
                                body=organizer_body,
                                from_email='sorgv.47@gmail.com',
                                to=['sorgv.47@gmail.com'],
                        )

                        attendees_email_message = EmailMessage(
                                subject= 'Te han invitado a un evento!: '+name+ ' | Underneath Systems',
                                body=organizer_body,
                                from_email='sorgv.47@gmail.com',
                                to=['sorgv.47@gmail.com'],
                        )

                        organizer_email_message.content_subtype = 'html'
                        attendees_email_message.content_subtype = 'html'
                        organizer_email_message.send()
                        attendees_email_message.send()
                        print("------Enviando notificaciones por email------")
                return redirect('events_operations:details')
        else:
                form = eventForm()
        return render(request, 'event/event_form.html', {'form':form})



def event_update(request, event_id):
        event = Event.objects.get(pk=event_id)
        if request.method == 'GET':
                form = eventForm(instance=event)
        else:
                form = eventForm(request.POST, instance=event)
                if form.is_valid():
                        form.save()
                        name = request.POST.get('name')
                        description = request.POST.get('description')
                        organizer = request.POST.get('organizer')
                        start = request.POST.get('start_date_time')
                        end = request.POST.get('end_date_time')
                        address = request.POST.get('address')
                        attendees = request.POST.getlist('attendees_list')
                        staff = request.POST.get('staff_list')
                        tag = request.POST.get('tag')
                        capacity = request.POST.get('capacity')

                        organizer_body = render_to_string(
                        'event/email_event_update_organizer.html', {
                                'Nombre': name,
                                'Descripcion': description,
                                'Organizador': organizer,
                                'FechaInicio': start,
                                'FechaFin': end,
                                'Direccion': address,
                                'InvitadosIniciales': attendees,
                                'Staff': staff,
                                'Etiquetas': tag,
                                'Capacidadmaxima': capacity
                                },
                        )


                        attendees_body = render_to_string(
                        'event/email_event_update_attendees.html', {
                                'Nombre': name,
                                'Descripcion': description,
                                'Organizador': organizer,
                                'FechaInicio': start,
                                'FechaFin': end,
                                'Direccion': address,
                                'InvitadosIniciales': attendees,
                                'Staff': staff,
                                'Etiquetas': tag,
                                'Capacidadmaxima': capacity
                                },
                        )

                        organizer_email_message = EmailMessage(
                                subject= 'Has actualizado el evento: ' + name + ' exitosamente. | Underneath Systems',
                                body=organizer_body,
                                from_email='sorgv.47@gmail.com',
                                to=['sorgv.47@gmail.com'],
                        )

                        attendees_email_message = EmailMessage(
                                subject= 'El evento: '+name+ ' fue actualizado. | Underneath Systems',
                                body=organizer_body,
                                from_email='sorgv.47@gmail.com',
                                to=['sorgv.47@gmail.com'],
                        )

                        organizer_email_message.content_subtype = 'html'
                        attendees_email_message.content_subtype = 'html'
                        organizer_email_message.send()
                        attendees_email_message.send()
                        return redirect('events_operations:details')
        return render(request, 'event/event_form.html', {'form':form})


def event_delete(request, event_id):
        event = Event.objects.get(pk=event_id)
        if request.method == 'POST':
                name = event.name
                attendees = request.POST.getlist('attendees_list')
                deleted_event_body = render_to_string(
                'event/email_event_deleted.html', {
                        'Nombre': name,
                        },
                )

                deleted_email_message = EmailMessage(
                        subject= 'El evento: '+str(name)+ ' fue cancelado. | Underneath Systems',
                        body=deleted_event_body,
                        from_email='sorgv.47@gmail.com',
                        to=['sorgv.47@gmail.com'],
                )

                deleted_email_message.content_subtype = 'html'
                event.delete()
                deleted_email_message.send()
                print("----- Evento ", name, " eliminado-----")
                return redirect('events_operations:details')
        return render(request, 'event/event_delete.html', {'event':event})



def send_invite(request, event_id):
        results = Event.objects.filter(pk=event_id)
        for e in results:
                print ( e.attendees_list.all())

        if request.method == 'GET':
                form = sendInviteForm()
        else:
                form = sendInviteForm(request.POST)
                # form = sendInviteForm(request.POST, instance=users)
                if form.is_valid():
                        # form.save()
                        attendee = request.POST.get('email')
                        name = request.POST.get('email')

                        invite_body = render_to_string(
                        'event/email_event_update_organizer.html', {
                                'Invitado': attendee,
                                },
                        )

                        invite_email_message = EmailMessage(
                                subject= 'Te estan invitando al evento: '+name+ '. | Underneath Systems',
                                body=invite_body,
                                from_email='underneath.systems@gmail.com',
                                to=[attendee],
                        )


                        invite_email_message.content_subtype = 'html'
                        invite_email_message.send()
                        return redirect('events_operations:details')
        return render(request, 'event/send_invite.html', {'form':form})



class eventsList(ListView):
    model = Event
    template_name = 'event/details.html'
    # paginate_by = 2
    ordering = ['id']

class displaySingleEvent(View):
    """
        Displays just one event
    """
    template = 'event/single_event_details.html'
    context = {}

    def get(self, request, event_id):
        """
            GET in one event
        """
        event = get_object_or_404(Event, id=event_id)
        self.context['event'] = event
        self.context['title'] = str(event)
        return render(request, self.template, self.context)



class mainEvents(View):
    template = 'event/index.html'
    context = {'title': 'Events page'}

    def get(self, request):
        """
            Main events page.
        """
        print("Main events page request")
        return render(request, self.template, self.context)



class Create(CreateView):
    model = Event
    form_class = eventForm
    template_name = 'event/event_form.html'
    # fields = "__all__"
    success_message = 'Evento Creado Correctamente !'

    def get_success_url(self):
            messages.success(self.request, self.success_message)
            print("Evento creado exitosamente")
            return reverse('events_operations:details')


class EventDetails(DetailView): 
    model = Event


class UpdateEvent(UpdateView): 
    model = Event
    form_class = eventForm
    template_name = 'event/event_form.html'
    success_url = reverse_lazy('events_operations:details')
    # success_message = 'Evento Actualizado Correctamente !'
    # def get_success_url(self):
    #     return reverse('details')


class CancelEvent(DeleteView):
	model = Event
	template_name = 'event/event_delete.html'
	success_url = reverse_lazy('details')

# class CancelEvent(SuccessMessageMixin, DeleteView): 
#     model = Event
#     form = Event
#     fields = "__all__"     

#     # Redireccionamos a la página principal luego de eliminar un registro o postre
#     def get_success_url(self): 
#         success_message = 'Evento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
#         messages.success (self.request, (success_message))       
#         return reverse('leer') # Redireccionamos a la vista principal 'leer'



class TagEvent(SuccessMessageMixin, DeleteView): 
    model = Event
    form = Event
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Evento Etiquetado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('events') # Redireccionamos a la vista principal 'leer'





class CancelInvitation(SuccessMessageMixin, DeleteView): 
    model = Event
    form = Event
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Invitacion cancelada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('events') # Redireccionamos a la vista principal 'leer'

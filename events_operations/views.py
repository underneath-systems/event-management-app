from django.shortcuts import render,redirect
from django.views.generic import View
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from events_operations.models import Event
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from events_operations.forms import eventForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# import requests 

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
		return redirect('events_operations:details')
	return render(request, 'event/event_form.html', {'form':form})


def event_delete(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.method == 'POST':
		event.delete()
		return redirect('events_operations:details')
	return render(request, 'event/event_delete.html', {'event':event})

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html", {
        "results": results,
        "query": query
    })

def write_organizer(request, idEvent):
    p = get_object_or_404(Question, pk=idEvent)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))




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



class StaffEvent(SuccessMessageMixin, DeleteView): 
    model = Event
    form = Event
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Staff asignado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
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

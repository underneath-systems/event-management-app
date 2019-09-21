from django.shortcuts import render,redirect
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from events_operations.models import Event
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from events_operations.forms import eventForm

def event_create(request):
	if request.method == 'POST':
		form = eventForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('eventos')
	else:
		form = eventForm()
	return render(request, 'event/event_form.html', {'form':form})


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

class eventosListado(ListView): 
    model = Event


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
        return reverse('eventos') # Redireccionamos a la vista principal 'leer'
    # template = 'event/create2.html'
    # context = {'title': 'create event'}

    # def get(self, request):
    #     """
    #         Create a new event.
    #     """
    #     print("Creating event")
    #     return render(request, self.template, self.context)


class EventDetails(DetailView): 
    model = Event


class UpdateEvent(SuccessMessageMixin, UpdateView): 
    model = Event
    form = Event
    fields = "__all__"  
    success_message = 'Event Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class CancelEvent(SuccessMessageMixin, DeleteView): 
    model = Event
    form = Event
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Evento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'



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

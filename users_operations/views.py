from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse, reverse_lazy
from django.shortcuts import render,redirect
from events_operations.models import Event
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

# def event_create(request):
# 	if request.method == 'POST':
# 		form = eventForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('details')
# 	else:
# 		form = eventForm()
# 	return render(request, 'event/event_form.html', {'form':form})

# def event_update(request, event_id):
# 	event = Event.objects.get(pk=event_id)
# 	if request.method == 'GET':
# 		form = eventForm(instance=event)
# 	else:
# 		form = eventForm(request.POST, instance=event)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('events_operations:details')
# 	return render(request, 'event/event_form.html', {'form':form})


# def event_delete(request, event_id):
# 	event = Event.objects.get(pk=event_id)
# 	if request.method == 'POST':
# 		event.delete()
# 		return redirect('events_operations:details')
# 	return render(request, 'event/event_delete.html', {'event':event})





# class eventsList(ListView):
#     model = Event
#     template_name = 'event/details.html'
#     # paginate_by = 2
#     ordering = ['id']


    
#     model = Event
#     form_class = eventForm
#     template_name = 'event/event_form.html'
#     # fields = "__all__"
#     success_message = 'Evento Creado Correctamente !'
#     def get_success_url(self):
#         return reverse('details')


# class EventDetails(DetailView): 
#     model = Event


# class UpdateEvent(UpdateView): 
#     model = Event
#     form_class = eventForm
#     template_name = 'event/event_form.html'
#     success_url = reverse_lazy('events_operations:details')
#     # success_message = 'Evento Actualizado Correctamente !'
#     # def get_success_url(self):
#     #     return reverse('details')


# class CancelEvent(DeleteView):
# 	model = Event
# 	template_name = 'event/event_delete.html'
# 	success_url = reverse_lazy('details')


# class TagEvent(SuccessMessageMixin, DeleteView): 
#     model = Event
#     form = Event
#     fields = "__all__"     

#     # Redireccionamos a la página principal luego de eliminar un registro o postre
#     def get_success_url(self): 
#         success_message = 'Evento Etiquetado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
#         messages.success (self.request, (success_message))       
#         return reverse('events') # Redireccionamos a la vista principal 'leer'



# class StaffEvent(SuccessMessageMixin, DeleteView): 
#     model = Event
#     form = Event
#     fields = "__all__"     

#     # Redireccionamos a la página principal luego de eliminar un registro o postre
#     def get_success_url(self): 
#         success_message = 'Staff asignado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
#         messages.success (self.request, (success_message))       
#         return reverse('events') # Redireccionamos a la vista principal 'leer'




# class CancelInvitation(SuccessMessageMixin, DeleteView): 
#     model = Event
#     form = Event
#     fields = "__all__"     

#     # Redireccionamos a la página principal luego de eliminar un registro o postre
#     def get_success_url(self): 
#         success_message = 'Invitacion cancelada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
#         messages.success (self.request, (success_message))       
#         return reverse('events') # Redireccionamos a la vista principal 'leer'

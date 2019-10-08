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
<<<<<<< HEAD
=======
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
>>>>>>> 15534af6033dfbb4029909f50aa551500120a536

class mainUsers(View):
    template = 'users/index.html'
    context = {'title': 'Main users page'}

    def get(self, request):
        """
            Main users page.
        """
        print("Main users page request")
        return render(request, self.template, self.context)

<<<<<<< HEAD
=======
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
                form = eventForm()
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






>>>>>>> 15534af6033dfbb4029909f50aa551500120a536
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


<<<<<<< HEAD
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
=======
>>>>>>> 15534af6033dfbb4029909f50aa551500120a536

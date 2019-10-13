from django import forms

from events_operations.models import *
from users_operations.models import User

class eventForm(forms.ModelForm):

        class Meta:
                model = Event

                fields = [
                        'name',
                        'description',
                        'organizer',
                        'start_date_time',
                        'end_date_time',
                        'address',
                        'attendees_list',
                        'staff_list',
                        'tag',
                        'capacity'
                ]
                labels = {
                        'name': 'Nombre',
                        'description': 'Descripcion',
                        'organizer': 'Organizador',
                        'start_date_time': 'Fecha de Inicio',
                        'end_date_time':'Fecha de fin',
                        'address': 'Direccion',
                        'attendees_list':'Lista_asistentes',
                        'staff_list':'Lista_staff',
                        'tag':'Etiquetas',
                        'capacity':'Capacidad_maxima'
                }
                widgets = {
                        'name': forms.TextInput(attrs={'class':'form-control'}),
                        'description': forms.TextInput(attrs={'class':'form-control'}),
                        'organizer': forms.Select(attrs={'class':'form-control'}),
                        'start_date_time': forms.SelectDateWidget(),
                        'end_date_time': forms.SelectDateWidget(attrs={'class':'form-control'}),
                        'address': forms.TextInput(attrs={'class':'form-control'}),
                        'attendees_list': forms.SelectMultiple(attrs={'class':'form-control'}),
                        'staff_list': forms.SelectMultiple(attrs={'class':'form-control'}),
                        'tag': forms.SelectMultiple(attrs={'class':'form-control'}),
                        'capacity': forms.NumberInput(attrs={'min':0,'max': '100'}),
                }

                def clean(self):
                        cleaned_data = self.cleaned_data
                        print(cleaned_data)
                        capacity = Event.capacity
                        attendees_num = Event.attendees_list.count
                        if self.capacity == self.capacity:
                                msg = "Must put 'help' in subject when cc'ing yourself."
                                self.add_error('capacity', msg)
                                raise ValidationError('Capacidad maxima del evento excedida!')



class sendInviteForm(forms.ModelForm):
        class Meta:
                model = User
                # fields = '__all__'
                # widgets = {'__all__':'required'}
                fields = [
                        'email',
                ]
                labels = {
                        'email': 'Invitado',
                }
                # widgets = {
                #         'email': forms.SelectMultiple(attrs={'class':'form-control'}),
                # }



class tagForm(forms.ModelForm):
        class Meta:
                model = Tag
                fields = [
                        'name'
                ]
                labels = {
                        'name':'Nombre'
                }
                widgets = {
                        'name': forms.TextInput(attrs={'class':'form-control'}),
                }

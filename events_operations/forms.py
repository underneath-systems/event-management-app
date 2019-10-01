from django import forms

from events_operations.models import *


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
			'capacity': forms.NumberInput(attrs={'class':'form-control'}),
		}

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

from django import forms

from events_operations.models import Event


class eventForm(forms.ModelForm):

	class Meta:
		model = Event

		fields = [
			'name',
			'organizer',
			'start_date_time',
			'end_date_time',
			'address',
		]
		labels = {
			'name': 'Nombre',
			'organizer': 'Organizador',
			'start_date_time': 'Fecha de Inicio',
			'end_date_time':'Fecha de fin',
			'address': 'Direccion',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'organizer': forms.Select(attrs={'class':'form-control'}),
			'start_date_time': forms.TextInput(attrs={'class':'form-control'}),
			'end_date_time': forms.TextInput(attrs={'class':'form-control'}),
			'address': forms.TextInput(attrs={'class':'form-control'}),
		}

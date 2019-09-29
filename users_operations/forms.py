from django import forms

from users_operations.models import * 

class attendeesForm(forms.ModelForm):

	class Meta:
		model = Attendees

		fields = [
                'name',
                'email',
                'password',
			    'photo_id',
                'qr_code',
		]
		labels = {
			    'name': 'Nombre',
                'email': 'Email',
                'password': 'Contrasena',
			    'photo_id': 'Fotografia',
                'qr_code':'Codigo QR'
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'password': forms.PasswordInput(attrs={'class':'form-control'}),
			'photo_id': forms.FileInput(attrs={'class':'form-control'}),
			'qr_code': forms.TextInput(attrs={'class':'form-control'}),
		}



class organizerForm(forms.ModelForm):

	class Meta:
		model = Organizer

		fields = [
                'name',
                'email',
                'password',
			    'photo_id',
                'phone',
		]
		labels = {
			    'name': 'Nombre',
                'email': 'Email',
                'password': 'Contrasena',
			    'photo_id': 'Fotografia',
                'phone':'Telefono'
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'password': forms.PasswordInput(attrs={'class':'form-control'}),
			'photo_id': forms.FileInput(attrs={'class':'form-control'}),
			'phone': forms.NumberInput(attrs={'class':'form-control'}),
		}


class staffForm(forms.ModelForm):
	class Meta:
		model = Staff
		fields = [
                'name',
                'email',
                'password',
			    'photo_id',
                'working_hours',
		]
		labels = {
			    'name': 'Nombre',
                'email': 'Email',
                'password': 'Contrasena',
			    'photo_id': 'Fotografia',
                'working_hours':'Horas disponibles'
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'password': forms.PasswordInput(attrs={'class':'form-control'}),
			'photo_id': forms.FileInput(attrs={'class':'form-control'}),
			'working_hours': forms.NumberInput(attrs={'class':'form-control'}),
		}



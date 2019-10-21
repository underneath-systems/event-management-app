from django import forms
from .admin import UserCreationForm
from users_operations.models import *

class attendeesForm(UserCreationForm):
        class Meta:
                model = Attendees

                fields = [
                        'email',
                        'password1',
                        'password2',
                        'first_name',
                        'last_name',
			'photo_id',
                        'qr_code',
                        ]
                labels = {
                        
                        'first_name': 'Nombre',
                        'last_name': 'Apellidos',
			'photo_id': 'Fotografia',
                        'qr_code':'Codigo QR'
                }
                widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control'}),
                        'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'password1': forms.PasswordInput(attrs={'class':'form-control'}),
                        'password2': forms.PasswordInput(attrs={'class':'form-control'}),
			'photo_id': forms.FileInput(attrs={'class':'form-control'}),
			'qr_code': forms.TextInput(attrs={'class':'form-control'}),
                }


class organizerForm(UserCreationForm):
        class Meta:
                model = Organizer

                fields = [
                        'email',
                        'password1',
                        'password2',
                        'first_name',
                        'last_name',
			'photo_id',
                        'phone',
		]
                labels = {
                        'email': 'Correo electronico',
                        'password1': 'Contrasena',
                        'password2': 'Confirmar contrasena',
                        'firs_name': 'Nombre',
                        'last_name': 'Apellidos',
                        'photo_id': 'Fotografia',
                        'phone':'Telefono'
                }
                widgets = {
                        'first_name': forms.TextInput(attrs={'class':'form-control'}),
                        'last_name': forms.TextInput(attrs={'class':'form-control'}),
                        'email': forms.EmailInput(attrs={'class':'form-control'}),
                        'password1': forms.PasswordInput(attrs={'class':'form-control'}),
                        'password2': forms.PasswordInput(attrs={'class':'form-control'}),
                        'photo_id': forms.FileInput(attrs={'class':'form-control'}),
                        'phone': forms.NumberInput(attrs={'class':'form-control'}),
                }



class staffForm(UserCreationForm):
        class Meta:
                model = Staff_event

                fields = [
                        'email',
                        'password1',
                        'password2',
                        'first_name',
                        'last_name',
			'photo_id',
                        'working_hours',
                ]
                labels = {
                        'email': 'Correo electronico',
                        'password1': 'Contrasena',
                        'password2': 'Confirmar contrasena',
                        'firs_name': 'Nombre',
                        'last_name': 'Apellidos',
                        'photo_id': 'Fotografia',
                        'working_hours': 'Horas disponibles',
                }
                widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control'}),
                        'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'password1': forms.PasswordInput(attrs={'class':'form-control'}),
                        'password2': forms.PasswordInput(attrs={'class':'form-control'}),
			'photo_id': forms.FileInput(attrs={'class':'form-control'}),
			'working_hours': forms.NumberInput(attrs={'class':'form-control'}),
                }

                


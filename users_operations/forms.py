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
                        'entity',
                        ]
                labels = {
                        
                        'first_name': 'Nombre',
                        'last_name': 'Apellidos',
			'photo_id': 'Fotografia',
                        'entity':'Entidad academica'
                }
                widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control'}),
                        'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'password1': forms.PasswordInput(attrs={'class':'form-control'}),
                        'password2': forms.PasswordInput(attrs={'class':'form-control'}),
			'photo_id': forms.FileInput(attrs={'class':'form-control'}),
			'entity': forms.Select(attrs={'class':'form-control'}),
                }


class organizerForm(forms.ModelForm):
        class Meta:
                model = Organizer 

                fields = [
                        'email',
                        'first_name',
                        'last_name',
		]
                labels = {
                        'email': 'Correo electronico',
                        'first_name': 'Nombre',
                        'last_name': 'Apellidos',
                }
                widgets = {
                        'first_name': forms.TextInput(attrs={'class':'form-control'}),
                        'last_name': forms.TextInput(attrs={'class':'form-control'}),
                        'email': forms.EmailInput(attrs={'class':'form-control'}),
                }
                
        def clean_email(self):
                email = self.cleaned_data.get('email')
                qs = User.objects.filter(email=email)
                if qs.exists():
                        raise forms.ValidationError("Correo ya registrado")
                return email

        def save(self, commit=True):
        # Save the provided password in hashed format
                user = super(organizerForm, self).save(commit=False)
                if commit:
                        user.save()
                return user


class staffForm(forms.ModelForm):
        class Meta:
                model = Staff_event

                fields = [
                        'email',
                        'first_name',
                        'last_name',
		]
                labels = {
                        'email': 'Correo electronico',
                        'first_name': 'Nombre',
                        'last_name': 'Apellidos',
                }
                widgets = {
                        'first_name': forms.TextInput(attrs={'class':'form-control'}),
                        'last_name': forms.TextInput(attrs={'class':'form-control'}),
                        'email': forms.EmailInput(attrs={'class':'form-control'}),
                }
                
        def clean_email(self):
                email = self.cleaned_data.get('email')
                qs = User.objects.filter(email=email)
                if qs.exists():
                        raise forms.ValidationError("Correo ya registrado")
                return email

        def save(self, commit=True):
        # Save the provided password in hashed format
                user = super(staffForm, self).save(commit=False)
                if commit:
                        user.save()
                return user
                


from django import forms

from events_operations.models import *
from users_operations.models import User
import datetime
from events_operations.get_username import get_username
now = datetime.datetime.now().year
current_month = datetime.datetime.now().month

YEAR_CHOICES = [str(now), str(now+1)]
MONTHS =  {
  1: "Enero",
  2: "Febrero",
  3: "Marzo",
  4: "Abril",
  5: "Mayo",
  6: "Junio",
  7: "Julio",
  8: "Agosto",
  9: "Septiembre",
  10: "Octubre",
  11: "Noviembre",
  12: "Diciembre",
}

AVAILABLE_MONTHS = {}

for key_month in MONTHS:
        if key_month == current_month:
                for month in range (current_month,13):
                        AVAILABLE_MONTHS[month] = MONTHS[month]


class eventForm(forms.ModelForm):

        class Meta:
                model = Event
                cur_year = datetime.datetime.today().year
                year_range = tuple([i for i in range(cur_year - 2, cur_year + 2)])

                req = get_username()
                print ("Your username is: %s" % (req))

                def clean_date(self):
                        start_date_time = self.start_date_time['start_date_time']
                        if start_date_time < datetime.date.today():
                                raise forms.ValidationError("The date cannot be in the past!")
                        return start_date_time

                def get_season():
                        import datetime
                        """
                        Returns the event's specific season
                        """
                        if 1 <= datetime.date.today().month < 4:
                                return "Winter event"


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
                        'start_date_time': forms.SelectDateWidget(years=YEAR_CHOICES, months=AVAILABLE_MONTHS, attrs={'class': 'datepicker'} ),
                        'end_date_time': forms.SelectDateWidget(years=YEAR_CHOICES, months=AVAILABLE_MONTHS),
                        'address': forms.TextInput(attrs={'class':'form-control'}),
                        'attendees_list': forms.SelectMultiple(attrs={'class':'form-control'}),
                        'staff_list': forms.SelectMultiple(attrs={'class':'form-control'}),
                        'tag': forms.SelectMultiple(attrs={'class':'form-control'}),
                        'capacity': forms.NumberInput(attrs={'min':0,'max': '100'}),
                }

        def __init__(self, *args, **kwargs):
                super(eventForm, self).__init__(*args, **kwargs)
                self.fields['organizer'].disabled = False
                #self.fields['organizer'].initial = 'juanc.23.g@enallt.unam.mx'


        """def clean(self):
                cleaned_data = self.cleaned_data
                print(cleaned_data)
                capacity = Event.capacity
                attendees_num = Event.attendees_list.count
                if self.capacity == self.capacity:
                        msg = "Must put 'help' in subject when cc'ing yourself."
                        self.add_error('capacity', msg)
                        raise ValidationError('Capacidad maxima del evento excedida!')"""



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

class assignStaffForm(forms.ModelForm):
        class Meta:
                model = Event
                fields = [
                        'staff_list',
                ]
                labels = {
                        'staff_list':'Lista_staff',
                }
                widgets = {
                        'staff_list': forms.SelectMultiple(attrs={'class':'form-control'}),
                }


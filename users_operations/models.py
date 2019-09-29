from django.db import models
# from events_operations.models import Event
# Create your models here.


class User(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    email = models.EmailField(primary_key=True)
    password = models.CharField(null=False, blank=False, max_length=20)
    photo_id = models.ImageField(null=True, blank=True, upload_to='media')
    def __str__(self):
        return '{} {}'.format(self.name, self.email)
# class attendees(user):
#     event = models.ManyToManyField(Event)

class Attendees(User):
    qr_code = models.CharField(default = '', null = False, blank = False, max_length=20)
    def __str__(self):
        return '{} {}'.format(self.name, self.email)


class Organizer(User):
    # idOrganizer = models.UUIDField(default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return '{} {}'.format(self.name, self.email)


class Staff(User):
    working_hours = models.IntegerField(default=8)
    def __str__(self):
        return '{} {}'.format(self.name, self.email)

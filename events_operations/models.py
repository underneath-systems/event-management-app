from django.contrib.postgres.fields import ArrayField
from django.db import models
from uuid import uuid4
import uuid
from users_operations.models import Attendees, Organizer,Staff_event, User
import datetime
from datetime import datetime
from events_operations.get_username import get_username

class Tag(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    def __str__(self):
        return '{}'.format(self.name)


class Event(models.Model):
    # def save(self, *args, **kwargs):
    #     req = get_username()
    #     print ("Your model username is: %s" % (req))
    # idEvent = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=20)
    description = models.CharField(null=True, blank=True, max_length=30)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(default=datetime.now, null=False, blank=False)
    end_date_time = models.DateTimeField(default=datetime.now, null=False, blank=False)
    address = models.CharField(max_length=100)
    attendees_list = models.ManyToManyField(Attendees, blank=True)
    staff_list = models.ManyToManyField(Staff_event, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    capacity = models.IntegerField(default=10)
    # eventCover = models.ImageField(upload_to='tmp')
    def __str__(self):
            return '{} {}'.format(self.name, self.organizer)
    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        # can use the below method also
        # queryset = self.__class__.objects.all()   
        return queryset


class Assist(models.Model):
    qr_code = models.ImageField(null=False, blank=False)
    #models.CharField(default = '', null = False, blank = False, max_length=20)
    user = models.ManyToManyField(User)
    event = models.ManyToManyField(Event)
    confirm = models.BooleanField(default = False)
    invitation = models.BooleanField()
    def __str__(self):
            return '{} {}'.format(self.user, self.event)

from django.contrib.postgres.fields import ArrayField
from django.db import models
from uuid import uuid4
import uuid
from users_operations.models import Attendees, Organizer,Staff


class Tag(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    def __str__(self):
        return '{}'.format(self.name)


class Event(models.Model):
    # idEvent = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=20)
    description = models.CharField(null=True, blank=True, max_length=30)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(null=False, blank=False)
    end_date_time = models.DateTimeField(null=False, blank=False)
    address = models.CharField(max_length=100)
    attendees_list = models.ManyToManyField(Attendees)
    staff_list = models.ManyToManyField(Staff)
    tag = models.ManyToManyField(Tag)
    capacity = models.IntegerField(default=10)
    # eventCover = models.ImageField(upload_to='tmp')
    def __str__(self):
            return '{} {}'.format(self.name, self.organizer)
    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        # can use the below method also
        # queryset = self.__class__.objects.all()   
        return queryset

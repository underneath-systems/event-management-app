from django.contrib.postgres.fields import ArrayField
from django.db import models
from uuid import uuid4
import uuid
from users_operations.models import Attendees, Organizer,Staff


# Create your models here.
# class Organizer(models.Model):
#     # idOrganizer = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=20)
#     rfc = models.CharField(max_length=20)
#     email = models.EmailField(primary_key=True)
#     phone = models.CharField(max_length=20)
#     def __str__(self):
#             return '{} {}'.format(self.name, self.email)
class Tag(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)

class Event(models.Model):
    # idEvent = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=20)
    description = models.CharField(null=True, blank=True, max_length=30)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(null=False, blank=False)
    end_date_time = models.DateTimeField(null=False, blank=False)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    address = models.CharField(max_length=100)
    attendees_list = models.ManyToManyField(Attendees)
    staff_list = models.ManyToManyField(Staff)
    tag = models.ManyToManyField(Tag)
    capacity = models.IntegerField(default=10)
    # eventCover = models.ImageField(upload_to='tmp')
    # slug = models.SlugField(max_length=40)
    def __str__(self):
            return '{} {}'.format(self.name, self.organizer)

# class Staff(models.Model):
#     event = models.ManyToManyField(Event)
#     name = models.CharField(max_length=20)


# class Tag(models.Model):
#     idTag = models.ManyToManyField(Event)
#     name = models.CharField(max_length=20)

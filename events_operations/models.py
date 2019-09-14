from django.db import models
from uuid import uuid4
import uuid
# from events_operations import models


# Create your models here.
class Organizer(models.Model):
    idOrganizer = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    rfc = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Event(models.Model):
    idEvent = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    organizer = models.CharField(max_length=30)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    address = models.CharField(max_length=100)
    eventCover = models.ImageField(upload_to='tmp')

class Staff(models.Model):
    idEmployee = models.ManyToManyField(Event)
    name = models.CharField(max_length=20)

class Category(models.Model):
    idCategory = models.ManyToManyField(Event)
    name = models.CharField(max_length=20)

class Tag(models.Model):
    idTag = models.ManyToManyField(Event)
    name = models.CharField(max_length=20)

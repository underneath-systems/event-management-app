from django.contrib import admin

# Register your models here.
# from .models import Organizers, Event, Staff, Category, Tag
# from events_operations.models import Organizer, Event
# , Staff, Category, Tag
from events_operations.models import Assist, Event, Tag

admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(Assist)

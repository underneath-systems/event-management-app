from django.contrib import admin

# Register your models here.
# from .models import Organizers, Event, Staff, Category, Tag
# from events_operations.models import Organizer, Event
# , Staff, Category, Tag
from events_operations.models import Organizer, Event, Staff, Tag

admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Staff)
# admin.site.register(Category)
admin.site.register(Tag)

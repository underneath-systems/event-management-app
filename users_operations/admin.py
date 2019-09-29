from django.contrib import admin
from users_operations.models import User,Attendees, Organizer, Staff 
# Register your models here.
admin.site.register(User)
admin.site.register(Attendees)
admin.site.register(Organizer)
admin.site.register(Staff)


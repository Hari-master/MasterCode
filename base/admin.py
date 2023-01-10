from django.contrib import admin
from .models import Message, Room, Topic, User


admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)

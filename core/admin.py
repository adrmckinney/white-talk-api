from django.contrib import admin
from core.models import User, SessionRegistrant, Session, Announcement

admin.site.register(User)
admin.site.register(SessionRegistrant)
admin.site.register(Session)
admin.site.register(Announcement)

from django.contrib import admin
from .models import Application
from .models import ContactMessage

admin.site.register(Application)
admin.site.register(ContactMessage)


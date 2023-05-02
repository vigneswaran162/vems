from django.contrib import admin

from .models import *

class admin_register(admin.ModelAdmin):
    list_display=['eventname','fullname','email','phoneno','rollno','collegename','dept']


admin.site.register(events_year)
admin.site.register(upload_event)
admin.site.register(addevent)
admin.site.register(event_announcement)
admin.site.register(registerevent,admin_register)


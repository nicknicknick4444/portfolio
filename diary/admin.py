from django.contrib import admin
from .models import Entry, SendTime

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("title", {"fields":["title"]}),
        ("detail", {"fields":["detail"]}),
        ("user", {"fields":["user"]}),
        ("by", {"fields": ["by"]}),
        ("created", {"fields": ["created"]}),
        ("last_modified", {"fields":["last_modified"]}),
        ("date_for", {"fields":["date_for"]}),
        ]
    list_display = ("title", "detail", "user", "by", "created", "last_modified", "date_for")

class SendTimeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("send_time", {"fields":["send_time"]}),
        ]
    list_display = ("send_time",)
    
admin.site.register(Entry, EntryAdmin)
admin.site.register(SendTime, SendTimeAdmin)

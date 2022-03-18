from django.contrib import admin
from .models import Admonish, TweetLists

# Register your models here.

class AdmonishAdmin(admin.ModelAdmin):
    fieldsets = [
        ("adm_id", {"fields":["adm_id"]}),
        ("adm_term", {"fields":["adm_term"]}),
        ("adm_text", {"fields":["adm_text"]}),
        #("adm_seshn", {"":["adm_seshn"]})
        ]
    list_display = ("adm_id", "adm_term", "adm_text")

class TweetListsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("twe_dict", {"fields":["twe_dict"]}),
        ("twe_term", {"fields":["twe_term"]}),
        ("twe_seshn", {"fields":["twe_seshn"]}),
        ("twe_time", {"fields":["twe_time"]}),
        ]
    list_listplay = ("twe_seshn", "twe_term", "twe_time")

admin.site.register(Admonish, AdmonishAdmin)
admin.site.register(TweetLists, TweetListsAdmin)

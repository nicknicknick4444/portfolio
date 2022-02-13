from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Squaresy, Number, Exceppo, Scores, Times

# Register your models here.

class SquaresyAdmin(admin.ModelAdmin):
    fieldsets = [
        ("The Tixt", {"fields":["square_text"]}),
        ("The Numboure", {"fields":["number"]}),
        ]
    list_display = ("square_text", "number")

class ScoresAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {"fields":["namey"]}),
        ("Score", {"fields":["score"]}),
        ("Duration", {"fields":["duration"]}),
        ("Seconds", {"fields":["all_seconds"]}),
        ("Attempts", {"fields":["attempts"]}),
        ]
    list_display = ("namey", "score", "duration", "all_seconds", "attempts")

class TimesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Start Time", {"fields":["start_time"]}),
        ("Finish Time", {"fields":["finish_time"]}),
        ("Attempts", {"fields":["attempts"]}),
        ("Session Glab", {"fields":["sessiony"]}),
        ]
    list_display = ("start_time", "finish_time", "attempts", "sessiony")

class ExceppoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Exceppo", {"fields":["exceppy"]}),
        ("Session Glab", {"fields":["sessiony"]}),
        ]
    list_display = ("exceppy", "sessiony")

class NumberAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Main List", {"fields":["wardle"]}),
        ("Session Glab", {"fields":["sessiony"]}),
        ]
    list_display = ("wardle", "sessiony")

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ("session_key", "session_data")
    
    

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Squaresy, SquaresyAdmin)
admin.site.register(Number, NumberAdmin)
admin.site.register(Exceppo, ExceppoAdmin)
admin.site.register(Scores, ScoresAdmin)
admin.site.register(Times, TimesAdmin)
admin.site.register(Session, SessionAdmin)

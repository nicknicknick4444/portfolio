from django.contrib import admin
from .models import Scores

# Register your models here.

# class SquaresyAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("The Tixt", {"fields":["square_text"]}),
#         ("The Numboure", {"fields":["number"]}),
#         ]
#     list_display = ("square_text", "number")

class ScoresAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {"fields":["namey"]}),
        ("Score", {"fields":["score"]}),
        ("Duration", {"fields":["duration"]}),
        ("Seconds", {"fields":["all_seconds"]}),
        ("Attempts", {"fields":["attempts"]}),
        ]
    list_display = ("namey", "score", "duration", "all_seconds", "attempts")

#admin.site.register(Squaresy, SquaresyAdmin)
admin.site.register(Scores, ScoresAdmin)

from django.contrib import admin
from .models import Colour

# Register your models here.

class ColourAdmin(admin.ModelAdmin):
    fieldsets = [
        ("colour_name", {"fields":["colour_name"]}),
        ("colour_hex", {"fields":["colour_hex"]}),
        ]
    list_display = ("colour_name", "colour_hex")

admin.site.register(Colour, ColourAdmin)

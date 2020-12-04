from django.contrib import admin
from .models import Pet, Image

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

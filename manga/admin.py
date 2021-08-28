from django.contrib import admin

from django.contrib import admin
from .models import *

class FeedFileInline(admin.TabularInline):
    model = PageFile


class FeedAdmin(admin.ModelAdmin):
    inlines = [
        FeedFileInline,
    ]

admin.site.register(Chapter, FeedAdmin)
admin.site.register(Manga)
admin.site.register(Comment)
admin.site.register(PageFile)

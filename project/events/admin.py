from django.contrib import admin
from .models import Event, Comment

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_slug', 'event_author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'event_author')
    search_fields = ('event_title', 'event_body')
    prepopulated_fields = {'event_slug': ('event_title',)}
    raw_id_fields = ('event_author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'event', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')    
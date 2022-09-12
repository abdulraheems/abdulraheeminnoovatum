from django.contrib import admin
from .models import Website

# Register your models here.
admin.site.register(Website)

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('website_title', 'website_link', 'website_content')
    list_filter = ('created_on')
    search_fields = ('website_title', 'website_link')
    ordering = ('created_on')
from django.contrib.sitemaps import Sitemap
from .models import Event
class EventSitemap(Sitemap):
    changefreq = 'daily' # 'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'
    priority = 0.9
    
    def items(self):
        return Event.published.all()
    def lastmod(self, obj):
        return obj.updated
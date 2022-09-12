from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from main import views
from django.contrib.sitemaps.views import sitemap
from events.sitemaps import EventSitemap
from main.views import home, follow, unfollow, post, search, add_comment, add_subcomment

sitemaps = {
    'events': EventSitemap,
}

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='search/homepage.html')),
    path('search/', include('haystack.urls')),
    path('search/autocomplete/', views.AutocompleteView, name='autocomplete'),
    # app url configs
    #path('feeds/', include('main.urls')),
    path('user/', include('user.urls')),
    path('events/', include('events.urls', namespace='events')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),

    #main urls
    path('feeds/', home, name = 'home'),
    path('search', search, name='search'),
    path('follow', follow),
    path('unfollow', unfollow),
    path('post', post),
    path('add_comment', add_comment),
    path('add_subcomment', add_subcomment),

    #projects

    path('projects/', TemplateView.as_view(template_name='projects/index.html')),
    path('about/', TemplateView.as_view(template_name='projects/about.html')),
    path('impact/', TemplateView.as_view(template_name='projects/impact.html')),
    path('testimony/', TemplateView.as_view(template_name='projects/testimony.html')),
    path('contact/', TemplateView.as_view(template_name='projects/contact.html')),
    path('fun/', TemplateView.as_view(template_name='projects/fun.html')),

    #projectlist
    path('machinelearningprojects/', TemplateView.as_view(template_name='projects/projectlist/machinelearningprojects.html')),
    path('java/', TemplateView.as_view(template_name='projects/projectlist/java.html')),
    path('dotnet/', TemplateView.as_view(template_name='projects/projectlist/dotnet.html')),
    path('php/', TemplateView.as_view(template_name='projects/projectlist/php.html')),
    path('iot/', TemplateView.as_view(template_name='projects/projectlist/iot.html')),
    path('android/', TemplateView.as_view(template_name='projects/projectlist/android.html')),
    
]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

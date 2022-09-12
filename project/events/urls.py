from django.urls import path
from . import views

app_name = 'events'

urlpatterns=[
    path('',views.event_list,name="event_list"),
    path('<slug:event>/',views.event_detail,name="event_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
    path('tag/<slug:tag_slug>/',views.event_list, name='event_tag'),
    
]
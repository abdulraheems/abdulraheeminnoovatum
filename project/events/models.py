# models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

# post model
class Event(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    

    event_title = models.CharField(max_length=250)
    event_slug = models.SlugField(max_length=250, unique_for_date='publish')
    event_author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    event_body = RichTextUploadingField() 
    event_featured_image = models.ImageField(upload_to='featured_image/%Y/%m/%d/',default='blank-profile-picture.png') 
    event_start_date = models.DateTimeField(max_length=250)
    event_end_date = models.DateTimeField(max_length=250)
    event_start_time = models.TimeField(max_length=250, blank=True)
    event_end_time = models.TimeField(max_length=250, blank=True)
    event_registration_deadline = models.DateTimeField(auto_now=True)
    event_venue = models.CharField(max_length=250)
    event_address = models.TextField()
    event_city = models.CharField(max_length=250)
    event_state = models.CharField(max_length=250)
    event_country = models.CharField(max_length=250)
    event_ticket_option = models.CharField(max_length=250)
    event_onlinepayment_option = models.CharField(max_length=250)
    event_event_images = models.ImageField(upload_to='event_images', default='blank-profile-picture.png')
    event_organizer_name = models.CharField(max_length=250)
    event_sponsors = models.CharField(max_length=250)
    event_event_type = models.CharField(max_length=250)
    event_event_topic = models.CharField(max_length=250)
    event_listing_privacy = models.CharField(max_length=250,default='public')
    event_remaining_tickets = models.CharField(max_length=250)


    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags = TaggableManager() 


    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.event_title

    objects = models.Manager() 
    published = PublishedManager() 

    def get_absolute_url(self):
        return reverse('events:event_detail',args=[self.slug])   

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True) 
        

class Comment(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(max_length=50)
    email=models.EmailField()
    parent=models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.body
    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)

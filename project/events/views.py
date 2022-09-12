from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Comment
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q
from django.views.generic import ListView, DetailView
#autocomplete urls
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from haystack.query import SearchQuerySet
import json
from django.http import HttpResponse


class EventList(ListView):
    model = Event
    # paginate_by="5"
    queryset=Event.published.all()
    context_object_name = "events"
    template_name = "events/event_list.html"

def event_list(request, tag_slug=None):
    events = Event.published.all()

     # post tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        events = events.filter(tags__in=[tag])
    
    # search
    query = request.GET.get("q")
    if query:
        events=Event.published.filter(Q(event_title__icontains=query) | Q(tags__name__icontains=query)).distinct()
            
    
    paginator = Paginator(events, 10) # 10 posts in each page
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        events = paginator.page(paginator.num_pages)
    
   
        
    return render(request,'events/event_list.html',{'events':events, page:'pages', 'tag':tag})


class EventDetail(DetailView):
    model = Event
    context_object_name = "event"
    template_name = "events/event_detail.html"

def event_detail(request, event):
    event=get_object_or_404(Event,slug=event,status='published')

    # List of active comments for this post
    comments = event.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.event = event
            # Save the comment to the database
            new_comment.save()
            return redirect(event.get_absolute_url()+'#'+str(new_comment.id))
    else:
        comment_form = CommentForm()

    # List of similar posts
    event_tags_ids = event.tags.values_list('id', flat=True)
    similar_events = Event.published.filter(tags__in=event_tags_ids).exclude(id=event.id)
    similar_events = similar_events.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    
    return render(request, 'events/event_detail.html',{'event':event,'comments': comments,'comment_form':comment_form,'similar_events':similar_events})


# handling reply, reply view
def reply_page(request):
    if request.method == "POST":

        form = CommentForm(request.POST)
        
        # print(form)

        if form.is_valid():
            event_id = request.POST.get('event_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            event_url = request.POST.get('event_url')  # from hidden input

            print(event_id)
            print(parent_id)
            print(event_url)


            reply = form.save(commit=False)
    
            reply.event = Event(id=event_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(event_url+'#'+str(reply.id))

    return redirect("/")



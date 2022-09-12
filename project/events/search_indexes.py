import datetime
from django.utils import timezone
from haystack import indexes
from .models import Event

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    event_body = indexes.CharField(model_attr='event_body', faceted=True, boost=1.125)
    event_venue = indexes.CharField(model_attr='event_venue')
    event_address = indexes.CharField(model_attr='event_address')
    event_organizer_name = indexes.CharField(model_attr='event_organizer_name')
    event_sponsors = indexes.CharField(model_attr='event_sponsors')
    event_event_type = indexes.CharField(model_attr='event_event_type')
    event_event_topic = indexes.CharField(model_attr='event_event_topic')
    
    
    # for auto complete
    event_title = indexes.EdgeNgramField(model_attr='event_title')

    # Spelling suggestions
    suggestions = indexes.FacetCharField()
                             
    def get_model(self):
        return Event
    
    def index_queryset(self, using=None):
        #return self.get_model().objects.all()
        return self.get_model().objects.filter(created__lte=timezone.now())
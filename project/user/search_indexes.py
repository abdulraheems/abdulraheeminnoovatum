import datetime
from django.utils import timezone
from haystack import indexes
from .models import Profile

class ProfileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #title = indexes.CharField(model_attr='title', faceted=True, boost=1.125)
    profile_about_me = indexes.CharField(model_attr='profile_about_me')
    #user = indexes.EdgeNgramField(model_attr='user')

    # Spelling suggestions
    suggestions = indexes.FacetCharField()
                             
    def get_model(self):
        return Profile
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
        #return self.get_model().objects.filter(created_at__lte=timezone.now())
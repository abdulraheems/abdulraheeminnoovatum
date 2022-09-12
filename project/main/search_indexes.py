import datetime
from django.utils import timezone
from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    post_text = indexes.CharField(model_attr='post_text', faceted=True)
    user = indexes.EdgeNgramField(model_attr='user')

    # Spelling suggestions
    suggestions = indexes.FacetCharField()
                             
    def get_model(self):
        return Post
    
    def index_queryset(self, using=None):
        #return self.get_model().objects.all()
        return self.get_model().objects.filter(created_at__lte=timezone.now())
import datetime
from haystack import indexes
from .models import Website

class WebsiteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #title = indexes.CharField(model_attr='title', faceted=True)
    website_link = indexes.CharField(model_attr='website_link', faceted=True)
    website_content = indexes.CharField(model_attr='website_content', faceted=True)

    website_title = indexes.EdgeNgramField(model_attr='website_title')

                             
    def get_model(self):
        return Website  
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
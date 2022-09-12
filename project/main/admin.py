from django.contrib import admin
# from .models import Comment, SubComment
# admin.site.register(Comment)
# admin.site.register(SubComment)
from .models import Post

admin.site.register(Post)
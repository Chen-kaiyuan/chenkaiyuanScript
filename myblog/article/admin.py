from django.contrib import admin
from article.models import Article
from article.models import Post
#from .models import Post, Category, Tag

import sys
reload(sys)
# Register your models here.

#admin.site.register(Article)
admin.site.register(Post)

sys.setdefaultencoding('utf-8')

#admin.site.register(Post)
#admin.site.register(Category)
#admin.site.register(Tag)
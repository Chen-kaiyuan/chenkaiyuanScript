from django.contrib import admin
from article.models import Article
#from .models import Post, Category, Tag

import sys
reload(sys)
# Register your models here.

admin.site.register(Article)

sys.setdefaultencoding('utf8')

#admin.site.register(Post)
#admin.site.register(Category)
#admin.site.register(Tag)
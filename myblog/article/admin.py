from django.contrib import admin
from article.models import Article

import sys
reload(sys)
# Register your models here.

admin.site.register(Article)

sys.setdefaultencoding('utf8')
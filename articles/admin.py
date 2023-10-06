from django.contrib import admin

from articles.models import Articles, Comment

# Register your models here.
admin.site.register(Articles)
admin.site.register(Comment)
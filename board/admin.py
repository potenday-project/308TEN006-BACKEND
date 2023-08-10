from django.contrib import admin
from .models import Memos, Comment, Tag

admin.site.register(Memos)
admin.site.register(Comment)
admin.site.register(Tag)
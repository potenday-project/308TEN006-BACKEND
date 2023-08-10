from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from member.models import Profile
import re


class Memos(models.Model):
    category = models.TextField(verbose_name='카테고리', max_length = 50, null=True, default='전체')
    images = models.ImageField(verbose_name='이미지', blank=True, upload_to="images", null=True, default='')
    title = models.TextField(verbose_name='제목', max_length = 150, db_column='제목', null=True, default='')
    text = models.TextField(verbose_name='내용', max_length = 500, db_column='내용', null=True, default='')
    experience_date = models.DateField(verbose_name='체험 날짜', null=True, default='1999-12-31')
    price = models.DecimalField(verbose_name='가격', max_digits=10, decimal_places=0, null=True, default=0)
    district = models.TextField(verbose_name='지역', max_length = 50, null=True, default='')
    platform = models.TextField(verbose_name='플랫폼', max_length = 150, null=True, default='')
    tag_text = models.TextField(verbose_name='Tag', max_length = 150, null=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    create_date = models.DateTimeField()
    name = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.tag_text)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(tag_name=t)
            self.tag_set.add(tag)
            
    def generate(self):
        self.create_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
        
    @property
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Memos, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_writer = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)

    class Meta:
        ordering = ['-id']
            
    def __str__(self):
        return str(self.comment_writer)

class Tag(models.Model):
    tag_name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.tag_name

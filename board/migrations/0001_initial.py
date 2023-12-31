# Generated by Django 4.2.4 on 2023-08-12 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=140, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(default='전체', max_length=50, null=True, verbose_name='카테고리')),
                ('images', models.ImageField(blank=True, default='', null=True, upload_to='images', verbose_name='이미지')),
                ('title', models.TextField(db_column='제목', default='', max_length=150, null=True, verbose_name='제목')),
                ('text', models.TextField(db_column='내용', default='', max_length=500, null=True, verbose_name='내용')),
                ('experience_date', models.DateField(default='1999-12-31', null=True, verbose_name='체험 날짜')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True, verbose_name='가격')),
                ('district', models.TextField(default='', max_length=50, null=True, verbose_name='지역')),
                ('platform', models.TextField(default='', max_length=150, null=True, verbose_name='플랫폼')),
                ('tag_text', models.TextField(max_length=150, null=True, verbose_name='Tag')),
                ('create_date', models.DateTimeField()),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag_set', models.ManyToManyField(blank=True, to='board.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_contents', models.CharField(max_length=200)),
                ('comment_writer_img', models.ImageField(blank=True, upload_to='comment_images')),
                ('comment_writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.profile')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.memos')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

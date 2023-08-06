# Generated by Django 4.2.4 on 2023-08-06 06:53

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
            name='Tag2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name2', models.CharField(max_length=140, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(db_column='내용', max_length=150)),
                ('update_date', models.DateTimeField()),
                ('text2', models.TextField(max_length=150, null=True)),
                ('text3', models.TextField(max_length=150, null=True)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag_set', models.ManyToManyField(blank=True, to='board.tag')),
                ('tag_set2', models.ManyToManyField(blank=True, to='board.tag2')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_contents', models.CharField(max_length=200)),
                ('comment_writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.profile')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.memos')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

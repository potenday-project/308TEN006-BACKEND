# Generated by Django 4.2.4 on 2023-08-13 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_memos_keyword_access_memos_keyword_amenities_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memos',
            name='keyword_access',
        ),
        migrations.RemoveField(
            model_name='memos',
            name='keyword_amenities',
        ),
        migrations.RemoveField(
            model_name='memos',
            name='keyword_price',
        ),
    ]

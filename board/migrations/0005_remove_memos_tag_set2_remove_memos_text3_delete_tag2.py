# Generated by Django 4.2.4 on 2023-08-10 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_memos_text2_memos_tag_text_alter_memos_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memos',
            name='tag_set2',
        ),
        migrations.RemoveField(
            model_name='memos',
            name='text3',
        ),
        migrations.DeleteModel(
            name='Tag2',
        ),
    ]

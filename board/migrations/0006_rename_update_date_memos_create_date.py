# Generated by Django 4.2.4 on 2023-08-10 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_remove_memos_tag_set2_remove_memos_text3_delete_tag2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memos',
            old_name='update_date',
            new_name='create_date',
        ),
    ]

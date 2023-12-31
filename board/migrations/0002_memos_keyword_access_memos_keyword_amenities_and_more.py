# Generated by Django 4.2.4 on 2023-08-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memos',
            name='keyword_access',
            field=models.IntegerField(default=0, null=True, verbose_name='키워드_접근성'),
        ),
        migrations.AddField(
            model_name='memos',
            name='keyword_amenities',
            field=models.IntegerField(default=0, null=True, verbose_name='키워드_편의시설'),
        ),
        migrations.AddField(
            model_name='memos',
            name='keyword_price',
            field=models.IntegerField(default=0, null=True, verbose_name='키워드_가격'),
        ),
    ]

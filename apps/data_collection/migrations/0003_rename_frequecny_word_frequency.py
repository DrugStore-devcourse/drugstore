# Generated by Django 4.2 on 2023-05-04 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_collection', '0002_word_unique_article_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='frequecny',
            new_name='frequency',
        ),
    ]

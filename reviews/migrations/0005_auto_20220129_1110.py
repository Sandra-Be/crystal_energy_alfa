# Generated by Django 3.2 on 2022-01-29 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.RemoveField(
            model_name='review',
            name='image_url',
        ),
    ]
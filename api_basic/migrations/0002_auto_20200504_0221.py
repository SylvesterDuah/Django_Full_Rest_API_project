# Generated by Django 3.0.5 on 2020-05-04 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auth',
            new_name='author',
        ),
    ]

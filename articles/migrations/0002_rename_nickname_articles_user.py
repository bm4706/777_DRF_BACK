# Generated by Django 4.2.6 on 2023-10-06 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='nickname',
            new_name='user',
        ),
    ]

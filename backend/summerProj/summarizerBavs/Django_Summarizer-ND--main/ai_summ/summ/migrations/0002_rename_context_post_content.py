# Generated by Django 5.0.7 on 2024-08-19 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summ', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='context',
            new_name='content',
        ),
    ]
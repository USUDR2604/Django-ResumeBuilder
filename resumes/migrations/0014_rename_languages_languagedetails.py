# Generated by Django 3.2.5 on 2021-07-12 09:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resumes', '0013_languages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Languages',
            new_name='LanguageDetails',
        ),
    ]
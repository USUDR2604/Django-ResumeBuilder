# Generated by Django 3.2.5 on 2021-07-12 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0011_rename_language_confid_languagedetails_language_confidence'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LanguageDetails',
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-12 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0016_achievementsoractivities_certificationdetails_educationdetails_experiencedetails_hobbiedetails_inter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationdetails',
            old_name='Org_Type',
            new_name='Organization_Type',
        ),
    ]
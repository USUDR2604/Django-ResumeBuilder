# Generated by Django 3.2.5 on 2021-07-13 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0026_achievementsoractivities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshipdetails',
            name='Internship_Job_Description',
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0028_internshipdetails_internship_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencedetails',
            name='Experience_Type',
            field=models.CharField(default='Experience', help_text='Enter Experience Type', max_length=25),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0027_remove_internshipdetails_internship_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipdetails',
            name='Internship_Job_Description',
            field=models.TextField(blank=True, help_text='Enter Experience Description', max_length=800),
        ),
    ]

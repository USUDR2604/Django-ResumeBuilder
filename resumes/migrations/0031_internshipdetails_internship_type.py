# Generated by Django 3.2.5 on 2021-07-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0030_alter_experiencedetails_experience_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipdetails',
            name='Internship_Type',
            field=models.CharField(default='Internship', editable=False, help_text='Enter Internship Type', max_length=25),
        ),
    ]

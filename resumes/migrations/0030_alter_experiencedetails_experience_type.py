# Generated by Django 3.2.5 on 2021-07-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0029_experiencedetails_experience_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencedetails',
            name='Experience_Type',
            field=models.CharField(default='Experience', editable=False, help_text='Enter Experience Type', max_length=25),
        ),
    ]

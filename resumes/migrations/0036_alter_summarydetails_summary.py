# Generated by Django 3.2.5 on 2021-07-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0035_alter_summarydetails_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summarydetails',
            name='Summary',
            field=models.TextField(help_text='Your Information', max_length=1000),
        ),
    ]

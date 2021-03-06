# Generated by Django 3.2.5 on 2021-07-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0018_certificationdetails_certify_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipdetails',
            name='Internship_Company_Name',
            field=models.CharField(default='RAJ SOFTWARE SOLUTIONS', help_text='Enter Company Name', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainingdetails',
            name='Training_ZipCode',
            field=models.CharField(default=686890, help_text='Enter Training Place ZipCode', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='internshipdetails',
            name='Internship_choice',
            field=models.CharField(blank=True, choices=[('OFFLINE', 'OFFLINE'), ('PART TIME', 'PART TIME'), ('ONLINE', 'ONLINE')], max_length=200),
        ),
    ]

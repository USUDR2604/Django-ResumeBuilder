# Generated by Django 3.2.5 on 2021-07-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0002_personaldetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetails',
            name='Address_2',
            field=models.CharField(default='India', help_text='Enter your Address', max_length=800),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='Address',
            field=models.CharField(help_text='Enter your Address', max_length=800),
        ),
    ]

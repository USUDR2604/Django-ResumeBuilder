# Generated by Django 3.2.5 on 2021-08-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0038_achievementsoractivities_actachiev_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievementsoractivities',
            name='ActAchiev_Choice',
            field=models.CharField(choices=[('ACTIVITY', 'ACTIVITY'), ('ACHIEVEMENT', 'ACHIEVEMENT')], default=0, help_text='Choose Either Activity or Achievement', max_length=200),
        ),
    ]

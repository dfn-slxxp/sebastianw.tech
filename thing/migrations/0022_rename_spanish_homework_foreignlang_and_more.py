# Generated by Django 4.2.5 on 2024-10-18 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0021_remove_homework_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='Spanish',
            new_name='ForeignLang',
        ),
        migrations.RenameField(
            model_name='homework',
            old_name='Advisory',
            new_name='HomeRoom',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0002_alter_homework_advisory_alter_homework_band_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='date',
            field=models.DateField(),
        ),
    ]
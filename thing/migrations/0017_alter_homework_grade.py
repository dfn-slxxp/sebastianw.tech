# Generated by Django 4.2.5 on 2024-09-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0016_homework_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='Grade',
            field=models.IntegerField(default='9', null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2024-09-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0017_alter_homework_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='Grade',
            field=models.CharField(default='9', max_length=2, null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0003_alter_homework_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='Advisory',
            field=models.CharField(blank=True, default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='homework',
            name='Band',
            field=models.CharField(blank=True, default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='homework',
            name='ELA',
            field=models.CharField(blank=True, default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='homework',
            name='Math',
            field=models.CharField(blank=True, default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='homework',
            name='Misc',
            field=models.CharField(blank=True, default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='homework',
            name='PE',
            field=models.CharField(blank=True, default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='homework',
            name='Science',
            field=models.CharField(blank=True, default='None', max_length=150),
        ),
        migrations.AlterField(
            model_name='homework',
            name='SocialStudies',
            field=models.CharField(blank=True, default='None', max_length=150),
        ),
    ]

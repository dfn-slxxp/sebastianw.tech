# Generated by Django 4.2.5 on 2023-09-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0006_alter_homework_ela'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='Advisory',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='Band',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='Math',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='Misc',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='PE',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='Science',
            field=models.CharField(default='None, null=True', max_length=150),
        ),
        migrations.AlterField(
            model_name='homework',
            name='SocialStudies',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
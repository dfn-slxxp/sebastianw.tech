# Generated by Django 4.2.5 on 2024-03-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thing', '0011_homework_spanish'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoBeforeAfter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('photoName', models.CharField(default='', max_length=100, null=True)),
                ('desc', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
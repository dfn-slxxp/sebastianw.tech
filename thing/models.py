from django.db import models

# Create your models here.
class Homework(models.Model):
    date = models.DateField()
    ELA = models.CharField(max_length=150, default="None", null=True)
    Math = models.CharField(max_length=150, default="None", null=True)
    Science = models.CharField(max_length=150, default="None", null=True)
    SocialStudies = models.CharField(max_length=150, default="None", null=True)
    Band = models.CharField(max_length=150, default="None", null=True)
    HomeRoom = models.CharField(max_length=150, default="None", null=True)
    PE = models.CharField(max_length=150, default="None", null=True)
    ForeignLang = models.CharField(max_length=150, default="None", null=True)
    Misc = models.CharField(max_length=150, default="None", null=True)

class PhotoBeforeAfter(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100, default="", null=True)
    description = models.CharField(max_length=200, default="", null=True)
    credit = models.CharField(max_length=150, default="", null=True)
    event = models.CharField(max_length=20, default="", null=True)

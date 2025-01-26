from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),

    path("homework/", views.homework, name="homework"),
    path("homework/successful/", views.successful),
    path("homework/<int:num>/edit/", views.edit),

    path("ggbypass/", views.goguardianbypass),

    path("photography/", views.photos),
    path("photography/nyias", views.nyias),
    path("photography/wild", views.wild),

    path("projects/", views.projects),

    path("cats/", views.cats),]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home), # home page with some pics idk
    path("why-us/", views.why), # why we are so sigma
    path("about-us/", views.about), # meet the team and why this ticket
    path("our-mission/", views.mission), # self explanitory + fresh shit i guess
    path("contact/", views.contact), # contact the team
    path("events/", views.events), # events
    path("transparency/", views.transparency), # idk
]

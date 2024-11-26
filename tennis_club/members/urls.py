from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.index, name="index"),
    path(route="members/", view=views.members, name="members"),
    path(route="members/details/<int:id>", view=views.details, name="details"),
    path(route="testing/", view=views.testing, name="testing"),
]

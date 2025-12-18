from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.index, name="index"),
    path(route="members/", view=views.members, name="members"),
    # Unicode characters are allowed in the slug as string
    path(route="members/details/<str:slug>", view=views.details, name="details"),
    path(route="members/table/", view=views.members_table, name="table"),
]

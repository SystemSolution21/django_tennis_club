from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def index(request) -> HttpResponse:
    template = loader.get_template(template_name="index.html")
    return HttpResponse(content=template.render())


def members(request) -> HttpResponse:
    members = Member.objects.all().values()
    template = loader.get_template(template_name="members.html")
    context = {
        "members": members,
    }
    return HttpResponse(content=template.render(context=context, request=request))


def details(request, id) -> HttpResponse:
    members = Member.objects.get(id=id)
    template = loader.get_template(template_name="details.html")
    context = {
        "members": members,
    }
    return HttpResponse(content=template.render(context=context, request=request))


# Testing view
def testing(request):
    template = loader.get_template(template_name="template.html")
    context = {
        "fruits": ["Apple", "Banana", "Orange"],
    }
    return HttpResponse(content=template.render(context=context, request=request))

from django.http import HttpResponse
from django.template import loader

from .models import Member


# Root page
def index(request) -> HttpResponse:
    template = loader.get_template(template_name="members/index.html")
    return HttpResponse(content=template.render())


# Members
def members(request) -> HttpResponse:
    members = Member.objects.all().values()
    template = loader.get_template(template_name="members/members.html")
    context = {
        "members": members,
    }
    return HttpResponse(content=template.render(context=context, request=request))


# Member details
def details(request, slug) -> HttpResponse:
    members = Member.objects.get(slug=slug)
    template = loader.get_template(template_name="members/details.html")
    context = {
        "members": members,
    }
    return HttpResponse(content=template.render(context=context, request=request))


# Member details table
def members_table(request) -> HttpResponse:
    data = Member.objects.all()
    template = loader.get_template(template_name="members/table.html")
    context = {
        "members": data,
    }
    return HttpResponse(content=template.render(context=context, request=request))

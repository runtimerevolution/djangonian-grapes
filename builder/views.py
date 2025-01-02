import json
from django.http import JsonResponse
from django.views.generic import DetailView
from django.core.serializers import serialize

from builder.models import Page


class BuilderView(DetailView):
    model = Page
    template_name = "builder/index.html"
    slug_url_kwarg = "slug"


class PageDetailView(DetailView):
    model = Page
    template_name = "builder/detail.html"
    slug_url_kwarg = "slug"


def save(request, id):
    if request.method == "POST":
        body = json.loads(request.body)
        page = Page.objects.get(id=id)
        page.data = body["data"]
        page.html = body["html"]
        page.css = body["css"]
        page.save()
        return JsonResponse({"success": True})


def load(request, id):
    if request.method == "GET":
        page = Page.objects.get(id=id)
        return JsonResponse({"data": page.data})

from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default="", null=False)

    data = models.JSONField(default=dict, blank=True)
    html = models.TextField(default="", blank=True)
    css = models.TextField(default="", blank=True)

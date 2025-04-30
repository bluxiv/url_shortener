from django.contrib import admin
from shortener.models import Link, Visit

# Register your models here.
admin.site.register(Link)
admin.site.register(Visit)

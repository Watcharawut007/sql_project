from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from django.contrib.auth.models import User
from .models import product, review


admin.site.register(product)
admin.site.register(review)
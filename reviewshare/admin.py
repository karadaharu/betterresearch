from django.contrib import admin

# Register your models here.
from .models import Paper, Review

admin.site.register(Paper)
admin.site.register(Review)

from django.contrib import admin
from .models import Records
# Register your models here.
admin.sites.site.register(Records)
from django.contrib import admin

# Register your models here.
from .models import die, batch

admin.site.register(die)
admin.site.register(batch)

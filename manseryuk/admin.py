from django.contrib import admin
from .models import Manseryuk

class ManseryukAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'month', 'day', 'time', 'gen', 'sl', 'created')


admin.site.register(Manseryuk,ManseryukAdmin)



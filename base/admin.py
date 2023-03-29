from django.contrib import admin
from .models import Submit,Person

class PersonInline(admin.StackedInline):
    model = Person

class SubmitAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'adress', 'phonnumber', 'email', 'created')
    inlines = (
        PersonInline,
    )

class PersonAdmin(admin.ModelAdmin):
    list_display = ('submit', 'name', 'year', 'month', 'day', 'time', 'gen', 'sl', 'created')
    

admin.site.register(Submit,SubmitAdmin)
admin.site.register(Person,PersonAdmin)

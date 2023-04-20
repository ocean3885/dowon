from django.contrib import admin
from .models import Submit,Person
from .models import User
from django.contrib.auth.admin import UserAdmin


class PersonInline(admin.StackedInline):
    model = Person

class SubmitAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'adress', 'phonnumber', 'email', 'created', 'process','complete')
    list_editable = ('process','complete',)
    inlines = (
        PersonInline,
    )

class PersonAdmin(admin.ModelAdmin):
    list_display = ('submit', 'name', 'year', 'month', 'day', 'time', 'gen', 'sl', 'created')
    

UserAdmin.fieldsets += ('Custom fields', {'fields': ('phonnumber',)}),

admin.site.register(Submit,SubmitAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(User, UserAdmin)
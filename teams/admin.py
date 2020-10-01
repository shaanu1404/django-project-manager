from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team_lead', 'category')
    ordering = ('id',)

admin.site.register(Team, TeamAdmin)

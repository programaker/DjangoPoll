# -*- coding: utf-8 -*-

from polls.models import Poll, Choice
from django.contrib import admin


class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Principal', {'fields': ['question']}),
    ('Informações de data', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
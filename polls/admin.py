# -*- coding: utf-8 -*-

from polls.models import Poll, Choice
from django.contrib import admin


class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 0


class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Principal', {'fields': ['question']}),
    ('Informações de data', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]

  inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)

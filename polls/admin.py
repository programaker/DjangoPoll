# -*- coding: utf-8 -*-

from polls.models import Poll, Choice
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 0


class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Principal', {'fields': ['question']}),
    ('Informações de data', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]

  inlines = [ChoiceInline]
  list_display = ('question', 'pub_date', 'was_published_today')
  list_filter = ['pub_date']
  search_fields = ['question']
  date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)

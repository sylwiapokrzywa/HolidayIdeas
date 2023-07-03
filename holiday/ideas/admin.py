from django.contrib import admin
from django.utils.html import format_html
from .models import Idea, Vote


class VoteInline(admin.StackedInline):
    model = Vote

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['country']
    list_display = ['country', 'status', 'show_holiday_url']
    list_filter = ['country']
    inlines = [
        VoteInline
    ]

    def show_holiday_url(self, obj):
        if obj.holiday_url is not None:
            return format_html(f'<a href="{obj.holiday_url}" target="_blank">{obj.holiday_url}</a>')
        else:
            return ''

    show_holiday_url.short_description = 'Holiday URL'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']
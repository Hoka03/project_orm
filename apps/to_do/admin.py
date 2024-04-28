from django.contrib import admin

from apps.to_do.models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'description',
                    'done', 'done_at', 'start_date', 'days', 'created_at')
    list_display_links = list_display
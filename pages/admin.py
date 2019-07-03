from django.contrib import admin
from .models import Index


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'subheading', 'name', 'is_published')
    list_display_links = ('id', 'subheading', 'name')
    list_editable = ('is_published',)
    search_fields = ('subheading', 'description', 'name')
    list_per_page = 25


admin.site.register(Index, MenuAdmin)

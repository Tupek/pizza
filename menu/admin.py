from django.contrib import admin
from .models import Pizza, Burgers, Pasta, Drinks

class MenuAdmin(admin.ModelAdmin):
    list_display = ('numb', 'title', 'price', 'is_pub')
    list_display_links = ('numb', 'title')
    list_editable = ('is_pub',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 25


admin.site.register(Pizza, MenuAdmin)
admin.site.register(Burgers, MenuAdmin)
admin.site.register(Pasta, MenuAdmin)
admin.site.register(Drinks, MenuAdmin)
# Register your models here.

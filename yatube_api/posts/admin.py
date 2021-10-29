from django.contrib import admin

from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    search_fields = ('title',)
    empty_value_display = '-пусто-'
    list_editable = ('description',)


admin.site.register(Group, GroupAdmin)

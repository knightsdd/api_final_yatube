from django.contrib import admin

from .models import Follow, Group


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


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)

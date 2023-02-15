from parser.models import News, Tag

from django.contrib import admin


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'link', 'text', 'pub_date', 'tags', )
    list_filter = ('pub_date', 'tags', )
    search_fields = ('title', 'tags', )
    ordering = ('-pub_date', )


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )

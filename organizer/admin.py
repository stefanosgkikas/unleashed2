from django.contrib import admin
from .models import NewsLink, Startup, Tag

@admin.register(NewsLink)
class NewsLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'startup', 'pub_date')
    search_fields = ('name', 'startup')
    list_filter = ('pub_date',)

@admin.register(Tag) 
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'founded_date')
    list_filter = ('founded_date',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

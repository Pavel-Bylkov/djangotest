from django.contrib import admin
from .models import Blog, Author, Entry
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tagline')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'tagline')
    search_fields = ('name', 'tagline')

@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    readonly_fields = ('email',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'headline', 'pub_date', 'rating')
    list_display_links = ('id', 'blog')

#admin.site.register(Blog, BlogAdmin)
#admin.site.register(Author, AutorAdmin)
admin.site.register(Entry, EntryAdmin)
